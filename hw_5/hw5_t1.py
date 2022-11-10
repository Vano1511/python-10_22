print('Здравствуйте, я удалю все слова, содержащие "абв" в файле task1_input.txt')
print( 'и помещу результат в файл task1_output.txt')
file = open('task1_input.txt')
content = file.readlines()
file.close()
find_text = 'абв'
file = open('task1_output.txt', 'w')
for line in content:
    for word in line.split():
        if find_text not in word:
            file.write(word+' ')
    file.write('\n')
file.close()
print('программа завершена успешно')