import sys
import os
import json
import webbrowser
import google.generativeai as genai
from dotenv import load_dotenv
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import uic

# Load environment variables
load_dotenv()

class QuestionGenerator(QThread):
    """Thread til at generere spørgsmål i baggrunden"""
    question_ready = pyqtSignal(dict)
    error_occurred = pyqtSignal(str)
    
    def __init__(self, topic, api_key):
        super().__init__()
        self.topic = topic
        self.api_key = api_key
        self.model = None
        
    def run(self):
        try:
            # Konfigurer Gemini API
            if not self.api_key or self.api_key.strip() == '':
                self.error_occurred.emit("Gemini API key er ikke indtastet. Indtast venligst din API key.")
                return
                
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-pro')
            
            # Prompt til at generere spørgsmål
            prompt = f"""
            Lav et multiple choice spørgsmål om emnet: {self.topic}
            
            Formatet skal være JSON og se sådan ud:
            {{
                "question": "Spørgsmålet her",
                "options": {{
                    "A": "Svarmulighed A",
                    "B": "Svarmulighed B", 
                    "C": "Svarmulighed C",
                    "D": "Svarmulighed D"
                }},
                "correct_answer": "A",
                "explanation": "Forklaring på hvorfor dette er det rigtige svar"
            }}
            
            Sørg for at spørgsmålet er passende svært og at forklaringen er detaljeret.
            Sørg for at svaret er på dansk.
            """
            
            response = self.model.generate_content(prompt)
            
            # Parse JSON response
            response_text = response.text.strip()
            if response_text.startswith('```json'):
                response_text = response_text[7:-3]
            elif response_text.startswith('```'):
                response_text = response_text[3:-3]
                
            question_data = json.loads(response_text)
            self.question_ready.emit(question_data)
            
        except Exception as e:
            self.error_occurred.emit(f"Fejl ved generering af spørgsmål: {str(e)}")

class MainWindow(QMainWindow):
    """Hovedvindue til at vælge emne"""
    
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.setup_connections()
        
    def load_ui(self):
        """Load UI fil"""
        ui_path = os.path.join(os.path.dirname(__file__), 'main_window.ui')
        uic.loadUi(ui_path, self)
        
    def setup_connections(self):
        """Opsæt signal-slot forbindelser"""
        self.start_quiz_btn.clicked.connect(self.start_quiz)
        self.topic_input.returnPressed.connect(self.start_quiz)
        self.api_key_input.returnPressed.connect(self.start_quiz)
        self.get_api_key_btn.clicked.connect(self.open_api_key_page)
        
    def start_quiz(self):
        """Start quiz med det valgte emne"""
        topic = self.topic_input.text().strip()
        api_key = self.api_key_input.text().strip()
        
        if not api_key:
            QMessageBox.warning(self, "Fejl", "Indtast venligst din Gemini API key!")
            return
            
        if not topic:
            QMessageBox.warning(self, "Fejl", "Indtast venligst et emne!")
            return
            
        # Åbn quiz vindue
        self.quiz_window = QuizWindow(topic, api_key)
        self.quiz_window.show()
        self.hide()
        
    def open_api_key_page(self):
        """Åbn Google AI Studio til at få API key"""
        webbrowser.open("https://makersuite.google.com/app/apikey")
        QMessageBox.information(
            self, 
            "API Key Info", 
            "Din browser åbner nu Google AI Studio.\n\n" +
            "1. Log ind med din Google konto\n" +
            "2. Klik 'Create API Key'\n" +
            "3. Kopier din API key\n" +
            "4. Indsæt den i feltet herover"
        )

