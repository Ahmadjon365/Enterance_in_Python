""" Decorators """

# def say_hello(name):
#     return f"Hello {name}"
#
#
# def be_awesome(name):
#     return f"Yo {name}, together we're the awesomest!"
#
#
# def greet_bob(greeter_func):
#     return greeter_func("Bob")


# print(greet_bob(say_hello))
# print(greet_bob(be_awesome))
#
# # index
# print(say_hello(greet_bob))

#                                        Vazifalar                                         #

"""
1) Funksiya qaytargan stringni katta harfga o'tkazib beradigan dekorator yarating
"""

# def big_alpha(func):
#     def sett(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return str(result).upper()
#
#     return sett
#
#
# @big_alpha
# def ret_sentence(sentence):
#     return sentence
#
#
# c = ret_sentence("You, what's up?")
# print(c)

"""
2. Fuksiya qaytaradigan stringni teskaraisiga aylantirib(reverse) beradigan dekorator yarating.
"""

# def reversing_txt(func):
#     def sett(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return str(result)[::-1]
#
#     return sett
#
#
# @reversing_txt
# def rev_sen(sentence):
#     return sentence
#
#
# z = rev_sen("?uoy era woH")
# print(z)

"""
3. Funksiya ishlashi uchun qancha vaqt ketganini hisoblab beradigan dekorator yozing
"""

# import time
#
#
# def start_timer():
#     return time.time()
#
#
# def end_timer(start_time):
#     return time.time() - start_time
#
#
# def time_teller(func):
#     def sett(*args, **kwargs):
#         start_time = start_timer()
#         result = func(*args, **kwargs)
#         elapsed_time = end_timer(start_time)
#         print(f"{func.__name__} --- {elapsed_time:.4f} soniyada bajarildi.")
#         return result
#
#     return sett
#
#
# @time_teller
# def example_function():
#     for _ in range(10 ** 7):
#         pass
#     print("Funksiya to'xtadi")
#
#
# example_function()

"""
4. Funksiya necha marta chaqirilganini sanovchi dekorator yozing
"""


# def count_calls(func):
#     def sett(*args, **kwargs):
#         sett.calls += 1
#         print(f"Funksiya {sett.calls} marta chaqirildi.")
#         return func(*args, **kwargs)
#
#     sett.calls = 0
#     return sett
#
#
# @count_calls
# def example_function():
#     print("Funksiya bajarildi")
#
#
# # Test
# example_function()
# example_function()
# example_function()
