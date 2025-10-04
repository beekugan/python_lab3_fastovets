import asyncio
from mypackage import module1

async def demo():
    print("=== gtrans4 demo (mypackage.module1) ===\n")
    # Переклад
    t = await module1.TransLate("Добрий день", "uk", "en")
    print("TransLate:", t)

    # Визначення мови
    ld_all = await module1.LangDetect("Hello world", "all")
    print("LangDetect (all):", ld_all)
    ld_lang = await module1.LangDetect("Hello world", "lang")
    print("LangDetect (lang):", ld_lang)

    # CodeLang
    code_to_name = await module1.CodeLang("en")
    print("CodeLang('en') ->", code_to_name)
    name_to_code = await module1.CodeLang("ukrainian")
    print("CodeLang('ukrainian') ->", name_to_code)

    # LanguageList
    print("\nLanguageList:")
    await module1.LanguageList(out="screen", text="Привіт")

if __name__ == "__main__":
    asyncio.run(demo())
