
s = True
while s:
    try:
        string = input("Введите числа через пробел:")
        list_of_strings = string.split()
        list_of_numbers = list(map(int, list_of_strings))
        num = int(input('введите число:'))
    except ValueError as e:
        print('ввели неправильно')
    else:
        s = False


def sort(l):

    for i in range(len(l)):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


def binary_search(l, num, left, right):
    if l[right] < num or l[left] >= num:
        print('R- ', right)
        print('not ok')
        return False

    else:

        if left > right:
            return False

        middle = (right + left) // 2
        if l[middle - 1] < num and l[middle] >= num:
            return middle
        elif l[middle - 1] >= num:
            right = middle - 1
            return binary_search(l, num, left, right)
        else:
            left = middle + 1
            return binary_search(l, num, left, right)


sort(list_of_numbers)
result = binary_search(list_of_numbers, num, 0, len(list_of_numbers) - 1)
if not result:
    print('условие не выполняется')
else:
    print('индексы ', result - 1, 'и', result)

