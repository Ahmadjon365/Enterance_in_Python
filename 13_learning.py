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

"""
2. Kiritilgan belgilardan  parollar generatsiya qiladigan generator yarating. 
     M: input: abs        output: abs→asb→sab→sba→bas→bsa
"""

"""
3. Cheksiz Fibonachi sonlarini generatsiya qiladigan generator yarating.
     M: 0→1→1→2→3→5→8→13→21→ …
"""

"""
4. listdagi elementlarni n tadan guruhlanganda barcha mavjud guruhlarni generatsiya qiladigan generator yarating. 
      M: my_list = [1,2,3,4] n=2. Natija: 1,2 → 1,3  → 1,4 →  2,3 → 2,4 → 3,4
"""
