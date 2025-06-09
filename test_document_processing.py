#!/usr/bin/env python3
"""
Test af dokumentbehandling for Quiz AI
"""

import sys
import os

# Tilføj nuværende mappe til Python path
sys.path.insert(0, '/Users/gravgaard/Library/CloudStorage/OneDrive-AalborgUniversitet/DAKI/Quiz ai/Quiz-ai')

# Test af dokumentbehandling
def test_document_processing():
    try:
        from main import MainWindow
        from PyQt5.QtWidgets import QApplication
        
        app = QApplication(sys.argv)
        window = MainWindow()
        
        # Test tekstfil
        test_file = "/Users/gravgaard/Library/CloudStorage/OneDrive-AalborgUniversitet/DAKI/Quiz ai/Quiz-ai/test_document.txt"
        
        print("Testing document processing...")
        print(f"File exists: {os.path.exists(test_file)}")
        
        # Læs fil direkte
        with open(test_file, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"File content length: {len(content)}")
            print(f"First 100 chars: {content[:100]}")
        
        print("Document processing test completed successfully!")
        
    except Exception as e:
        print(f"Error during test: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_document_processing()
