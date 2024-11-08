from random import randint

# Loop while; random; Games;

# i = 1
#
# while i <= 5:
#     print(i)
#     i += 1

# while True:
#     name = input("Ism kiriting: ")
#     if name == "Ahmadjon":
#         print("Topildi")
#         break
#     else:
#         print("Hato")


#                                        Vazifalar                                         #

"""
1. While siklidan foydalanib print qiling:
1
22
333
4444
55555
"""

# num = 0
# a = []
#
# while num < 5:
#     num += 1
#     a.append(num)
#     print(*a)

"""
2. While dan foydalanib sondagi raqamlar yig'indisini topadigan dastur tuzing.
input: 555   output: 15
input: 8125   output: 16
"""

# while True:
#     num = input("Sonlar yig'indisi uchun son: ")
#     print(f"Yig'indi: {sum(int(digit) for digit in num)}")


"""
3. While orqali 1 dan 100 gacha bo'lgan toq solar yig'indisini topuvchi dastur tuzing
"""

# print("Toq sonlar yig'indisi: " + str(sum(r for r in range(1, 100 + 1, 2))))  # V-1

# ---V-2--- #

# i = 0
# toq = 0
#
# while i <= 100:
#     if i % 2 != 0: toq += i
#     i += 1
# print("Toq sonlar yig'indisi:", toq)

"""
4. While orrqali Ro'yxatdagi 2-eng katta sonni topuvchi dastur yozing
"""

# raqamlar = [23, 45, 12, 67, 34, 89, 90, 54]
# max_num = 0
# second_max = 0
# i = 0
#
# while i < len(raqamlar):
#     if raqamlar[i] > max_num:
#         second_max = max_num
#         max_num = raqamlar[i]
#     elif raqamlar[i] > second_max and raqamlar[i] != max_num:
#         second_max = raqamlar[i]
#     i += 1
#
# print("Ro'yxatdagi 2-eng katta son:", second_max)

"""
5. Taxmin qilish o'yinini simulyatsiya qiladigan dastur yarating.
Dastur 1 dan 100 gacha bo'lgan tasodifiy sonni yaratishi va
foydalanuvchidan raqamni taxmin qilishni so'rashi kerak.
Agar foydalanuvchi taxmini haqiqiy raqamdan yuqori bo'lsa, dastur "Juda baland!" va
foydalanuvchidan yana taxmin qilishni so'rang. Xuddi shunday, agar foydalanuvchining
taxmini haqiqiy raqamdan past bo'lsa, dastur "Juda past!" va foydalanuvchidan yana taxmin
qilishni so'rang. Dastur foydalanuvchidan to'g'ri raqamni topmaguncha taxmin qilishni so'rashi kerak.
"""

a = randint(1, 100 + 1)
print("Tahminiy sonni topish o'yini,")

while True:
    b = int(input("Taxmin qilingan sonni toping: "))

    if b > a:
        print("Juda baland! -", b - a)
    elif b < a:
        print("Juda past! +", a - b)
    else:
        print("Tabriklayman! To'g'ri topdingiz!")
        break

# # Top.1

# while 1:
#     rang = input("Svetafor qanday rangda: ").title()
#     if rang == "Qizil" or rang == "Sariq" or rang == "Yashil":
#         print("Rahmat, to'g'ri keladi!")
#         break
#     else:
#         print("Bu xato rang!")

# # Top.2

# a = randint(1, 10 + 1)
# print("Tahminiy sonni topish o'yini,")
#
# while 1:
#     b = int(input("Taxmin qilingan sonni toping: "))
#     if a != b:
#         print("Noto'g'ri, iltimos qayta urunib ko'rin!")
#     else:
#         print("Tabriklaymiz! siz topdingiz!")
#         break

# # Top.3

# a = []
#
# while 1:
#     name = input("Do'stingiz ismini kiriting: ").title()
#     if name == "Stop":
#         print(', '.join(a))
#         break
#     else:
#         a.append(name)

# # Top.4

# usd = 12_600
# print("Dollar so'mga o'tkazish")
#
# while 1:
#     i = input("Pul kiriting: ").title()
#     if i.isdigit():
#         print(int(i) * usd)
#     elif str(i) == "Exit":
#         print("To'xtatildi!")
#         break
#     else:
#         print("Xato kiritildi! Qayta urunib ko'ring,")
