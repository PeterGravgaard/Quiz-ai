# Quiz AI - Dokumentupload Funktionalitet

## 🎉 Ny Funktionalitet Tilføjet!

Din Quiz AI applikation understøtter nu dokumentupload til generering af quiz spørgsmål!

## 🔧 Funktioner

### Understøttede Filtyper
- **PDF filer** (.pdf)
- **Word dokumenter** (.docx, .doc)
- **Excel regneark** (.xlsx, .xls)
- **Tekst filer** (.txt)

### Sådan Bruger Du Det

1. **Start applikationen**
   ```bash
   python main.py
   ```

2. **Vælg metode til at oprette quiz:**
   - **Mulighed 1**: Indtast emne manuelt (som før)
   - **Mulighed 2**: Upload dokument (NYT!)

3. **Upload dokument:**
   - Klik på "Vælg Dokument" knappen
   - Vælg din fil (PDF, Word, Excel eller tekst)
   - Filstien vises i input feltet

4. **Indtast din API key** (som før)

5. **Start quiz** - AI'en genererer nu spørgsmål baseret på dokumentets indhold!

## ⚡ Funktionalitet

### Dokumentbehandling
- **PDF**: Uddrag tekst fra alle sider
- **Word**: Uddrag tekst fra alle paragraffer
- **Excel**: Uddrag data fra alle ark og celler
- **Tekst**: Læs direkte fra fil

### Intelligent Quiz Generering
- AI'en analyserer dokumentets indhold
- Genererer relevante multiple choice spørgsmål
- Inkluderer forklaringer baseret på dokumentet

### Validering
- Tjekker at enten emne ELLER dokument er valgt
- Viser fejlmeddelelser ved problemer
- Rydder input felter automatisk

## 🧪 Test Filer Inkluderet

- `test_document.txt` - Matematik test dokument
- `test_matematik.pdf` - PDF test dokument
- `test_complete_functionality.py` - Test script

## 🔧 Tekniske Detaljer

### Nye Dependencies
- `PyPDF2==3.0.1` - PDF behandling
- `python-docx==1.1.0` - Word dokument behandling
- `openpyxl==3.1.2` - Excel behandling

### Nye UI Elementer
- Dokument upload sektion
- Fil sti input felt
- "Vælg Dokument" knap

### Kode Ændringer
- Nye dokumentbehandlingsfunktioner i `MainWindow`
- Opdateret `start_quiz` metode til at håndtere begge input typer
- Forbedret AI prompt til dokumentbaserede spørgsmål

## 🎯 Brug

Perfect til:
- Undervisning: Upload pensum og få automatiske quiz
- Revision: Upload noter og test dig selv  
- Træning: Upload faglige tekster og øv
- Læring: Upload dokumenter og få spørgsmål

Hav det sjovt med din opgraderede Quiz AI! 🚀
