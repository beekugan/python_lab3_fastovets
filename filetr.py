import os
import json
import importlib
from langdetect import detect
from colorama import Fore, Style


base_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(base_dir, "config.json")

try:
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
except Exception as e:
    print(f"Помилка читання конфігураційного файлу: {e}")
    exit()

text_filename = config.get("text_filename", "input_text.txt")
target_lang = config.get("target_lang", "en")
module_name = config.get("module", "module3") 
output_type = config.get("output", "screen")
max_chars = config.get("max_chars", 1000)
max_words = config.get("max_words", 200)
max_sentences = config.get("max_sentences", 20)

try:
    translator_module = importlib.import_module(module_name)
except Exception as e:
    print(f"Помилка імпорту модуля {module_name}: {e}")
    exit()

text_path = os.path.join(base_dir, text_filename)
if not os.path.exists(text_path):
    print(f"Помилка: файл '{text_filename}' не знайдено.")
    exit()


try:
    with open(text_path, "r", encoding="utf-8") as f:
        text = f.read()
except Exception as e:
    print(f"Помилка зчитування файлу: {e}")
    exit()


sentences = text.replace("!", ".").replace("?", ".").split(".")
words = text.split()
chars = len(text)


print(Fore.YELLOW + "=== Інформація про вхідний файл ===" + Style.RESET_ALL)
print(f"Назва файлу: {text_filename}")
print(f"Розмір файлу: {os.path.getsize(text_path)} байт")
print(f"Кількість символів: {chars}")
print(f"Кількість слів: {len(words)}")
print(f"Кількість речень: {len(sentences)}")

try:
    text_lang = detect(text)
    print(f"Мова тексту: {text_lang}")
except Exception as e:
    text_lang = "unknown"
    print(f"Не вдалося визначити мову: {e}")


sentences_to_read = min(max_sentences, len(sentences))
words_to_read = min(max_words, len(words))
chars_to_read = min(max_chars, chars)


short_text = text[:chars_to_read]


try:
    translated_text = translator_module.TransLate(short_text, text_lang, target_lang)
except Exception as e:
    print(f"Помилка перекладу: {e}")
    exit()


print(Fore.GREEN + "\n=== Результат ===" + Style.RESET_ALL)
print(f"Модуль перекладу: {module_name}")
print(f"Мова перекладу: {target_lang}")

if output_type == "screen":
    print("\nПерекладений текст:\n")
    print(Fore.CYAN + translated_text + Style.RESET_ALL)
else:
    output_filename = f"{os.path.splitext(text_filename)[0]}_{target_lang}.txt"
    output_path = os.path.join(base_dir, output_filename)
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(translated_text)
        print(Fore.GREEN + f"Ok. Переклад збережено у файл: {output_filename}" + Style.RESET_ALL)
    except Exception as e:
        print(f"Помилка запису результату: {e}")
