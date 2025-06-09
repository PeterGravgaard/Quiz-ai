#!/usr/bin/env python3
"""
Demo script to show the Quiz AI application functionality
"""

import sys
import os
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QTimer, Qt

# Import our main classes
sys.path.append('.')
from main import MainWindow, QuizWindow

def demo_app():
    """Demo the application with some test data"""
    app = QApplication(sys.argv)
    
    # Create main window
    main_window = MainWindow()
    
    # Set demo data
    main_window.api_key_input.setText("demo-api-key-placeholder")
    main_window.topic_input.setText("Dansk historie")
    
    print("Demo app started!")
    print("- API key field set to demo value")
    print("- Topic set to 'Dansk historie'")
    print("- Main window should be visible")
    print("- Click 'Start Quiz' to proceed (note: will fail without real API key)")
    
    main_window.show()
    
    return app.exec_()

if __name__ == '__main__':
    demo_app()
