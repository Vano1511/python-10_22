from math import pi
file = open('pi.txt')
content = file.read()
file.close()

elements = int(input(f'введите число  N, чтобы задать точность до {len(content) - 2} знаков после запятой: '))

print(f'вот число пи с заданной вами точностью: {content[:elements+2]}')
