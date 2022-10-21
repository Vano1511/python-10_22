numbers = [int(el) for el in input('введите последовательнось чисел через пробел и я найду произведения пар чисел: ').split()]
start = 0               # присвоим маркерам первый и последний индексы
end = len(numbers) - 1
result = []             # итоговый пустой список
while end >= start:
    result.append(numbers[start] * numbers[end])
    start += 1
    end -= 1

print(f'вот список произведенеий элементов на зеркальных позициях вашего списка: {result}')