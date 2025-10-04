import asyncio
from mypackage.module1 import TransLate, LangDetect, CodeLang, LanguageList
from mypackage.module2 import TransLate, LangDetect, CodeLang, LanguageList

async def main():
    print(await TransLate("Добрий день", "uk", "en"))
    print(await LangDetect("Hello world"))
    print(await CodeLang("english"))
    print(await CodeLang("uk"))
    await LanguageList("screen", "Привіт")  # таблиця мов із перекладом

async def main():
    # 1. Переклад
    print(await TransLate("Добрий день", "uk", "en"))

    # 2. Визначення мови
    print(await LangDetect("Hello world"))

    # 3. Код → назва
    print(await CodeLang("en"))

    # 4. Назва → код
    print(await CodeLang("ukrainian"))

    # 5. Таблиця мов (вивід на екран з перекладом прикладу)
    await LanguageList(out="screen", text="Привіт")



if __name__ == "__main__":
    asyncio.run(main())
