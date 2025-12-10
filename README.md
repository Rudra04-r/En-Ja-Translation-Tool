# En-Ja-Translation-Tool  
A Python-based interactive English-to-Japanese translation tool that provides full-sentence translation, romaji conversion, and word-by-word breakdown. Designed for language learners, developers, and anyone interested in Japanese NLP.

---

# 🚀 Features

# 1. Full Sentence Translation
- Translates English sentences into Japanese using googletrans.
- Provides natural, context-aware Japanese output.

# 2. Romaji Conversion
- Uses pykakasi to convert Japanese text into romaji (Latin script).
- Helps users read and pronounce Japanese easily.

# 3. Word-by-Word Translation
- Tokenizes English input using regular expressions.
- Translates each word individually for detailed understanding.
- Displays results in a clean, well-formatted table:
  - English word  
  - Japanese translation  
  - Romaji pronunciation  

# 4. Interactive CLI
- Accepts multiple inputs continuously.
- Type `quit` or `exit` to stop the program.

# 5. Error Handling
- Gracefully handles translation issues or network/API errors.
- Ensures smooth user experience.

---

# 📦 Dependencies

The tool automatically installs the required packages if missing:

- `googletrans==4.0.0-rc1`
- `pykakasi`
- `re` (built-in)
- `sys`, `subprocess`, `pkgutil` (built-in)

---

# Example

English → Japanese translator (Google-like). Type 'quit' or 'exit' to stop.

English: I love learning Japanese.
Japanese: 日本語を学ぶのが大好きです
Romaji: Nihongo o manabu no ga daisuki desu

Word-by-word:
English              Japanese                      Romaji
--------------------------------------------------------------
I                    私                            watashi
love                 愛する                        aisuru
learning             学ぶ                          manabu
Japanese             日本語                        nihongo

.                    .                            
