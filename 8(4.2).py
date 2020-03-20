sclad_list = []  # Кінцевий саисок товарів складу
while True:
    while True:
        try:
            n = int(input("Скільки товарів додамо в склад?"))  # Перевірка на правильність входження
        except ValueError:
            print('Введіть чиса!')
            break
        for j in range(n):
            list = []  # Пустий список,в який користувач додаватиме товари за заданими значеннями
            for i in range(1):
                list.append(('Найменування', input('Введіть найменування')))  # Додаємо в список наступні елементи
                list.append(('Виробник', input('Введіть виробника')))  # Стільки разів,скільки задав користувач
                try:
                    list.append(('Кількість товару ', int(input('Введите кількість товару '))))
                    list.append(('Ціна', int(input('Введить ціну'))))
                    # Також перевірка на правильність входження(число/слово)
                except ValueError:
                    print('Введіть числа! ')
                break
            sclad_list.append(list)
        for i in range(len(sclad_list) - 1):  # Бульбашкове сортування за 'Найменуванням' ,за алфавітом
            for j in range(len(sclad_list) - 1):
                if sclad_list[i][0] > sclad_list[i + 1][0]:
                    sclad_list[i], sclad_list[i + 1] = sclad_list[i + 1], sclad_list[i]
        print(sclad_list)
        print('Хочете повторити дії? Введіть так ,якщо ні - інше')
        answer = input('')
        if answer == 'так':
            continue
        else:
            break
