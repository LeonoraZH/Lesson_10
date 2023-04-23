"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""
words = ['class', 'function', 'method']

# Создаем пустой список, куда будем добавлять байтовые строки
bytes_list = []

# Проходимся по каждому слову в списке и преобразуем его в байтовую строку
for word in words:
    byte_word = b''
    for letter in word:
        byte_word += bytes(letter, encoding='utf-8')
    bytes_list.append(byte_word)

# Выводим тип, содержание и длину каждой переменной
for i, byte_word in enumerate(bytes_list):
    print(f"Тип переменной words[{i}]: {type(byte_word)}, содержание: {byte_word}, длина: {len(byte_word)}")
