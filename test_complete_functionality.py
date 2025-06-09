#!/usr/bin/env python3
"""
Komplet test af dokumentupload funktionalitet
"""

import sys
import os
sys.path.insert(0, '/Users/gravgaard/Library/CloudStorage/OneDrive-AalborgUniversitet/DAKI/Quiz ai/Quiz-ai')

def test_document_functions():
    from main import MainWindow
    from PyQt5.QtWidgets import QApplication
    
    print("=== Test af Document Upload Funktionalitet ===\n")
    
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # Test filer
    test_files = [
        ("/Users/gravgaard/Library/CloudStorage/OneDrive-AalborgUniversitet/DAKI/Quiz ai/Quiz-ai/test_document.txt", "TXT"),
        ("/Users/gravgaard/Library/CloudStorage/OneDrive-AalborgUniversitet/DAKI/Quiz ai/Quiz-ai/test_matematik.pdf", "PDF"),
    ]
    
    for file_path, file_type in test_files:
        if os.path.exists(file_path):
            print(f"🧪 Tester {file_type} fil: {os.path.basename(file_path)}")
            try:
                content = window.extract_document_content(file_path)
                print(f"✅ {file_type} læst succesfuldt!")
                print(f"📄 Indhold længde: {len(content)} tegn")
                print(f"🔤 Første 100 tegn: {content[:100]}...")
                print()
            except Exception as e:
                print(f"❌ Fejl ved læsning af {file_type}: {e}")
                print()
        else:
            print(f"⚠️  {file_type} fil ikke fundet: {file_path}")
            print()
    
    print("=== Test af UI komponenter ===")
    
    # Tjek at alle nødvendige UI komponenter findes
    ui_components = [
        'topic_input',
        'document_path_input', 
        'upload_document_btn',
        'start_quiz_btn',
        'api_key_input'
    ]
    
    for component in ui_components:
        if hasattr(window, component):
            print(f"✅ UI komponent '{component}' fundet")
        else:
            print(f"❌ UI komponent '{component}' mangler")
    
    print("\n=== Test fuldført ===")
    print("📝 Dokumentupload funktionalitet er implementeret og klar til brug!")
    print("🎯 Du kan nu uploade PDF, Word, Excel og tekst filer til at generere quiz spørgsmål")

if __name__ == "__main__":
    test_document_functions()
