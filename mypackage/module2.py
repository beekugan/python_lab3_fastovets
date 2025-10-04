import sys
import asyncio
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory

# Перевірка версії Python
if sys.version_info >= (3, 13):
    print("Увага: Python 3.13 або новіший, можливі проблеми з бібліотекою deep_translator")

DetectorFactory.seed = 0

# Отримуємо словник підтримуваних мов
translator = GoogleTranslator(source='auto', target='en')  # приклад
LANGUAGES = translator.get_supported_languages(as_dict=True)


async def TransLate(text: str, scr: str, dest: str) -> str:
    """
    Перекладає текст з мови scr на мову dest
    """
    try:
        translator = GoogleTranslator(source=scr, target=dest)
        result = translator.translate(text)
        return result
    except Exception as e:
        return f"Помилка: {e}"


async def LangDetect(text: str, set: str = "all") -> str:
    """
    Визначає мову тексту (коефіцієнт довіри недоступний у deep_translator).
    """
    try:
        lang = detect(text)  # визначає мову
        if set == "lang" or set == "all":
            return f"Мова: {lang}"
        elif set == "confidence":
            return "Коефіцієнт довіри недоступний у deep_translator"
        else:
            return f"Мова: {lang}"
    except Exception as e:
        return f"Помилка: {e}"


async def CodeLang(lang: str) -> str:
    """
    Перетворює код мови у назву і навпаки
    """
    try:
        lang = lang.lower()
        if lang in LANGUAGES:  # якщо ввели код (en)
            return LANGUAGES[lang]
        elif lang in LANGUAGES.values():  # якщо ввели назву (english)
            for code, name in LANGUAGES.items():
                if name == lang:
                    return code
        return "Помилка: мова не знайдена"
    except Exception as e:
        return f"Помилка: {e}"


async def LanguageList(out: str = "screen", text: str = None) -> str:
    """
    Виводить таблицю мов і кодів, а також переклад text на цю мову
    """
    try:
        lines = []
        header = f"{'Код':<10}{'Мова':<20}"
        if text:
            header += "Переклад"
        lines.append(header)

        for code, name in LANGUAGES.items():
            row = f"{code:<10}{name:<20}"
            if text:
                try:
                    tr_text = GoogleTranslator(source="auto", target=code).translate(text)
                    row += tr_text
                except:
                    row += "-"
            lines.append(row)

        if out == "screen":
            for line in lines:
                print(line)
        elif out == "file":
            with open("languages_deep.txt", "w", encoding="utf-8") as f:
                for line in lines:
                    f.write(line + "\n")
        else:
            return "Помилка: невірний параметр out"

        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"
