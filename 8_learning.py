# Functions; dict methods;

# def sanoq():
#     for _ in range(40):
#         if _ % 2 == 0 and _ % 3 == 0:
#             print(_)
#         else:
#             continue
#
#
# sanoq()

# def big_sales(dictionary: dict):
#     return max(dictionary, key=dictionary.get)
#
#
# my_d = {
#     "January": 34230,
#     "February": 63431,
#     "March": 35842,
#     "December": 38932
# }
#
# print(big_sales(my_d))

"""                                        Vazifalar                                         """

"""
1. "user_data" funksiyasini elon qilasizlar.
Funksiyani 3 ta parametri bor (first_name, last_name, age).
Input orqalik ism, familiya va yoshni kiritamiz.
va bu bu qiymatlarni "user_data" funksiyasini chaqirib argumentlariga beramiz.
"user_data" funksiyasi bu (first_name, last_name, age) o'zgaruvchilarni qiymatini

  Ism: Alisher
  Familiya: Olimov
  Yosh: 27

ko'rinishiga print qilib bersin.
"""

# def user_data(First_name: str, Last_name: str, Age: int):
#     return f"Ismi: {First_name},\nFamiliyasi: {Last_name},\nYoshi: {Age}"
#
#
# data_user = {"Name": "Ahmadjon", "Surname": "Abdulfotih", "Age": 16}
# print(user_data(data_user["Name"], data_user["Surname"], data_user["Age"]))

"""
2. "find_max" funksiyasini elon qilasizlar.
Funksiyani 3 ta parametri bor (a, b, c).
Input orqalik 3 ta son kiritamiz.
va bu sonlarni "find_max" funksiyasi chaqirib argumentlariga beramiz.
"find_max" funksiyasini bu (a, b, c) o'zgaruvchilardan eng kattasini
topib print qiladi.

  Eng katta son - A = 10
  yoki 
  Eng katta son - A va B = 10
  yoki
  Eng katta son - A va B va C = 10
"""

# def find_max(a, b, c):
#     max_num = max(a, b, c)
#     max_nums = []
#
#     if a == max_num:
#         max_nums.append("A")
#     if b == max_num:
#         max_nums.append("B")
#     if c == max_num:
#         max_nums.append("C")
#
#     return f"Eng katta son - {' va '.join(max_nums)} = {max_num}"
#
#
# print(find_max(10, 6, 10))

"""
3. "find_letter_count" funksiyasini elon qilasizlar.
Funksiyani 2 ta parametri bor (word, letter).
Input orqalik so'z kiritamiz, keyin esa shu so'zda qidirmoqchi bolgan so'zimizni kiritamiz.
va bu qiymatlarni "find_letter_count" funksiyasini chaqirib argumentlariga beramiz.
"find_letter_count" funksiyasi bu (word, letter) o'garuvchilardan foydalanib
"word" da "letter" nechi martda qatnashganini print qilsin.

  "Programing" so'zida "r" dan 2 ta.
"""

# def find_letter_count(word: str, letter: str):
#     return f"{word} so'zida {letter} dan {word.count(letter)} ta bor"
#
#
# print(find_letter_count("Arra", 'r'))

"""  
4. "list_sum" funksiyasi elon qilasizlar.
Funksiyani 1 ta pametrni bor (myList).
"myList" funksiyasini chaqirib unda argumentini berasizlar.
uni ichida esa myList elementlarini yig'indisini print qilasizlar.

  Listning elementlar yig'indisi = 32
"""

# def list_sum(l: list):
#     return f"List elementlari yig'indisi: {sum(l)}"
#
#
# print(list_sum([23, 43, 21, 54, 34]))

"""
5. daraja(a, b) - bu funksiya a ni b darajasini print qilsin.
"""

# def daraja(a, b):
#     return f"{a} ning {b} darajasi: {a ** b}"
#
#
# print(daraja(4, 7))

"""
6. daraja4(a, b, c, d) - bu funksiya a ni b, c va d chi darajasini print qilsin.
"""

