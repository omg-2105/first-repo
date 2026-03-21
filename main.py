# print("first commit")
# print("Робота на сьогодні закінчена")
# print("Кухня готова, Гіт працює!")

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

# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# fib = fibonacci()
# for _ in range(10):
#     print(next(fib))

# def natural_numbers():
#     n = 1
#     while True:
#         yield n
#         n += 1
#
# naturals = natural_numbers()
# for _ in range(10):
#     print(next(naturals))

# # 1. Визначаємо декоратор
# def log_decorator(func):
#     def wrapper():
#         print("--- Повідомлення ПЕРЕД викликом функції ---")
#         func()  # Виклик самої функції greet()
#         print("--- Повідомлення ПІСЛЯ виклику функції ---")
#     return wrapper
#
# # 2. Застосовуємо декоратор до функції greet
# @log_decorator
# def greet():
#     print("Вітаю! З Днем народження та вдалими знахідками!")
#
# # 3. Викликаємо декоровану функцію
# greet()

# def signal_booster(original_function):
#     def wrapper():
#         print("Підсилюємо сигнал антеною за 5500 грн...")
#         original_function() # Викликаємо твою функцію
#         print("З'єднання стабільне!")
#     return wrapper
#
# @signal_booster
# def open_python_lesson():
#     print("Відкриваємо лекцію на JavaRush")
#
# # Тепер викликаємо:
# open_python_lesson()

# def logger(func):
#     def wrapper():
#         print("Запит відправлено на вишку...")
#         func()
#         print("Завантаження завершено!")
#     return wrapper
#
# @logger
# def download_lesson():
#     print("...йде завантаження Python лекції...")
#
# # Виклич функцію нижче:
# download_lesson()

# import platform
#
# print("Operating System:", platform.system())
# print("Node Name:", platform.node())
# print("OS Release:", platform.release())
# print("OS Version:", platform.version())
# print("Machine:", platform.machine())
# print("Processor:", platform.processor())
# print("Architecture:", platform.architecture())
# print("Python Version:", platform.python_version())
# print("Python Compiler:", platform.python_compiler())

# def maximun_reproduction(years_to_flood, children_per_woman, generation_gap):
#     population = 2  # Адам і Єва
#     year = 0
#
#     # Кожні 80 років (середній час до появи онуків) рахуємо приріст
#     while year < years_to_flood:
#         # Тільки половина населення (жінки) народжує дітей
#         females = population / 2
#         new_children = females * children_per_woman
#
#         population += new_children
#         year += generation_gap
#
#         # Виводимо проміжні результати кожні 400 років
#         if year % 400 == 0:
#             print(f"Рік {year}: {int(population):,}")
#
#     return int(population)
#
#
# # Налаштування: 1656 років, 50 дітей на жінку, покоління кожні 80 років
# total_people = maximun_reproduction(1656, 50, 80)
# print(f"\nЗагальна кількість людей до Потопу: {total_people:,}")

# def realistic_biblical_population(years_limit):
#     population = 2
#     # Список, де ми будемо зберігати вік груп людей (спрощено)
#     # Кожні 20 років народжується нова група
#     people_groups = {0: 2}  # вік: кількість людей
#
#     for year in range(20, years_limit + 20, 20):
#         new_borns = 0
#         current_groups = list(people_groups.items())
#
#         for age, count in current_groups:
#             # Якщо вік від 60 до 450 — вони народжують (по 1 дитині на пару за 20 років)
#             if 60 <= age <= 450:
#                 new_borns += count / 2 * 2  # Кожна пара дає 2 дітей за 20 років
#
#             # Старіння: додаємо 20 років
#             people_groups[age + 20] = people_groups.pop(age)
#
#             # Смертність: якщо старше 930 років — видаляємо з розрахунку
#             if age + 20 > 930:
#                 people_groups.pop(age + 20)
#
#         people_groups[0] = new_borns
#         population = sum(people_groups.values())
#
#         if year % 200 == 0 or year == years_limit:
#             print(f"Рік {year:4}: {int(population):,}")
#
#     return int(population)
#
#
#
#
# # Запускаємо до 1656 року
# all_people = realistic_biblical_population(1656)
#
# earth_area = 149_000_000
# population_per_square_km = all_people // earth_area
# print(population_per_square_km) # 2998
#
# population_per_square_ga = population_per_square_km / 100
# rounded_pop_p_s_ga = round(population_per_square_ga)
# print(rounded_pop_p_s_ga)

