def x_to_bin(num):
    result = ''   # результат будет строкой
    if num == 0:
        return 0
    while num >= 1:
        result = str(num % 2) + result
        num //= 2
    if num < 0:
        result = '1'    # первую пишем единицу и не меняем ее
        for el in x_to_bin(-num):
            if el == '1':
                result += '0'
            if el == '0':
                result += '1'
        counter = len(result) - 1
        res = [el for el in result]   # перевожу в список, чтобы было проще работать
        x = 1                # надо двоично прибавить один
        while counter >= 1 and x:
            if res[counter] == '0':
                res[counter] = '1'
                x = 0
            else:
                res[counter] = '0'
                counter -= 1
        result = ''.join(res)      # обратно перевожу в строку
    return result

number = int(input('введите целое число и я переведу его в двоичную систему счисления: '))

print(f' число {number} в двоичной системе имеет вид: {x_to_bin(number)} ')