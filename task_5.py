"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

def ping(host):
    result = subprocess.run(['ping', '-c', '5', host], stdout=subprocess.PIPE)
    return result.stdout

yandex_ping = ping('yandex.ru')
print(yandex_ping)

yandex_encoding = chardet.detect(yandex_ping)['encoding']

yandex_ping_str = yandex_ping.decode(yandex_encoding)
print(yandex_ping_str)

youtube_ping = ping('youtube.com')
print(youtube_ping)

youtube_encoding = chardet.detect(youtube_ping)['encoding']

youtube_ping_str = youtube_ping.decode(youtube_encoding)
print(youtube_ping_str)
