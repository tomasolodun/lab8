#виведіть на екран елементи лінійного масиву (заданий користувачем) у \
#зворотному порядку
import numpy as np #Імпортуємо бібліотеку numpy
while True:
    while True:
        try:
            A = np.array(list(map(int, input('Введіть лінійний масив: ').split())))[::-1]
            print(A) # Розвертаємо введений користувачем масив за допомогою зрізу [::-1]
            break
        except ValueError: #Перевіряємо правильність вводу(числа)
            print('Введіть послідовність чисел!')
    print('Хочете повторити дії? Введіть yes чи інше')
    answer = input('')
    if answer == 'yes':
        continue
    else:
        break