# Closures: ya'ni Biror funksiya ichidagi funksiyani to'g'ridan to'g'ri chaqirish;

# global
# a = [4, 5, 6]


# def f1():  # O'zgarmas
#     print(a)
#
#
# def f2():  # O'zgartira oluvchi
#     global a
#     a.append(7)
#     return a
#
#
# print(f2())
# print(a)


# local

# def f3():
#     a = 4
#     print(a)
#
#
# def f4():
#     a = 4
#
#     def f1():  # inner function
#         print(a)  # nonlocal


# def f1():
# 	a = 4
# 	def f2(): #inner function
# 		print(a) #nonlocal


# a = 4
#
#
# def f1():
#     global a
#     a = 5
#     print(a)  # local -> 5
#
#
# print(a)  # global -> 4


# def f(x):
#     def g(y):
#         return y
#
#     return g
#
#
# a = 5
# b = 1
#
# h = f(a)
# natija = h(b)
# print(natija)  # Output is 1
#
# # yoki
# natija = f(a)(b)
# print(natija)  # Output is 1


# def f(x):
#     def g(y):
#         return y
#
#     return g(y)
#
#
# a = 5
# b = 1
# h = f(a)  # Xatolik beradi: NameError: name 'y' is not defined


# def f(x):
#     def g(y):
#         def h(z):
#             return z
#
#         return h
#
#     return g
#
#
# a = 5
# b = 2
# c = 1
# f(a)(b)(c)  # Output is 1


# # Agar biz nonlocal o’zgaruvchidan foydalansakchi:

# def f(x):
#     z = 2
#
#     def g(y):
#         return z * x + y
#
#     return g
#
#
# a = 5
# b = 1
# h = f(a)
# print(h(b))  # Output is 11


"""“closure” atamasi “close” so’zidan olingan bo’lib, , u free (nonlocal) variable larni ushlab qolgan holda
open term ni yopish natijasida vujudga kelgani uchun shunday nomlangan"""

# def f(x):
#     z = 2
#
#     def g(y):  # g hali closure emas
#         return z * x + y
#
#     return g
#
#
# a = 5
# b = 1
# h = f(a)  # endi h closure bo'ldi, qaysiki g ga teng bo'lgan.
# print(h(b))  # Output is 11


# # Python free variable larni saqlab turadi.

# print(h.__code__.co_freevars) # ('x', 'z')
# # ularning qiymatlari esa:
# print(h.__closure__[0].cell_contents)  # 5
# print(h.__closure__[1].cell_contents)  # 2


# # Bu closure emas:
#
# def f(x):
#     z = 2
#
#     def g(y):
#         return y
#
#     return g
#
#
# a = 5
# b = 1
# h = f(a)
# print(h(b))  # Output is 1
# print(h.__code__.co_freevars)  # Output is ()


# def f(x):
#     def g(y): #closure
#         def h(z): #closure
#             return x * y * z
#
#         return h
#
#     return g
#
#
# a = 5
# b = 2
# c = 1
# f(a)(b)(c)  # Output is 10


# # Closure sifatida biz lambda funksiya ham ishlata olamiz:

# def f(x):
#     z = 2
#     return lambda y: z * x + y
#
#
# a = 5
# b = 1
# f(a)(b)  # Output is 11


"""Composer - 2ta funksiyani qo’shib beruvchi funksiya.
Composer yaratamiz:
"""


# def compose(g, f):
#     def h(*args, **kwargs):  # closure funksiya
#         return g(f(*args, **kwargs))
#
#     return h
#
#
# # Vazifani bajaramiz:
# km_to_m = lambda x: x * 1000
# m_to_sm = lambda x: x * 100
#
# km_to_sm = compose(m_to_sm, km_to_m)
# print(km_to_sm(12))  # Output 1 200 000
