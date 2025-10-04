from googletrans import Translator, LANGUAGES

translator = Translator()


async def TransLate(text: str, scr: str, dest: str) -> str:
    """
    Перекладає текст з мови scr на мову dest
    """
    try:
        result = await translator.translate(text, src=scr, dest=dest)
        return result.text
    except Exception as e:
        return f"Помилка: {e}"


async def LangDetect(text: str, set: str = "all") -> str:
    """
    Визначає мову і коефіцієнт довіри
    """
    try:
        detect = await translator.detect(text)
        if set == "lang":
            return detect.lang
        elif set == "confidence":
            return str(detect.confidence)
        else:
            return f"Мова: {detect.lang}, Довіра: {detect.confidence}"
    except Exception as e:
        return f"Помилка: {e}"


async def CodeLang(lang: str) -> str:
    """
    Перетворює код мови у назву і навпаки
    """
    try:
        lang = lang.lower()
        if lang in LANGUAGES:  # введено код (наприклад 'en')
            return LANGUAGES[lang]
        elif lang in LANGUAGES.values():  # введено назву (наприклад 'english')
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
                    tr_text = (await translator.translate(text, dest=code)).text
                    row += tr_text
                except:
                    row += "-"
            lines.append(row)

        if out == "screen":
            for line in lines:
                print(line)
        elif out == "file":
            with open("languages.txt", "w", encoding="utf-8") as f:
                for line in lines:
                    f.write(line + "\n")
        else:
            return "Помилка: невірний параметр out"

        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"
