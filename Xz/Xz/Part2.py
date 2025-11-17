text = input("Введите текст: ")
chars = len(text)
words = text.split()
word_count = len(words)
vowels = "aeiouаеёиоуыэюя"
consonants = "bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ"
vowel_count = 0
consonant_count = 0
longest_word = max(words, key=len) if words else ""
longest = len(longest_word)
for letter in text.lower():
    if letter in vowels:
        vowel_count += 1
    elif letter in consonants:
        consonant_count += 1
print("Символов (включая пробелы):", chars)
print("Слов:", word_count)
print("Гласных:", vowel_count)
print("Согласных:", consonant_count)
print("Самое длинное слово:", longest_word, f"(длина: {longest})")