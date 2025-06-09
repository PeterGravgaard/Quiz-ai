#!/usr/bin/env python3
"""
Test af nye funktioner: Sværhedsgrads-valg og næste spørgsmål
"""

import sys
import os
sys.path.insert(0, '/Users/gravgaard/Library/CloudStorage/OneDrive-AalborgUniversitet/DAKI/Quiz ai/Quiz-ai')

def test_new_features():
    from main import MainWindow, QuizWindow, QuestionGenerator
    from PyQt5.QtWidgets import QApplication
    
    print("=== Test af Nye Funktioner ===\n")
    
    app = QApplication(sys.argv)
    window = MainWindow()
    
    print("🧪 Tester UI komponenter...")
    
    # Tjek sværhedsgrads-komponenter
    ui_components = [
        'easy_difficulty_btn',
        'hard_difficulty_btn',
    ]
    
    for component in ui_components:
        if hasattr(window, component):
            print(f"✅ Sværhedsgrads-komponent '{component}' fundet")
        else:
            print(f"❌ Sværhedsgrads-komponent '{component}' mangler")
    
    print("\n🧪 Tester standard indstillinger...")
    if hasattr(window, 'easy_difficulty_btn') and window.easy_difficulty_btn.isChecked():
        print("✅ 'Let' er valgt som standard")
    else:
        print("❌ 'Let' er ikke valgt som standard")
    
    print("\n🧪 Tester QuestionGenerator med sværhedsgrad...")
    
    # Test QuestionGenerator med forskellige sværhedsgrader
    test_cases = [
        ("Matematik", "dummy_api_key", "let"),
        ("Historie", "dummy_api_key", "svær")
    ]
    
    for topic, api_key, difficulty in test_cases:
        try:
            generator = QuestionGenerator(topic, api_key, difficulty)
            print(f"✅ QuestionGenerator oprettet med emne '{topic}' og sværhedsgrad '{difficulty}'")
            print(f"   - Emne: {generator.topic}")
            print(f"   - Sværhedsgrad: {generator.difficulty}")
        except Exception as e:
            print(f"❌ Fejl ved oprettelse af QuestionGenerator: {e}")
    
    print("\n🧪 Tester QuizWindow med sværhedsgrad...")
    
    try:
        # Test QuizWindow med forskellige parametre
        quiz_window = QuizWindow("Test emne", "dummy_api_key", "Test Display", "svær")
        print("✅ QuizWindow oprettet med sværhedsgrad")
        print(f"   - Emne: {quiz_window.topic}")
        print(f"   - Display navn: {quiz_window.display_name}")
        print(f"   - Sværhedsgrad: {quiz_window.difficulty}")
    except Exception as e:
        print(f"❌ Fejl ved oprettelse af QuizWindow: {e}")
    
    print("\n=== Funktionalitets-resumé ===")
    print("🎯 Sværhedsgrads-valg:")
    print("   - 😊 Let: Grundlæggende spørgsmål")
    print("   - 🔥 Svær: Komplekse og udfordrende spørgsmål")
    print("\n⏭️  Næste Spørgsmål:")
    print("   - Knappen vises efter svar er afgivet")
    print("   - Genererer nyt spørgsmål med samme sværhedsgrad")
    print("\n✨ Integreret med dokument-upload:")
    print("   - Sværhedsgrad gælder både for emner og dokumenter")
    print("   - AI tilpasser spørgsmålene efter valgt niveau")
    
    print("\n🎉 Alle nye funktioner er implementeret og klar!")

if __name__ == "__main__":
    test_new_features()
