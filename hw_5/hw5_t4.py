print('Здравствуйте, я зашифрую текст в файле task4_input.txt с помощью RLE алгоритма')
print( 'и помещу результат в файл task4_output.txt')
file = open('task4_input.txt')
content = file.read()
file.close()
counter = 0                   # создаем счетчик, определяем стартовую букву и пустой итоговый текст
start_char = content[0]
final_text = ''
for char in content:
    if char == start_char:
        counter += 1
    else:
        final_text += start_char + str(counter)   #добавляем результат подсчета и обнуляем счетчик
        counter = 1               #один, потому что мы уже на первом новом символе
        start_char = char
final_text += start_char + str(counter) # дописываем подсчет последнего символа
file = open('task4_output.txt', 'w')
file.write(final_text)
file.close()
print('программа завершена успешно')