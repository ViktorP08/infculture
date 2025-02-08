# TODO заменить значение пропущенного элемента средним арифметическим

# Исходный список с пропущенным элементом:
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Вычисление среднего значения
av = sum(num for num in numbers if num is not None) / (len(numbers))

print("Измененный список:", [av if num is None else num for num in numbers])
