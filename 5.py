while True:
    while True:
        try:
            x = int(input('Введіть елемент пошуку'))
        except ValueError:
            print('Введіть числа!! ')
            break
        import numpy as np
        import random

        masiv = np.array(range(1, 11))  # Створюємо масив для перевірки правильності вводу.
        print(masiv)
        l = len(masiv)
        count = 0  # Введемо лічильник для підрахунку кулькості операцій.
        while count < l and masiv[count] != x:  # Додаємо лінійний пошук
            count += 1
        print('Кількість порівнянь', count + 1)  # Кількість порівнянь,починається з 0,тому додамо 1
        if count == l:
            print('Елемент не знайдено')
        else:
            print(f'На позиции {count} знайдено Ваш елемент {x}')
        # Робота з рандомними числами
        masiv1 = np.zeros(20, dtype=int)
        for i in range(20):
            masiv1[i] = random.randint(-5, 10)
        print(masiv1)
        l1 = len(masiv1)
        count2 = 0
        while count2 < l and masiv1[count2] != x:  # Лінійний пошук
            count2 += 1
        print('Кількість порівнянь', count2 + 1)
        if count2 == l1:
            print('Елемент не знайдено')
        else:
            print(f'На позиции {count2} найден Ваш елемент {x}')
    print('Хочете повторити дії? Введіть так ,якщо ні - інше')
    answer = input('')
    if answer == 'так':
        continue
    else:
        break
