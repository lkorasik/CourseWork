def max_boring_prefix_length():
    n = int(input())
    a = list(map(int, input().split()))

    # перебираем все префиксы массива и ищем максимальный скучный префикс
    max_len = 0
    for i in range(1, n + 1):
        # создаем словарь, содержащий количество вхождений каждого числа в префиксе
        count = {}
        for j in range(i):
            if a[j] in count:
                count[a[j]] += 1
            else:
                count[a[j]] = 1
        # проверяем, является ли префикс скучным
        remove = False
        freq = list(count.values())
        for j in range(len(freq) - 1):
            if freq[j] != freq[j + 1]:
                if remove:
                    # если уже был удален один элемент, то этот префикс не скучный
                    break
                elif freq[j] > freq[j + 1]:
                    # пытаемся удалить элемент с чаще встречающимся значением
                    if freq[j] - freq[j + 1] == 1:
                        remove = True
                    else:
                        break
                else:
                    if freq[j + 1] - freq[j] == 1:
                        remove = True
                    else:
                        break
        else:
            # если префикс скучный, запоминаем его длину
            max_len = i
    print(max_len)

if __name__ == "__main__":
    max_boring_prefix_length()
