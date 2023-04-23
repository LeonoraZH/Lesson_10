"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ['разработка', 'администрирование', 'protocol', 'standard']

for word in words:
    word_bytes = word.encode('utf-8')
    print(f"{word} в байтовом представлении: {word_bytes}")

    word_decoded = word_bytes.decode('utf-8')
    print(f"{word_bytes} обратно преобразовано в строковое представление: {word_decoded}\n")
