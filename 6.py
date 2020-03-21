while True:
    while True:
        try:
            x = int(input('Введіть елемент пошуку'))
        except ValueError:
            print('Введіть числа!! ')
            break

        import numpy as np
        import random

        masiv = np.array(range(1, 15))  # Створюємо масив для перевірки правильності вводу.
        print(masiv)
        R = len(masiv) - 1  # Кінець масиву
        L, count, k = 0, 0, 0,  # Початок масиву,лічильник,змінна для позиції числа
        flag = False
        while L <= R and not flag:
            k = (L + R) // 2  # Якщо ввести 9,після першої операції к=6,після другої 10 і тд
            count += 2  # лічильник операцій
            if masiv[k] == x:
                flag = True
            elif masiv[k] < x:
                count += 1
                L = k + 1
            else:
                count += 1
                R = k - 1
        if not flag:
            print('Елемент не знайдено')
        else:
            print(f'Елемент знайдено на позиції {k} за {count} порівнянь')
        # Рандомні числа
        masiv1 = np.zeros(20, dtype=int)
        for i in range(20):
            masiv1[i] = random.randint(-10, 10)
        print(masiv1)
        R1 = len(masiv1) - 1  # Кінець масиву
        L1, count1, k1 = 0, 0, 0,  # Початок масиву,лічильник,змінна для позиції числа
        flag1 = False
        while L1 <= R1 and not flag1:
            k1 = (L1 + R1) // 2
            count1 += 2  # Лічильник для підрахунку кількості операцій
            if masiv1[k1] == x:
                flag1 = True
            elif masiv1[k1] < x:
                L1 = k1 + 1
                count1 += 1
            else:
                R1 = k1 - 1
                count1 += 1
        if not flag1:
            print('Елемент не знайдено')
        else:
            print(f'Елемент знайдено на позиції {k1} за {count1} порівнянь')

    print('Хочете повторити дії? Введіть так ,якщо ні - інше')
    answer = input('')
    if answer == 'так':
        continue
    else:
        break
