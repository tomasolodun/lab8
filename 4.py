# у матриці 4*4, що задана користувачем замініть всі від’ємні елементи на 0.
import numpy as np

while True:
    while True:
        try:
            n, m = int(input('Введіть кількість рядків: ')), \
                   int(input('Введіть кількість стовпчиків: '))
        except ValueError:
            print('Input numbers!! ')
            break
        A = np.zeros((n, m), dtype=int)  # Ініціалізуємо матрицю нулями.
        for i in range(n):  # Доступ до рядків і стовпчиків
            for j in range(m):
                if n == 4 and m == 4:  # Перевірка на правильність розмірності матриці 4 на 4
                    A[i, j] = int(input(f' [{i + 1}, {j + 1}]: '))
                    print(A)
                    if A[i, j] < 0:  # Якщо елемент матриці від'ємний - замін ана 0
                        A[i, j] = 0
        print(A)  # Наша матриця уже із заміною від'ємних чисел на число 0.
        if n != 4 or m != 4:  # Випадок, коли користувач ввів матрицю не 4 на 4.
            print('Введіть матрицю 4х4!')
    print('Хочете повторити дії? Введіть yes чи інше')
    answer = input('')
    if answer == 'yes':
        continue
    else:
        break
