# En: Slicing; Conditions of if, elif, else; Operators of and, or; Conditional symbols of in, not in;
# Uz: Kesish; Shartlar; Operatorlar; Shartli belgilar:
from imp import new_module
from time import perf_counter

# # Slicing: # Example
#
# my_list = [True, False, 0, 1, 3]
# my_sentence = "The world is the best in the world"
# one = my_list[1:3]
# two = my_sentence[4::2]
# print(one, " | ", two)

# # if, elif, else:
#
# number = int(input("Son kiriting: "))
# if number >= 1:
#     print("Musbat son")
# elif number == 0:
#     print("Neytral son")
# else:
#     print("Manfiy son")

# # and, or:
#
# name = input("Ismingiz: ")
# age = int(input("Yoshingiz: "))
# if name.istitle() and age >= 18:
#     print(f"Sizning ismingiz: {name} va siz o'smir ekansiz.")
# elif not name.istitle() and age <= 17:
#     print(
#         f"Siz ismingizni bosh harifini kichik yozdingiz,"
#         f" siz mana shunaqa yozishingiz kerak edi: {name.title()}"
#         f" va siz o'smir emas ekansiz.")
# else:
#     print(f"Sizning ismingiz: {name}, yoshingiz: {age}")

# # in, not in:
#
# the_list = [False, 23, 34, True]
# i = int(input("Kiriting: "))
# if i in the_list:
#     print("Manbada mavjud!")
# elif i not in the_list:
#     print("Manbada mavjud emas!")
# # else:
# #     print("Mavjud emas!")

#                                        Vazifalar                                         #

""" 1. Ob-havo Tavsifi: Foydalanuvchidan ob-havo haroratini inputda so'rang.
 Agar harorat 0 dan past bo'lsa, "Sovuq" deb print chiqaring.
 Agar 0 dan 20 gacha bo'lsa, "Salqin".
 Agar 21 dan 30 gacha bo'lsa, "Iliq".
 Agar 31 dan yuqori bo'lsa, "Issiq" deb chiqaring."""

# ob_havo = int(input("Harorat: "))
#
# if ob_havo < 0:
#     print("Sovuq")
# elif ob_havo <= 20 > 0:
#     print("Salqin")
# elif ob_havo <= 30 > 21:
#     print("Iliq")
# elif ob_havo >= 31:
#     print("Issiq")

""" 2. Internet-do'kon Chegirmasi: Foydalanuvchidan xarid summasini so'rang. Agar summa
 50,000 so'mdan kam bo'lsa, chegirma yo'q. Agar 50,000 dan 100,000 so'mgacha bo'lsa,
 5%chegirma. Agar 100,000 so'mdan yuqori bo'lsa, 10% chegirma hisoblang va yakuniy
 narxni chiqaring."""

# narx = int(input("Hardi summasini kiriting: "))
# if narx <= 50_000:
#     print("Chegirmasiz harid!")
# elif narx < 100_000 > 50_000:
#     print("5% li Chegirmali harid!")
# else:
#     print("10% li chegirmali harid!")
# print("Haridingiz uchun rahmat :)")


""" 3. Tizimga Kirish: Foydalanuvchidan login va parolni so'rang. Agar login "admin" va parol
"12345" bo'lsa, "Xush kelibsiz, admin!" deb chiqaring. Agar login yoki parol noto'g'ri bo'lsa,
"Login yoki parol xato" deb chiqaring."""

# nickname = "admin"
# password = "12345"
# i = input("Username ni kiriting: ")
# i_ = input("Parolni kiriting: ")
# if i == nickname and i_ == password:
#     print("Xush kelibsiz, Admin!")
# else:
#     print("Username yoki parol xato!")

""" 4. Film Yosh Cheklovi: Foydalanuvchidan yoshini so'rang. Agar yosh 13 dan kichik bo'lsa,
"Sizga ushbu film tavsiya etilmaydi" deb chiqaring. Agar 13 dan 17 gacha bo'lsa, "Siz filmni
ota-onangiz bilan ko'rishingiz mumkin". Agar 18 va undan katta bo'lsa, "Siz filmni tomosha
qilishingiz mumkin" deb chiqaring."""

# age = int(input("Yoshingiz: "))
# if age < 13:
#     print("Sizga ushbu film tavsiya etilmaydi!")
# elif age <= 17 >= 13:
#     print("Siz  filmni ota-onangiz bilan ko'ra olasiz.")
# elif age >= 18:
#     print("Siz filmni tomosha eta olasiz.")

""" 5. Restoran Menyusi: Foydalanuvchiga menyudan taom tanlash imkoniyatini bering: 1
"Osh", 2- "Mastava", 3- "Shashlik". Tanlovga qarab taomning narxi va tayyorlanish vaqtini
chiqaring."""

