def fibo(num, list=[0, 1]):
    for number in range(2, num+1):
        list.append(list[number-1] + list[number-2])
    return list

qantity = int(input('введите необходимое количество элементов и я вам выдам последовательности фиббоначи и негафиббоначи: '))
list_fibo = fibo(qantity)
prelist_negafibo = list_fibo[1:]
list_negafibo = [prelist_negafibo[i]*((-1)**i) for i in range(len(prelist_negafibo))]

result = list_negafibo[::-1] + list_fibo

print(f'вот итоговый список: {result} ')