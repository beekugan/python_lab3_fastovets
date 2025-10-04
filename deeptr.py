from mypackage import module3


def main():
    # 1. Демонстрація TransLate
    text_to_translate = "Доброго дня! Як ви сьогодні?"
    translated = module3.TransLate(text_to_translate, "auto", "en")
    print(f"Оригінал: {text_to_translate}")
    print(f"Англійською: {translated}\n")

    # 2. Демонстрація LangDetect
    sample_text = "Bonjour tout le monde"
    lang_info = module3.LangDetect(sample_text, "all")
    print(f"Текст: {sample_text}")
    print(f"Результат: {lang_info}\n")

    # 3. Демонстрація CodeLang
    print(f"Код для 'ukrainian': {module3.CodeLang('ukrainian')}")
    print(f"Назва для 'en': {module3.CodeLang('en')}\n")

    # 4. Демонстрація LanguageList (вивід на екран)
    result_screen = module3.LanguageList("screen", "Привіт світ")
    print(f"Результат: {result_screen}\n")




if __name__ == "__main__":
    main()
