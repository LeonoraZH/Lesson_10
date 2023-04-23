"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""

word1 = 'разработка'
word2 = 'сокет'
word3 = 'декоратор'

print(f"Тип переменной word1: {type(word1)}, содержание: {word1}")
print(f"Тип переменной word2: {type(word2)}, содержание: {word2}")
print(f"Тип переменной word3: {type(word3)}, содержание: {word3}")

word1_unicode = [ord(letter) for letter in word1]
word2_unicode = [ord(letter) for letter in word2]
word3_unicode = [ord(letter) for letter in word3]

word1_unicode = ''.join([f"\\u{ord(letter):04x}" for letter in word1])
word2_unicode = ''.join([f"\\u{ord(letter):04x}" for letter in word2])
word3_unicode = ''.join([f"\\u{ord(letter):04x}" for letter in word3])

print(f"Тип переменной word1_unicode: {type(word1_unicode)}, содержание: {word1_unicode}")
print(f"Тип переменной word2_unicode: {type(word2_unicode)}, содержание: {word2_unicode}")
print(f"Тип переменной word3_unicode: {type(word3_unicode)}, содержание: {word3_unicode}")

