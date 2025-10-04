import sys
from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs, DetectorFactory
from colorama import Fore, Style


DetectorFactory.seed = 0


def TransLate(text: str, scr: str, dest: str) -> str:
  
    try:
        if not text:
            return "Помилка: текст не задано."

        if scr == "auto":
            translator = GoogleTranslator(source="auto", target=dest)
        else:
            translator = GoogleTranslator(source=scr, target=dest)

        translated = translator.translate(text)
        return translated
    except Exception as e:
        return f"Помилка перекладу: {e}"


def LangDetect(text: str, set: str = "all") -> str:
  
    try:
        if not text:
            return "Помилка: текст не задано."

        detected = detect_langs(text)[0]
        lang_code = detected.lang
        confidence = detected.prob

        if set == "lang":
            return lang_code
        elif set == "confidence":
            return f"{confidence:.2f}"
        else:
            return f"Мова: {lang_code}, коефіцієнт довіри: {confidence:.2f}"
    except Exception as e:
        return f"Помилка визначення мови: {e}"


def CodeLang(lang: str) -> str:
 
    try:
        languages_dict = GoogleTranslator().get_supported_languages(as_dict=True)
        lang_lower = lang.lower()

        # Якщо ввели назву мови
        if lang_lower in languages_dict:
            return languages_dict[lang_lower]

        # Якщо ввели код мови
        inv_dict = {v: k for k, v in languages_dict.items()}
        if lang_lower in inv_dict:
            return inv_dict[lang_lower]

        return "Помилка: мову не знайдено."
    except Exception as e:
        return f"Помилка отримання коду мови: {e}"


def LanguageList(out: str = "screen", text: str = "") -> str:
    
    try:
        languages_dict = GoogleTranslator().get_supported_languages(as_dict=True)
        lines = []
        header = f"{'Мова':<25} | {'Код':<10}"
        if text:
            header += f" | {'Переклад'}"
        lines.append(header)
        lines.append("-" * 70)

        for lang_name, code in languages_dict.items():
            line = f"{lang_name:<25} | {code:<10}"
            if text:
                try:
                    translated = GoogleTranslator(source="auto", target=code).translate(text)
                    line += f" | {translated}"
                except Exception:
                    line += " | [Помилка перекладу]"
            lines.append(line)

        output = "\n".join(lines)

        if out == "file":
            with open("languages.txt", "w", encoding="utf-8") as f:
                f.write(output)
            return "Ok (дані записано у файл languages.txt)"
        else:
            print(Fore.CYAN + output + Style.RESET_ALL)
            return "Ok"

    except Exception as e:
        return f"Помилка створення списку мов: {e}"


