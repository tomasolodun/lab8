# виведіть на екран транспоновану матрицю 3*3 (початкова матриця задана користувачем)
import numpy as np
while True:
    while True:
        try:
            n, m = int(input('Введіть кількість рядків: ')), \
                   int(input('Введіть кількість стовпчиків: '))
            A = np.zeros((n, m), dtype=int)  # Ініціалізуємо матрицю нулями,як початкову
            if n == 3 and m == 3:  # Перевірка розмірності 3 на 3.
                for i in range(n):  # Створюємо послідовність циклу рядків та стовпчиків
                    for j in range(m):
                        A[i, j] = int(input(f' [{i+1}, {j+1}]: '))
                print('Ваша матриця: ', A)
            break
        except ValueError:  # Перевірка на правильність вводу(числа)
            print('Введіть числа! ')
    T = np.zeros((n, m), dtype=int)  # Ініціалізуємо нульову матрицю,пізніше стане транспортованою Т
    for i in range(m):  # цикл для присвоєння введеної матриці майбутній транспортованій
        for j in range(n):
            T[i, j] = A[j, i]  # Перестановкою індексів ми отримаємо транспоновану матрицю.
    print('Транспонована матриця: ', T)
    print('Хочете повторити дії? Введіть yes чи інше')
    answer = input('')
    if answer == 'yes':
        continue
    else:
        break