# def daraja4(a, b, c, d):
#     return f"{a} ning {b} darajasi: {a ** b}\n{c} ning {d} darajasi: {c ** d}"
#
#
# print(daraja4(4, 7, 5, 3))


"""
7. digit_count_and_sum(word) - bu funksiya "word" ni ichidagi raqamni aniqlab ularni yig'indisini va nechtaligini print qilsin.
"""

# def digit_count_and_sum(word: str):
#     a = []
#
#     for i in word:
#         if i.isdigit():
#             a.append(int(i))
#
#     return f"Raqamlar yig'indisi: {sum(a)}, raqamlar nechtaligi: {len(a)}"
#
#
# print(digit_count_and_sum("Ahmadjonning tel raqami: +998770333308"))

"""
8. add_right(a, b) - bu funksiya a sonini o'ng tomoniga b sonini birlashtirib qoysin va print qilsin.
"""

# def add_right(a: int or float, b: int or float):
#     print(int(str(a) + str(b)))
#
#
# add_right(5, 71)

"""
9. add_left(a, b) - bu funksiya a sonini chap tomoniga b sonini birlashtirib qoysin va print qilsin.
"""

# def add_left(a: int or float, b: int or float):
#     print(int(str(b) + str(a)))
#
#
# add_left(71, 5)

"""
10. work_with_list(a) - bu funksiya a listdan eng kichik sonni topib list elementlariga ko'paytirib qiymatini o'zgartiradi va listni print qilsin.
"""

# def work_with_list(a: list):
#     mini = min(a)
#     original_a = a[:]
#     a.clear()
#     for i in original_a: a.append(i * mini)
#     return a
#
#
# print(work_with_list([32, 3, 23, 43, 3, 34, 32, 43454, 554, 656, 7878, 34, 4]))

"""
11. big_sales(sales) funksiyasini yarating. 
sales bu dictionary:
{
  "yanvar": 12000,
  "mart": 6000,
  "aprel": 15000,
  "sentabr": 9000,
  "dekabr": 10000,
}

qaysi oyda eng ko'p sotuv bolgan bo'lganini return qilsin.
"""

# def big_sales(sales: dict):
#     return max(sales, key=sales.get)
#
#
# my_d = {
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
# }
#
# print(big_sales(my_d))

"""
12. min_max(numbers, max_num, min_num) max_num numbers ichigagi eng katta sonmi yoki yoqmi shuni aniqlang, 
min_num numbers ichigagi eng kichik sonmi yoki yoqmi shuni aniqlang
"""

# def min_max(numbers: list or tuple or set, max_num, min_num):
#     max_n = max(numbers)
#     min_n = min(numbers)
#
#     max_message = "Maksimal raqam to'g'ri yozilgan!" if max_n == max_num else f"Maksimal raqam bu emas, balki: {max_n} bo'ladi"
#     min_message = "Minimal raqam to'g'ri yozilgan!" if min_n == min_num else f"Minimal raqam bu emas, balki: {min_n} bo'ladi"
#
#     return f"{max_message}. {min_message}"
#
#
# print(min_max([12, 43, 65, 89, 5, 67, 32, 84, 34], 84, 5))

"""
13. expensiveProduct(products) - funksiyadagi products - list.
[{'a': 'b', 'c': 123},
 {'a': 'b', 'c': 123},
 {'a': 'b', 'c': 123},
 {'a': 'b', 'c': 123}]
Eng qimmat telefon nomini print qilib bersin bu funksiya.
"""

# def expensive_product(products):
#     max_product = products[0]
#
#     for product in products:
#         if product["price"] > max_product["price"]:
#             max_product = product
#     return max_product
#
#
# my_pros = [{
#     "name": "Iphone X",
#     "price": 600
# }, {
#     "name": "Iphone 12",
#     "price": 1500
# }, {
#     "name": "Samsung Note 9",
#     "price": 800
# }, {
#     "name": "Samsung S10",
#     "price": 1100
# }]
#
# print(expensive_product(my_pros))
