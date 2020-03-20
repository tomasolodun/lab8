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
            while (j < len(s1)) and i < (len(s) - len(s1)):
                j = 0
                i += 1  # Кількість зсувів,позиція
                while j < len(s1) and s1[j] == s[i + j]:
                    j += 1
            if j == len(s1):
                print(
                    f'Підрядок знайдено на позиції {i},за {i + 1} зсувів')  # позиція починається з 0,кількість
                # зсувів з 1(тут)
            else:
                print('Підрядок не знайдено')
            print('Хочете повторити дії? Введіть так ,якщо ні - інше')
            answer = input('')
            if answer == 'так':
                continue
            else:
                break

