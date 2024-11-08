# Loops of for & while

# # for:
# cars = ["Lamborghini", "Ferrari", "Porsche", "Chevrolet", "Opel", "Nissan", "BMW", "Mercedes-benz"]
# count = 0
#
# for car in cars:
#     count += 1
#     c = "Supper car: " + car
#     print(str(count) + ")", c)

# # Factorial:
# num = int(input("Son kiriting: "))
# ans = 1
#
# for i in range(1, num + 1):
#     ans *= i
# print(ans)

# # Tub son - o'ziga va 1 ga qoldiqsiz bo'linuvchi sondir:
# num = int(input("Son kirting: "))
# last = int(num ** 0.5)
#
# for i in range(2, last + 1):
#     if i % 2 == 0 and i != 2:
#         continue
#     if num % i == 0:
#         print("🚫")
#         break
# else:
#     print("✅")

#                                        Vazifalar                                         #

""" Foydalanuvchidan qiziqishlari so'ralsin.

Agar kitob yoki kutubxona qiziqishlari orasida bo'lsa, qanday kitoblar yoqishi so'ralsin.
    agar detektiv so'zini ishlatsa, shaytanat kitobi haqidagi fikri so'ralsin.
    agar diniy kitoblarga qiziqsa "Hadis va Hayot" kitoblar to'plamini sovg'a qilamiz deyilsin.

Agar sport so'zi qiziqishlari orasida bo'lsa, qaysi sport turiga qiziqishi so'ralsin,
   agar futbol sport turlari orasida bo'lsa, qaysi komandani yoqtirishi so'ralsin.
        agar real yoki barsa komandasini yozsa, el-classicoga chipta sovg'a qilamiz deyilsin """

# ans = input("Qiziqishlaringizni kiriting: ").title()
#
# if "Kitob" in ans or "Kutubxona" in ans:
#     i = input("Qanday kitoblarga qiziqasiz: ").title()
#     if i.find("Detaktiv") >= 0:
#         a = input("Shaytanat kitobi haqidagi fikringizni qoldiring: ")
#         print(f"Sizning fikringiz quyidagicha:\n{a}")
#     elif i.find("Diniy") >= 0:
#         print("Sizga 'Hadis va Hayot' kitoblarini sovg'a etamiz!")
#     else:
#         print(f"Siz quyidagi kitoblarga qiziqar ekansiz:\n{i}")
# elif "Sport" in ans:
#     i = input("Qanday sport turiga qiziqasiz: ").title()
#     if i.find("Futbol") >= 0:
#         a = input("Qaysi jamoani yoqtirasiz: ").title()
#         if "Real" or "Barsa" in a:
#             print("Sizga el-classico ga chipta sovg'a etamiz!")
#         else:
#             print(f"Siz quyidagi jamoalarga qiziqar ekansiz: {a}")
#     else:
#         print(f"Siz quyidagi sport turiga qiziqar ekansiz:\n{i}")
# else:
#     print(f"Siz quyidagi narsalarga qiziqar ekansiz:\n{', '.join(ans.split(', '))}")

# # Top.1
#
# pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
#
# for i in pochtalar:
#     if '@' not in i or  '.' not in i:
#         print(f"{i} email hato kiritilgan")
#     else:
#         continue

# # Top.2

# users_pass = ["password123", "Qwerty!", "admin", "StrongPass1!", "asdfghjkl", "00012348765"]
#
# for i in users_pass:
#     if len(i) < 8:
#         print(f"Qisqa parol! {i}")
#     elif i.isalpha() or i.isnumeric():
#         print(f"Kuchsiz parol! {i}")
#     else:
#         print(f"Kuchli parol! {i}")

# # Top.3

# temp = [20, 22, 19, 23, 21, 31, -3]
#
# for i in temp:
#     if i < 0:
#         print(f"Sovuq {i}")
#     elif i <= 20 > 0:
#         print(f"Salqin {i}")
#     elif i <= 30 > 21:
#         print(f"Iliq {i}")
#     elif i >= 31:
#         print(f"Issiq {i}")

# # Top.4

# meals = ["Osh", "Shashlik", "Manti", "Lag'mon"]
#
# inp = input("Buyurtmani kiriting: ").title()
#
# if inp in meals:
#     print("Buyurtma qabul qilindi!")
# else:
#     print("Kechirasiz, bunday taom yo'q")

# # Top.5

# ages = [16, 21, 17, 30, 25]
#
# for i in ages:
#     if i >= 18:
#         print("Xush kelibsiz!")
#     else:
#         print("Yosh chegarasi yetmagan!")

# # Top.6

# xabarlar = ["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
#
# for i in xabarlar:
#     if i == "Batareya past":
#         print("Telefoningizni quvvatlang!")
#     else:
#         print(f"Yangi habar: {i}")

# # Top.7

# fayllar = ["kitob.jpg", "ko_jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
#
# musiqalar = []
# rasmlar = []
#
# for i in fayllar:
#     if '.jpg' in i:
#         musiqalar.append(i)
#     elif '.mp3' in i:
#         rasmlar.append(i)
#     else:
#         continue
#
# print("Musiqalar: " + ', '.join(musiqalar))
# print("Rasmlar: " + ', '.join(rasmlar))
