print("Введите последовательность чисел через пробел:")
array = input()
print("Введите любое целое число:")
num = input()

while True:
    list_1 = list(map(int, array.split(' '))) #удаляем пробелы, приводим к целым числам
    num_1 = int(num) #приводим введенное пользователем число к целому

#алгоритм двоичного поиска
def binary_search(list_1, num_1, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if list_1[middle] == num_1:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif num_1 < list_1[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(list_1, num_1, left, middle - 1)
    else:  # иначе в правой
        return binary_search(list_1, num_1, middle + 1, right)

print(binary_search(list_1, num_1, 0, 99))