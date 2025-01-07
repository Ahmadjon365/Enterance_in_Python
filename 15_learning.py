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
# def time_teller(func):
#     def sett(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         elapsed_time = time.time() - start_time
#         print(f"{func.__name__} --- {elapsed_time:.3f} soniyada bajarildi.")
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
# @time_teller
# def lot_func():
#     i = 0
#     for _ in range(10 ** 7):
#         i += _
#         print(i)
#     print("Funksiya to'xtadi")
#
#
# lot_func()
# example_function()

"""
4. Funksiya necha marta chaqirilganini sanovchi dekorator yozing
"""

# def count_calls(func):
#     def sett(*args, **kwargs):
#         sett.calls += 1
#         return func(*args, **kwargs)
#
#     sett.calls = 0
#     return sett
#
#
# @count_calls
# def example_function():
#     return True
#
#
# # Test
# example_function()
# example_function()
# example_function()
# print(example_function.calls)
