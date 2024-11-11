# # Shallow copy & Deepcopy;

# import copy
#
# a = [1, 2, 3, [2, 3, 4]]
# c = a.copy()
# b = copy.deepcopy(a)
# b[3].append(3)
# print(a)
# c[3].append(9)
# print(a)

# # Dictionary methods;

"""
hash table -> dict;
CRUD - Create, Read, Update, Delete;
"""

# d = {"name": "Nosir", "age": 24}
# d_ = dict(name="Nosir", age=24)
# d__ = dict([("name", "Nosir"), ("age", 24)])
#
# print(d, d_, d__, )

# d["baho"] = [10, 8, 9, 7, 10]
# print(d["baho"])

# --- --- --- --- --- #

# movie = {
#     "Sulaymon": "Kayi",
#     "Ertugrul": "Kayi",
#     "Usmon": "Kayi",
# }

# adding_new_data = {
#     "Bola": "Edabali qizi",
#     "Malhun": "Bey qizi",
# }
#
# adding_second_data = [
#     ["Askar", "Nom"],
#     ("Alp", "Nom"),
# ]
#
# movie.update(adding_new_data)
# movie.update(adding_second_data)
# print(movie)

# # Delete a key:value pair that doesn't exist in the dictionary: KeyError
# del movie["NoKey"]
# print(movie)

# movie["SomeThing"] = 0
# print(movie)
# movie.popitem()
# a = movie.pop("Sulaymon")
# print(movie)
# print(a)

# search = movie.get("Osman", False)
# print(search)

# print(movie.setdefault("Osman", "Turkish"))
# print(movie)

# print(list(movie.items()))
# print(list(movie.keys()))
# print(list(movie.values()))

# from collections import Counter
#
# count = Counter(movie.values())
# print(count)

# # Set & its methods

#                                        Vazifalar                                         #

"""
1. stringlar ro'yxatini oladigan va ularni uzunligi bo'yicha guruhlaydigan str_counter(strs) funksiya yozing, 
bunda kalitlar string uzunliklari va qiymatlar shu uzunlikdagi string keladi.
M: str_counter(["shaftoli", "olma", "nok" ]) -> {8:"shaftoli", 4: "olma", 3: "nok"}
"""

# def str_counter(strs):
#     d = {}
#     for i in strs:
#         d[i] = len(i)
#     return d
#
#
# print(str_counter(["shaftoli", "olma", "nok"]))

"""
2. Bir xil uzunlikdagi ikkita listni parametr sifatida oladigan, kalitlar birinchi ro'yxatning 
elementlari va qiymatlar ikkinchi ro'yxatning mos keladigan elementlari bo'lgan dict qaytaradigan merge_list(l1,l2) funksiya yarating.
M: list_1 = ["a", "b", "c"] 
   list_2 = [1, 2, 3]  
   merge_list(list_1 ,list_2)  -> {"a":1, "b":2, "c":3}
"""

# def merge_list(l1: list, l2: list):
#     l = {}
#     for i in range(len(l1)):
#         l.update({l1[i]: l2[i]})
#     return l
#
#
# list_1 = ["a", "b", "c"]
# list_2 = [1, 2, 3]
# print(merge_list(list_1, list_2))

"""
3. Foydalanuvchilarga kontaktlarni qo‘shish, yangilash, o‘chirish va qidirish 
imkonini beruvchi dict ga asoslangan telefon kontaktlar ro'yxati dasturini yarating
M: contacts = {"Nodir":"+998918602711", "Laziz":"+998908002534"}
"""
# from Game.contacting import dast
#
# dast()

"""
4. Raqamlar ro'yxatini oladigan va ro'yxatdagi har bir raqamning takrorlanish sonini o'z ichiga 
olgan dict qaytaradigan counter_dict(nums) nomli funksiya yozing.
M: counter_dict([2,1,1,1]) -> {2:1, 1:3} Chunki listda 1ta 2 va 3ta 1bor.
"""

# def counter_dict(nums: list):
#     d = {}
#     for i in nums:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
#     return d
#
#
# print(counter_dict([3, 2, 3, 4, 2, 3, 2, 3, 2, 4, 2, ]))

"""
5. Ballar dict ni(kalit = talaba nomi, qiymat = ball) parametr sifatida oladigan va eng yaxshi ikkita
o'quvchining ismlari ro'yxatini qaytaradigan max_ball_students(talabalar) funksiya yozing.
max_ball_students({{"Akmal":64, "Tohir":55, "Nodir":76, "Zafar":80 }}) -> {"Zafar":80, "Nodir":76}
"""


# def max_ball_students(talabalar):
#     talabalar_sorted = []
#     for key, value in talabalar.items():
#         talabalar_sorted.append((key, value))
#
#     talabalar_sorted.sort(key=lambda x: x[1], reverse=True)
#     return {talabalar_sorted[0][0]: talabalar_sorted[0][1], talabalar_sorted[1][0]: talabalar_sorted[1][1]}
#
#
# d = {"Akmal": 64, "Tohir": 55, "Nodir": 76, "Zafar": 80}
# print(max_ball_students(d))
