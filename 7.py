while True:
    while True:
        try:
            s = 'Босий хлопець сіно косить, роса росить ноги босі.'
            print(s)
            s1 = input('Введіть підрядок')
            s1 = int(s1)  # перевірка на ввід слів,а не чисел
            print('Введіть слова!! ')
            break
        except ValueError:
            i = -1  # Індекси рядка
            j = 0  # Індекси підрядка
            count = 0
            while (j < len(s1)) and i < (len(s) - len(s1)):
                j = 0
                i += 1
                count += 2
                while j < len(s1) and s1[j] == s[i + j]:
                    j += 1
                    count += 2
            if j == len(s1):
                print(
                    f'Підрядок знайдено на позиції {i+1},за {count} порівнянь')
            else:
                print('Підрядок не знайдено')
            print('Хочете повторити дії? Введіть так ,якщо ні - інше')
            answer = input('')
            if answer == 'так':
                continue
            else:
                break
