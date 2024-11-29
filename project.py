import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# To make language detection more consistent
DetectorFactory.seed = 0

# Function to perform translation
def translate_text():
    try:
        # Get selected source language
        src_lang_name = src_lang_combo.get()
        src_lang = lang_code_map.get(src_lang_name, None)
        if not src_lang:
            messagebox.showerror("Error", f"Source language '{src_lang_name}' is not supported.")
            return
        
        # Get the text to translate
        text = text_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter text to translate!")
            return
        
        # Auto-detect source language if 'auto' is selected
        if src_lang == "auto":
            try:
                detected_lang = detect(text)
                confirmation = messagebox.askyesno(
                    "Language Detection",
                    f"Detected language: {detected_lang.upper()}.\nDo you want to continue with this?"
                )
                if not confirmation:
                    return
                src_lang = detected_lang
            except LangDetectException:
                messagebox.showerror("Error", "Could not detect the language. Please enter more text.")
                return
        
        # Get selected target language
        target_lang_name = target_lang_combo.get()
        target_lang = lang_code_map.get(target_lang_name, None)
        if not target_lang:
            messagebox.showerror("Error", f"Target language '{target_lang_name}' is not supported.")
            return
        
        # Perform translation
        result_output.delete("1.0", tk.END)
        translated_text = GoogleTranslator(source=src_lang, target=target_lang).translate(text)
        result_output.insert(tk.END, f"Translation in {target_lang_name}:\n{translated_text}\n\n")
        
        # Save translation history
        history_listbox.insert(tk.END, f"{src_lang_name} -> {target_lang_name}: {translated_text}")
    
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")

# Function to clear input and output areas
def clear_text():
    text_input.delete("1.0", tk.END)
    result_output.delete("1.0", tk.END)

# Function to clear history
def clear_history():
    history_listbox.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("LinguaFlow")
window.geometry("1200x700")
window.resizable(True, True)

# Frames for layout
top_frame = tk.Frame(window, bg="#FFDEE9")  # Light pink
top_frame.pack(fill="x", padx=10, pady=10)

middle_frame = tk.Frame(window, bg="#B5FFFC")  # Light teal
middle_frame.pack(fill="both", expand=True, padx=10, pady=10)

bottom_frame = tk.Frame(window, bg="#D4FC79")  # Light green
bottom_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Full language names
languages = [
    'Auto Detect', 'Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', 
    'Catalan', 'Cebuano', 'Chinese', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Esperanto', 'Estonian', 'Finnish', 'French', 'Galician', 'Georgian', 
    'German', 'Greek', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian',
    'Japanese', 'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Kinyarwanda', 'Korean', 'Kurdish', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian', 'Luxembourgish',
    'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Myanmar', 'Nepali', 'Norwegian', 'Nyanja', 'Odia', 'Pashto', 
    'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Romanian', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian', 'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 
    'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tagalog', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Turkish', 'Turkmen', 'Ukrainian', 
    'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu'
]

# Language code mapping for translation
lang_code_map = {
    'Auto Detect': 'auto', 'Afrikaans': 'af', 'Albanian': 'sq', 'Amharic': 'am', 'Arabic': 'ar', 'Armenian': 'hy', 'Azerbaijani': 'az', 'Basque': 'eu', 'Belarusian': 'be',
    'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Catalan': 'ca', 'Cebuano': 'ceb', 'Chinese': 'zh', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da',
    'Dutch': 'nl', 'English': 'en', 'Esperanto': 'eo', 'Estonian': 'et', 'Finnish': 'fi', 'French': 'fr', 'Galician': 'gl', 'Georgian': 'ka', 'German': 'de',
    'Greek': 'el', 'Gujarati': 'gu', 'Haitian Creole': 'ht', 'Hausa': 'ha', 'Hawaiian': 'haw', 'Hebrew': 'he', 'Hindi': 'hi', 'Hungarian': 'hu', 'Icelandic': 'is',
    'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it', 'Japanese': 'ja', 'Javanese': 'jv', 'Kannada': 'kn', 'Kazakh': 'kk', 'Khmer': 'km',
    'Kinyarwanda': 'rw', 'Korean': 'ko', 'Kurdish': 'ku', 'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv', 'Lithuanian': 'lt', 'Luxembourgish': 'lb',
    'Macedonian': 'mk', 'Malagasy': 'mg', 'Malay': 'ms', 'Malayalam': 'ml', 'Maltese': 'mt', 'Maori': 'mi', 'Marathi': 'mr', 'Mongolian': 'mn', 'Myanmar': 'my',
    'Nepali': 'ne', 'Norwegian': 'no', 'Nyanja': 'ny', 'Odia': 'or', 'Pashto': 'ps', 'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 'Punjabi': 'pa',
    'Romanian': 'ro', 'Russian': 'ru', 'Samoan': 'sm', 'Scots Gaelic': 'gd', 'Serbian': 'sr', 'Sesotho': 'st', 'Shona': 'sn', 'Sindhi': 'sd', 'Sinhala': 'si',
    'Slovak': 'sk', 'Slovenian': 'sl', 'Somali': 'so', 'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw', 'Swedish': 'sv', 'Tagalog': 'tl', 'Tajik': 'tg',
    'Tamil': 'ta', 'Tatar': 'tt', 'Telugu': 'te', 'Thai': 'th', 'Turkish': 'tr', 'Turkmen': 'tk', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uyghur': 'ug', 'Uzbek': 'uz',
    'Vietnamese': 'vi', 'Welsh': 'cy', 'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu'
}

# Widgets in the top frame
tk.Label(top_frame, text="Enter Text:", font=("Arial", 14, "bold"), bg="#FFDEE9").pack(side="left", padx=10, pady=10)

# Text Input Area
text_input = tk.Text(top_frame, height=5, width=50, font=("Arial", 12), relief="solid")
text_input.pack(side="left", padx=10, pady=10)

# Source Language Dropdown
src_lang_combo = ttk.Combobox(top_frame, values=languages, state="readonly", font=("Arial", 12), width=20)
src_lang_combo.set("Auto Detect")
src_lang_combo.pack(side="left", padx=10, pady=10)

# Target Language Dropdown
target_lang_combo = ttk.Combobox(top_frame, values=languages, state="readonly", font=("Arial", 12), width=20)
target_lang_combo.set("English")
target_lang_combo.pack(side="left", padx=10, pady=10)

# Translate Button
tk.Button(top_frame, text="Translate", font=("Arial", 12), command=translate_text, bg="#00C0FF").pack(side="left", padx=10, pady=10)

# Result Output Area
result_output = tk.Text(middle_frame, height=10, width=80, font=("Arial", 12), relief="solid", bg="#E3FFDC")
result_output.pack(pady=10)

# History Listbox
history_listbox = tk.Listbox(bottom_frame, font=("Arial", 12), height=10)
history_listbox.pack(fill="both", expand=True, padx=10, pady=10)

# Buttons for clearing
tk.Button(bottom_frame, text="Clear Text", font=("Arial", 12), command=clear_text, bg="#FF9999").pack(side="left", padx=10, pady=10)
tk.Button(bottom_frame, text="Clear History", font=("Arial", 12), command=clear_history, bg="#FF9999").pack(side="right", padx=10, pady=10)

# Run the application
window.mainloop()