# meals = {1: {"Vaqti": 40, "Nomi": "Osh", "Narxi": 35_000}, 2: {"Vaqti": 30, "Nomi": "Mastava", "Narxi": 25_000},
#          3: {"Vaqti": 35, "Nomi": "Shashlik", "Narxi": 30_000}}
#
# i = int(input("Menudan tanlang: 1: Osh, 2: Mastava, 3: Shashlik: "))
#
# meal_name = meals[1]["Nomi"]
# meal_name_ = meals[2]["Nomi"]
# meal_name__ = meals[3]["Nomi"]
#
# meal_time = meals[1]["Vaqti"]
# meal_time_ = meals[2]["Vaqti"]
# meal_time__ = meals[3]["Vaqti"]
#
# meal_price = meals[1]["Narxi"]
# meal_price_ = meals[2]["Narxi"]
# meal_price__ = meals[3]["Narxi"]
#
# if i == 1:
#     print(f"Sizning taomonigiz: {meal_name}\nTayyorlanish vaqti: {meal_time}\nNarxi: {meal_price}")
# elif i == 2:
#     print(f"Sizning taomonigiz: {meal_name_}\nTayyorlanish vaqti: {meal_time_}\nNarxi: {meal_price_}")
# elif i == 3:
#     print(f"Sizning taomonigiz: {meal_name__}\nTayyorlanish vaqti: {meal_time__}\nNarxi: {meal_price__}")
# else:
#     print("Bunday taom mavjud emas!")

""" 6. Email Tekshiruvi: Foydalanuvchidan email manzilini inputda kiritishni so'rang. Agar
emailda "@" belgisi va "." nuqtasi bo'lmasa, "Noto'g'ri email manzili" deb chiqaring. Aks
holda, "Email qabul qilindi" deb chiqaring.
Yordam: find() string metodidan foydalaning. Masalan if matn.find(“belgi”) ==-1 bo’lsa
demak belgi matnda topilmagan bo’ladi."""

# i = input("Emailni kiriting: ")
#
# if i.find("@") and i.find("."):
#     print("Email qabul qilindi!")
# else:
#     print("Email hato kiritilgan!")

"""7. Talaba Baholash Tizimi: Foydalanuvchidan olgan ballini so'rang (0 dan 100 gacha).
Quyidagi mezonlarga ko'ra bahoni print qiling:
● 86 dan 100 gacha: 5 baho
● 70 dan 85 gacha: 4 baho
● 55 dan 69 gacha: 3 baho
● 55 dan past: 2 baho"""

# mark = int(input("Talaba bahosini kiriting (0-100): "))
#
# if mark < 55:
#     print("2 baho")
# elif mark < 70 >= 55:
#     print("3 baho")
# elif mark < 86 >= 70:
#     print("4 baho")
# elif mark <= 100 > 85:
#     print("5 baho")
# else:
#     print("Bunday baholash mavjud emas!")

""" 8. Bankomat Pul Yechish: Foydalanuvchidan kartasidagi summani va yechmoqchi
bo'lgan summani so'rang. Ya’ni 2 ta input bo’ladi. Agar kartadagi puli yechiladigan puldan
kam bo'lsa, "Hisobda yetarli mablag' mavjud emas" deb print chiqaring. Agar yechiladigan
summa 5 000 so'mdan kam bo'lsa, "Minimal yechish summasi 5 000 so'm" deb chiqaring.
Aks holda, "Pul muvaffaqiyatli yechildi" deb print chiqaring va kartadagi qolgan mablag'ni
print qiling."""

# i = int(input("Qancha mablag' mavjud: "))
# i_ = int(input("Qancha mablag' yechib olasiz: "))
#
# if i_ > i:
#     print("Mablag' yetarli emas!")
# elif i_ < 5_000:
#     print("Eng past yechish narxi 5.000 so'm!")
# else:
#     print("Pul muvaffaqiyatli yechib olindi!")

""" 9. Ish Jadvalini Tekshirish: Foydalanuvchidan haftaning kunini so'rang (Dushanba,
Seshanba, ... , Yakshanba). Agar kun "Shanba" yoki "Yakshanba" bo'lsa, "Bugun dam olish
kuni" deb chiqaring. Aks holda, "Bugun ish kuni" deb chiqaring."""

# dates = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
# rest_days = dates[5:]
# work_days = dates[0:5]
#
# a = input("Hafta kunini kiriting: ").title()
#
# if a in rest_days:
#     print("Bugun dam olish kuni!")
# elif a in work_days:
#     print("Bugun ish kuni!")
# else:
#     print("Bunday hafta kuni mavjud emas!")

""" 10. Mobil Tarif Tanlash: Foydalanuvchidan oyiga qancha internet trafikidan foydalanishini
so'rang (GB da). Agar trafik 1 GB dan kam bo'lsa, "Sizga 'Mini' tarifi mos keladi" deb
chiqaring. Agar 1 GB dan 5 GB gacha bo'lsa, "Sizga 'Standard' tarifi mos keladi". Agar 5
GBdan yuqori bo'lsa, "Sizga 'Unlimited' tarifi mos keladi" deb chiqaring."""

# i = int(input("Ta'rif rejasini MB ko'rinishida kiriting: "))
# if i < 1024:
#     print("Sizga 'Mini' ta'rifi mos keladi.")
# elif i < 5120 > 1024:
#     print("Sizga 'Standard' ta'rifi mos keladi.")
# elif i > 5120:
#     print("Sizga 'Unlimited' ta'rifi mos keladi.")
