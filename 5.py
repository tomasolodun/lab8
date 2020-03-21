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
        i = 0
        count = 0 # Введемо лічильник для підрахунку кулькості операцій.
        while i < l and masiv[i] != x:  # Додаємо лінійний пошук
            i += 1
            count += 2
        print('Кількість порівнянь', count )  # Кількість порівнянь
        if i == l:
            print('Елемент не знайдено')
        else:
            print(f'На позиции {i+1} знайдено Ваш елемент {x}')
        # Робота з рандомними числами
        masiv1 = np.zeros(20, dtype=int)
        for i in range(20):
            masiv1[i] = random.randint(-5, 10)
        print(masiv1)
        l1 = len(masiv1)
        i = 2
        count2 = 0 # Введемо лічильник для підрахунку кулькості операцій.
        while i < l and masiv1[i] != x:  # Лінійний пошук
            i += 1
            count2 += 2
        print('Кількість порівнянь', count2)
        if i == l1:
            print('Елемент не знайдено')
        else:
            print(f'На позиции {i+1} найден Ваш елемент {x}')
    print('Хочете повторити дії? Введіть так ,якщо ні - інше')
    answer = input('')
    if answer == 'так':
        continue
    else:
        break
