import asyncio
from mypackage import module2

async def demo():
    print("=== gtrans3 demo (mypackage.module2) ===\n")
    # Переклад
    t = await module2.TransLate("Добрий день", "uk", "en")
    print("TransLate:", t)

    # Визначення мови (deep_translator зазвичай не повертає confidence)
    ld = await module2.LangDetect("Hello world", "all")
    print("LangDetect:", ld)

    # CodeLang
    code_to_name = await module2.CodeLang("en")
    print("CodeLang('en') ->", code_to_name)
    name_to_code = await module2.CodeLang("ukrainian")
    print("CodeLang('ukrainian') ->", name_to_code)

    # LanguageList (screen)
    print("\nLanguageList:")
    await module2.LanguageList(out="screen", text="Привіт")

if __name__ == "__main__":
    asyncio.run(demo())

