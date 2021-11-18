"""
Даны два списка чисел. Посчитайте, сколько (уникальных) чисел содержится одновременно как в первом списке,
так и во втором.
- Примечание. Эту задачу на Питоне можно решить в одну строчку.

(Задача решается с применением множеств)
"""

from random import randint

# ВАРИАНТ №1
lst1 = [randint(1, 20) for i in range(10)]
lst2 = [randint(1, 20) for i in range(10)]
# Преобразуем list в set, объеденяем их "|" и выводим их длину. Получаем кол. элементов
print(lst1)
print(lst2)
print(len((set(lst1)) | set(lst2)))

# ВАРИАНТ №2
"""
lst1 = [1, 2, 2, 3, 5, 6]
lst2 = [1, 7, 2, 8, 9, 10]

print(lst1)
print(lst2)
print(len(set(lst1) | set(lst2)))
"""

# ВАРИАНТ №3
# print(len(set(input("Enter any numbers: ").split()) | set(input("Enter any numbers: ").split())))
