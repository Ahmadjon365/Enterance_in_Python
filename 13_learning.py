# Iterator & Generator

the_l = [1, 2, 3]
the_iter_l = iter(the_l)

# print(type(the_l))
# print(type(the_iter_l))

# print(next(the_iter_l))
# print(next(the_iter_l))
# print(next(the_iter_l))
# print(next(the_iter_l))  # Agar bunda ma'lumotlar yetarli bo'lmasa: "StopIteration" hatosi yuzaga chiqadi.

# while True:
#     try:
#         print(next(the_iter_l))
#     except StopIteration:  # Hatolik yuzaga chiqganida to'xtatadi.
#         break

# def try_gen(y):
#     n = y
#     n += 1
#     print("Amaldagi qo'shimcha")
#     yield n
#
#     n **= 2
#     print("Amaldagi orttirish")
#     yield n
#
#
# result = try_gen(6)
#
# print(next(result))
# print(next(result))

# def duble_qaytar(min, max):
#     for i in range(min, max + 1):
#         yield i ** 2
#
#
# result = duble_qaytar(1, 5)
#
# for item in result:
#     print(item)

# my_list_com = [num for num in range(1, 5 + 1)]
# print(my_list_com)
#
# my_generator = (num for num in range(1, 5 + 1))
# print(my_generator)
#
# for i in my_generator:
#     print(i)

#                                        Vazifalar                                         #

"""
1. Har safar chaqirilganda keyingi tub sonni generatsiya qiladigan generator yarating. 
    M: 2 →3→5→7→11→13
"""


def prime_generator():
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


# Foydalanish
g = prime_generator()
for _ in range(10):  # 10 ta tub son generatsiya qiladi
    print(next(g), end=" → ")

"""
2. Kiritilgan belgilardan  parollar generatsiya qiladigan generator yarating. 
     M: input: abs        output: abs→asb→sab→sba→bas→bsa
"""


def password_generator(chars):
    def permute(data, start, end):
        if start == end:
            yield ''.join(data)
        else:
            for i in range(start, end):
                data[start], data[i] = data[i], data[start]
                yield from permute(data, start + 1, end)
                data[start], data[i] = data[i], data[start]  # Backtrack

    yield from permute(list(chars), 0, len(chars))


# Foydalanish
chars = "abs"
gen = password_generator(chars)
for password in gen:
    print(password, end=" → ")

"""
3. Cheksiz Fibonachi sonlarini generatsiya qiladigan generator yarating.
     M: 0→1→1→2→3→5→8→13→21→ …
"""


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Foydalanish
gen = fibonacci_generator()
for _ in range(10):  # 10 ta Fibonacci soni generatsiya qiladi
    print(next(gen), end=" → ")

"""
4. listdagi elementlarni n tadan guruhlanganda barcha mavjud guruhlarni generatsiya qiladigan generator yarating. 
      M: my_list = [1,2,3,4] n=2. Natija: 1,2 → 1,3  → 1,4 →  2,3 → 2,4 → 3,4
"""


def group_generator(my_list, n):
    def combine(data, start, end, r, current):
        if r == 0:
            yield tuple(current)
            return
        for i in range(start, end):
            current.append(data[i])
            yield from combine(data, i + 1, end, r - 1, current)
            current.pop()  # Backtrack

    yield from combine(my_list, 0, len(my_list), n, [])


# Foydalanish
my_list = [1, 2, 3, 4]
n = 2
gen = group_generator(my_list, n)
for group in gen:
    print(group, end=" → ")
