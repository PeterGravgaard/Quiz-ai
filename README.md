# Quiz AI - Multiple Choice Quiz med Gemini API

## ✅ STATUS: KLAR TIL BRUG!
**Alle AttributeError problemer er løst. Applikationen virker nu perfekt!**

En Python applikation der bruger Google's Gemini API til at generere multiple choice spørgsmål baseret på brugerens valgte emne.

## Funktionalitet

- **API Key Input**: Indtast din Gemini API key direkte i applikationen
- **Emne-valg**: Indtast det emne du vil have spørgsmål om
- **AI-genererede spørgsmål**: Bruger Gemini API til at lave relevante spørgsmål
- **Multiple choice**: Fire svarmuligheder (A, B, C, D)
- **Øjeblikkelig feedback**: Viser om svaret er rigtigt eller forkert
- **Detaljerede forklaringer**: Får forklaring på det rigtige svar
- **Modern UI**: Designet med Qt Designer
- **Direkte API Key link**: Knap til at åbne Google AI Studio

## Installation

1. **Installer Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Få en Gemini API key:**
   - Applikationen har en "Få API Key" knap der åbner [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Alternativt kan du manuelt gå til linket og oprette en API key

## Brug

1. **Start applikationen:**
   ```bash
   python main.py
   ```

2. **Brug applikationen:**
   - Indtast din Gemini API key (klik "Få API Key" hvis du ikke har en)
   - Indtast et emne (f.eks. "Historie", "Matematik", "Biologi")
   - Klik "Start Quiz"
   - Vælg dit svar blandt de fire muligheder
   - Klik "Svar" for at se resultatet
   - Klik "Næste Spørgsmål" for at fortsætte

## Filstruktur

- `main.py` - Hovedapplikation med al logik
- `main_window.ui` - Qt Designer fil til emne-valg siden (nu med API key input)
- `quiz_window.ui` - Qt Designer fil til quiz siden
- `requirements.txt` - Python dependencies
- `.env` - Konfigurationsfil (valgfri - API key kan indtastes i UI'en)

## Funktioner

### Hovedvindue
- **API Key Input**: Sikkert password-felt til API key
- **"Få API Key" knap**: Åbner Google AI Studio direkte
- **Emne Input**: Simpel input til emne-valg
- **Modern og brugervenlig design**
- **Validering af både API key og emne-input**

### Quiz-vindue
- Viser spørgsmål og fire svarmuligheder
- Real-time feedback på svar
- Farvekodet feedback (grøn for rigtigt, rød for forkert)
- Detaljerede forklaringer
- Mulighed for at fortsætte med nye spørgsmål

### API Integration
- API key indtastes direkte i UI'en (ingen .env fil nødvendig)
- Asynkron kommunikation med Gemini API
- Fejlhåndtering for API-kald
- JSON parsing af AI-svar
- Thread-baseret loading for bedre brugeroplevelse

## Fejlhåndtering

Applikationen håndterer forskellige fejlsituationer:
- Manglende API key (nu med brugervenlig påmindelse)
- Ugyldig API key (fejlbesked fra Gemini API)
- Netværksfejl
- Parsing-fejl af AI-svar
- Bruger-input validation

## Sikkerhed

- API key vises som password-felt (skjult tekst)
- API key gemmes ikke permanent - skal indtastes ved hver start
- Ingen sensitive data gemmes lokalt

## Tilpasning

Du kan nemt tilpasse applikationen:
- Ændre UI design i `.ui` filerne med Qt Designer
- Modificere AI-prompts i `QuestionGenerator` klassen
- Tilføje flere spørgsmålstyper eller sværhedsgrader
- Implementere score-tracking eller andre features
- Tilføje API key gemning (hvis ønsket)

## 🔧 Løste Problemer

Følgende problemer er blevet rettet:
- ✅ **AttributeError**: Alle UI element navne matcher nu mellem .ui filer og Python kode
- ✅ **Button navne**: `start_quiz_button` → `start_quiz_btn`, `get_api_key_button` → `get_api_key_btn`
- ✅ **Option buttons**: `option_a` → `option_a_btn` (samme for B, C, D)
- ✅ **Submit/Next buttons**: `submit_button` → `submit_btn`, `next_button` → `next_btn`
- ✅ **Missing labels**: Kombineret `explanation_label` og `loading_label` funktionalitet i eksisterende labels
- ✅ **API model**: Opdateret fra deprecated `gemini-pro` til `gemini-1.5-flash`

## 🧪 Testing

Kør disse tests for at verificere funktionalitet:

```bash
# Test at alle UI elementer eksisterer
python test_ui.py

# Demo applikation med pre-filled data  
python demo.py

# Direkte applikation test
python main.py
```
