print("first commit")
print("Робота на сьогодні закінчена")
print("Кухня готова, Гіт працює!")

# class MyClass:
#     def __init__(self):
#         self.name = "Alice"
#
#     def greet(self):
#         print("Hello, " + self.name)
#
# obj = MyClass()
# print(dir(obj))  # Выводит список атрибутов и методов объекта 'obj'
# print(dir())

# print(hash("hello"))  # Возвращает хеш-значение строки "hello"
# print(hash(42))       # Возвращает хеш-значение числа 42
# print(hash((1, 2, 3)))  # Возвращает хеш-значение кортежа (1, 2, 3)

# number = 12
# string = 'hello'
# my_list = [12, 'hello']
# my_set = (12, 'hello')
#
# print(id(number))
# print(id(string))
# print(id(my_list))
# print(id(my_set))
#
# print(hash(number))
# print(hash(string))
# print(hash(my_list))
# print(hash(my_set))
#
# print(dir(number))
# print(dir(string))
# print(dir(my_list))
# print(dir(my_set))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # Вывод: [2, 4, 6, 8, 10]

# words = ["banana", "apple", "cherry", "date"]
# sorted_words = sorted(words, key=lambda x: len(x))
# print(sorted_words)  # Вывод: ['date', 'apple', 'banana', 'cherry']

# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])
# print(pairs)  # Вывод: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# chisla = [1, 2, 3]
# kvadrat_chisla = list(map(lambda x: x ** 2, chisla))
# print(kvadrat_chisla)

# def make_filter(threshold):
#     # threshold — це "поріг", який замикання запам'ятає
#     def filter_func(value):
#         # Повертає True, якщо значення більше за поріг
#         return value > threshold
#
#     return filter_func
#
#
# # Набір даних для тесту (наприклад, VDI знахідок або розміри плитки)
# data = [10, 25, 45, 60, 75, 90, 100]
#
# # 1. Створюємо фільтр для "дрібних" значень (пропускає все, що більше 30)
# filter_medium = make_filter(30)
#
# # 2. Створюємо фільтр для "великих" значень (пропускає все, що більше 80)
# filter_high = make_filter(80)
#
# # Використовуємо фільтри
# print(f"Початковий список: {data}")
#
# # Відфільтруємо список за допомогою вбудованої функції filter()
# result_medium = list(filter(filter_medium, data))
# result_high = list(filter(filter_high, data))
#
# print(f"Значення більше 30: {result_medium}")
# print(f"Значення більше 80: {result_high}")

# def large_range(n):
#     for i in range(n):
#         yield i
#
# for value in large_range(1000000):
#     # Обрабатываем значения по одному
#     print(value)
