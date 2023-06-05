from translate import Translator

def translate_text(text, target_language):
    translator = Translator(to_lang=target_language)
    try:
        translated = translator.translate(text)
        return translated
    except Exception as e:
        print(f"Translation error: {e}")
        return None

# Example usage
text_to_translate = str(input("Enter the text"))
target_language = "es"  # Translate to Spanish
translated_text = translate_text(text_to_translate, target_language)

if translated_text is not None:
    print(f"Translated text: {translated_text}")
else:
    print("Translation failed.")
