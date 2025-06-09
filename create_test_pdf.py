#!/usr/bin/env python3
"""
Opret en simpel PDF test-fil til Quiz AI
"""

try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    import os
    
    def create_test_pdf():
        filename = "/Users/gravgaard/Library/CloudStorage/OneDrive-AalborgUniversitet/DAKI/Quiz ai/Quiz-ai/test_matematik.pdf"
        
        # Opret PDF
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter
        
        # Tilføj tekst
        c.setFont("Helvetica", 16)
        c.drawString(100, height - 100, "Matematik Test Dokument")
        
        c.setFont("Helvetica", 12)
        y = height - 150
        
        content = [
            "Dette er et test dokument om matematik til Quiz AI.",
            "",
            "Grundlæggende matematik:",
            "- Addition: 2 + 3 = 5",
            "- Subtraktion: 5 - 2 = 3", 
            "- Multiplikation: 4 × 3 = 12",
            "- Division: 12 ÷ 4 = 3",
            "",
            "Geometri:",
            "- Arealet af en kvadrat: side × side",
            "- Arealet af en cirkel: π × radius²",
            "- Omkredsen af en cirkel: 2 × π × radius",
            "",
            "Algebra:",
            "- En ligning er et matematisk udsagn med et lighedstegn",
            "- Eksempel: x + 5 = 10, hvor x = 5",
        ]
        
        for line in content:
            c.drawString(100, y, line)
            y -= 20
        
        c.save()
        print(f"PDF oprettet: {filename}")
        return filename
    
    if __name__ == "__main__":
        create_test_pdf()
        
except ImportError:
    print("reportlab er ikke installeret. Kører pip install...")
    import subprocess
    subprocess.run(["pip", "install", "reportlab"])
    print("Prøv at køre scriptet igen.")
