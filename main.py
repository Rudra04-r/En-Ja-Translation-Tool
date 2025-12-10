# ================================
# Google-Translate-like: English -> Japanese + Romaji + Word-by-word
# ================================

import sys, subprocess, pkgutil
def pip_install(pkg):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
    
if not pkgutil.find_loader("googletrans"):
    pip_install("googletrans==4.0.0-rc1")

if not pkgutil.find_loader("pykakasi"):
    pip_install("pykakasi")
    
from googletrans import Translator
from pykakasi import kakasi
import re


translator = Translator()
_kakasi = kakasi()
_kakasi.setMode("H", "a")   
_kakasi.setMode("K", "a")   
_kakasi.setMode("J", "a")   
_kakasi.setMode("r", "Hepburn")
_kakasi.setMode("s", True)
_converter = _kakasi.getConverter()


def tokenize_eng(text):
    
    text = text.strip()
    
    tokens = re.findall(r"[A-Za-z0-9']+|[^\sA-Za-z0-9]+", text)
    
    tokens = [t for t in tokens if t.strip() != ""]
    return tokens

def japanese_to_romaji(japanese_text):
    if not japanese_text:
        return ""
    try:
        romaji = _converter.do(japanese_text)
        romaji = re.sub(r'\s+', ' ', romaji).strip()
        return romaji
    except Exception:
        return ""


def translate_full(text):
    
    res = translator.translate(text, dest='ja', src='en')
    jap = res.text
    
    pron = getattr(res, "pronunciation", None)
    romaji = pron if pron else japanese_to_romaji(jap)
    return jap, romaji


def translate_word_by_word(text):
    tokens = tokenize_eng(text)
    word_results = []
    for tok in tokens:
        
        if re.fullmatch(r"[^\w']+", tok):
            word_results.append((tok, tok, "")) 
            continue
        
        try:
            r = translator.translate(tok, dest='ja', src='en')
            jap = r.text
            pron = getattr(r, "pronunciation", None)
            romaji = pron if pron else japanese_to_romaji(jap)
            word_results.append((tok, jap, romaji))
        except Exception:
            
            word_results.append((tok, tok, ""))
    return word_results


print("English → Japanese translator (Google-like). Type 'quit' or 'exit' to stop.")
print("You will get: (1) full sentence translation, (2) romaji/transliteration, (3) word-by-word breakdown.\n")

while True:
    try:
        text = input("English: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nExiting.")
        break
    if not text:
        print("Please type a sentence or 'quit' to exit.")
        continue
    if text.lower() in ("quit", "exit"):
        print("Goodbye.")
        break

    
    try:
        japanese, romaji = translate_full(text)
    except Exception as e:
        print("Full translation failed:", str(e))
        japanese, romaji = "", ""

    
    try:
        wb = translate_word_by_word(text)
    except Exception as e:
        print("Word-by-word translation failed:", str(e))
        wb = []

    
    print("\n--- Result ---")
    if japanese:
        print("Japanese:", japanese)
    else:
        print("Japanese: [no translation available]")

    if romaji:
        print("Romaji:", romaji)
    else:
        print("Romaji: [no romaji available]")

    
    if wb:
        print("\nWord-by-word:")
    
        print(f"{'English':<20} {'Japanese':<30} {'Romaji'}")
        print("-" * 70)
        for eng_tok, jap_tok, roma_tok in wb:
            
            eng_disp = (eng_tok[:18] + "..") if len(eng_tok) > 20 else eng_tok
            jap_disp = (jap_tok[:28] + "..") if len(jap_tok) > 30 else jap_tok
            roma_disp = (roma_tok[:40] + "..") if len(roma_tok) > 42 else roma_tok
            print(f"{eng_disp:<20} {jap_disp:<30} {roma_disp}")
    print("\n") 
