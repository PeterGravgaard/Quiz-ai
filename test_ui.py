#!/usr/bin/env python3
"""
Test script to validate UI elements exist
"""

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

def test_main_window():
    """Test that main window UI elements exist"""
    print("Testing main window UI elements...")
    
    app = QApplication(sys.argv)
    main_window = uic.loadUi('main_window.ui')
    
    # Test required elements
    required_elements = [
        'api_key_input',
        'topic_input', 
        'start_quiz_btn',
        'get_api_key_btn'
    ]
    
    for element in required_elements:
        if hasattr(main_window, element):
            print(f"✅ {element} exists")
        else:
            print(f"❌ {element} MISSING")
    
    app.quit()

def test_quiz_window():
    """Test that quiz window UI elements exist"""
    print("\nTesting quiz window UI elements...")
    
    app = QApplication(sys.argv)
    quiz_window = uic.loadUi('quiz_window.ui')
    
    # Test required elements
    required_elements = [
        'topic_label',
        'question_label',
        'option_a_btn',
        'option_b_btn', 
        'option_c_btn',
        'option_d_btn',
        'result_label',
        'submit_btn',
        'next_btn'
    ]
    
    for element in required_elements:
        if hasattr(quiz_window, element):
            print(f"✅ {element} exists")
        else:
            print(f"❌ {element} MISSING")
    
    app.quit()

if __name__ == '__main__':
    test_main_window()
    test_quiz_window()
    print("\nUI validation complete!")