# quantity_apricots = 5
# water = 100
# water_per_apricot = water / quantity_apricots
#
# for i in range(1, quantity_apricots + 1):
#     print(f"Apricot №{i} gived {water_per_apricot} liters of water.")

# quantity_apricots = 5
# water = 100
# water_per_apricot = water / quantity_apricots
#
# print(f"\nПлан на сьогодні: дати кожному дереву по {water_per_apricot} л. води.\n")
#
# # Починаємо з 1, закінчуємо на кількості + 1
# for i in range(1, quantity_apricots + 1):
#     print(f"Дерево №{i} полито. Використано {water_per_apricot} літрів. ✅")
#
# print("\nРоботу завершено! Сад напоєний.")

# total_harvest = 0
# current_yield = 10
# quantity_trees = 6
#
# for i in range(1, quantity_trees + 1):
#     # 1. Додаємо врожай поточного дерева до загального кошика
#     total_harvest = total_harvest + current_yield
#
#     print(f"Дерево №{i} дало {current_yield} кг. У кошику вже {total_harvest} кг.")
#
#     # 2. Збільшуємо врожай для НАСТУПНОГО дерева на 5 кг
#     current_yield = current_yield + 5
#
# print(f"\nФінальний результат: Ти зібрав {total_harvest} кг абрикосів! 🎉")

# curr_power_percents = 100
# fall_power = 5
# for i in range(1, 7):
#     curr_power_percents = curr_power_percents - fall_power
#     print(f"First hour{i} - {curr_power_percents}")
#     fall_power += 2
#
# print(curr_power_percents)
#
# curr_power_percents = 100
# fall_power = 5  # скільки втрачаємо зараз
#
# for i in range(1, 7):  # тепер точно 6 годин
#     curr_power_percents = curr_power_percents - fall_power
#     print(f"Hour {i}: Battery - {curr_power_percents}% (lost {fall_power}%)")
#     # Ось тут магія: збільшуємо ВТРАТУ на майбутнє
#     fall_power = fall_power + 2
#
# print(f"\nFinal charge: {curr_power_percents}%")

# class Library: # клас Бібліотека
#     books = ['a', 'b', 'c']  # список книг в бібліотеці
#     @classmethod # декоратор який показує що робити в бібліотеці
#     def add_book(cls, book):  # функція незрозуміло чому сіельес?
#         cls.books.append(book)  # додає книгу
#     def display_books(self):  # функція незрозуміло чому селф?
#         print(self.books)  # виводить список книг у бібліотеці
# info = Library()   # присвоюємо змінній інфо клас Бібліотека?
# info.add_book('d')   # тут ясно додаємо книгу д
# info.display_books()  # звертаємось до функції яка виводить список книг

class Orchard:
    total_trees = 0

    @classmethod
    def add_tree(cls, number):
        cls.total_trees += number
    def display_status(self):
        print(f"У саду зараз: {self.total_trees} дерев")
info = Orchard()
info.add_tree(10)
info.display_status()

# class Orchard:
#     total_trees = 0
#
#     @classmethod
#     def add_tree(cls, numbers_range):
#         # Проходимо циклом по кожному числу в range
#         for n in numbers_range:
#             cls.total_trees += 1  # Додаємо по одному дереву за кожен крок
#
#     def display_status(self):
#         print(f"У саду зараз: {self.total_trees} дерев")
#
#
# info = Orchard()
# info.add_tree(range(1, 11))  # Тепер це спрацює!
# info.display_status()

trees = 0

for i in range(7):
    i += 1
    print(f"Tree #{i} planted")
    trees = trees + 1
print(trees)

trees_count = 0

# Кажемо range почати з 1 і зупинитися перед 8 (тобто на 7)
for i in range(1, 8):
    print(f"Tree #{i} planted")
    trees_count += 1

print(f"Total trees: {trees_count}")