class QuizWindow(QMainWindow):
    """Vindue til at vise spørgsmål og håndtere svar"""
    
    def __init__(self, topic, api_key):
        super().__init__()
        self.topic = topic
        self.api_key = api_key
        self.current_question = None
        self.load_ui()
        self.setup_connections()
        self.setup_ui()
        self.generate_new_question()
        
    def load_ui(self):
        """Load UI fil"""
        ui_path = os.path.join(os.path.dirname(__file__), 'quiz_window.ui')
        uic.loadUi(ui_path, self)
        
    def setup_connections(self):
        """Opsæt signal-slot forbindelser"""
        self.submit_btn.clicked.connect(self.submit_answer)
        self.next_btn.clicked.connect(self.next_question)
        
    def setup_ui(self):
        """Opsæt UI elementer"""
        self.topic_label.setText(f"Emne: {self.topic}")
        self.result_label.hide()
        
    def generate_new_question(self):
        """Generer nyt spørgsmål"""
        self.question_label.setText("Genererer spørgsmål...")
        self.disable_options()
        
        # Start thread til at generere spørgsmål
        self.question_thread = QuestionGenerator(self.topic, self.api_key)
        self.question_thread.question_ready.connect(self.display_question)
        self.question_thread.error_occurred.connect(self.handle_error)
        self.question_thread.start()
        
    def display_question(self, question_data):
        """Vis det genererede spørgsmål"""
        self.current_question = question_data
        
        # Opdater UI
        self.question_label.setText(question_data["question"])
        self.option_a_btn.setText(f"A) {question_data['options']['A']}")
        self.option_b_btn.setText(f"B) {question_data['options']['B']}")
        self.option_c_btn.setText(f"C) {question_data['options']['C']}")
        self.option_d_btn.setText(f"D) {question_data['options']['D']}")
        
        # Aktivér knapper
        self.enable_options()
        self.submit_btn.setEnabled(True)
        self.next_btn.hide()
        self.result_label.hide()
        
    def disable_options(self):
        """Deaktivér svar muligheder"""
        self.option_a_btn.setEnabled(False)
        self.option_b_btn.setEnabled(False)
        self.option_c_btn.setEnabled(False)
        self.option_d_btn.setEnabled(False)
        self.submit_btn.setEnabled(False)
        
    def enable_options(self):
        """Aktivér svar muligheder"""
        self.option_a_btn.setEnabled(True)
        self.option_b_btn.setEnabled(True)
        self.option_c_btn.setEnabled(True)
        self.option_d_btn.setEnabled(True)
        
        # Clear previous selections
        self.option_a_btn.setChecked(False)
        self.option_b_btn.setChecked(False)
        self.option_c_btn.setChecked(False)
        self.option_d_btn.setChecked(False)
        
    def get_selected_answer(self):
        """Få det valgte svar"""
        if self.option_a_btn.isChecked():
            return "A"
        elif self.option_b_btn.isChecked():
            return "B"
        elif self.option_c_btn.isChecked():
            return "C"
        elif self.option_d_btn.isChecked():
            return "D"
        return None
        
    def submit_answer(self):
        """Submit svar og vis resultat"""
        selected = self.get_selected_answer()
        if not selected:
            QMessageBox.warning(self, "Fejl", "Vælg venligst et svar!")
            return
            
        correct = self.current_question["correct_answer"]
        is_correct = selected == correct
        
        # Vis resultat
        if is_correct:
            result_text = "✅ Rigtigt!\n\n"
            self.result_label.setStyleSheet(
                "font-size: 12pt; background-color: #e8f5e8; border: 1px solid #4caf50; border-radius: 5px; color: #2e7d32;"
            )
        else:
            result_text = f"❌ Forkert!\nDet rigtige svar var: {correct}\n\n"
            self.result_label.setStyleSheet(
                "font-size: 12pt; background-color: #ffebee; border: 1px solid #f44336; border-radius: 5px; color: #c62828;"
            )
            
        result_text += f"Forklaring: {self.current_question['explanation']}"
        self.result_label.setText(result_text)
        self.result_label.show()
        
        # Deaktivér submit knap og vis næste knap
        self.submit_btn.setEnabled(False)
        self.next_btn.show()
        
    def next_question(self):
        """Gå til næste spørgsmål"""
        self.generate_new_question()
        
    def handle_error(self, error_message):
        """Håndter fejl"""
        QMessageBox.critical(self, "Fejl", error_message)
        self.question_label.setText("Fejl ved indlæsning af spørgsmål")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
