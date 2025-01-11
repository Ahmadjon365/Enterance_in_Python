# Polymorphism


class Odam:
    qollar_soni = 2
    oyoqlar_soni = 2


class Jangchi(Odam):
    energiya = 100
    jangdan_song = 30

    def jang_qil(self):
        if self.energiya >= self.jangdan_song:
            self.energiya -= self.jangdan_song
            print(f"Jangda {self.jangdan_song} energiya ketdi, Jangdan {self.energiya} qoldi!")
        else:
            print("Jangga energiya yetarli emas, o'ladi!")


# print(Jangchi.qollar_soni)  # 2

Jamshid = Jangchi()

# Jamshid.jang_qil()
# Jamshid.jang_qil()
# Jamshid.jang_qil()
# Jamshid.jang_qil()
#
# print(Jangchi.oyoqlar_soni)  # 2

from random import randint


class Shifokor(Odam):
    mahsuli = ["Suv", "Qora kunjut", "Jiyda"]

    def davola(self):
        if len(self.mahsuli) > 0:
            start = 0
            stop = len(self.mahsuli)
            print(f"Davolanmaqda {self.mahsuli.pop(randint(start, stop - 1))} bilan!")
        else:
            print("Davolanmoq uchun mahsul yo'q!")


Damir = Shifokor()


# Damir.davola()
# Damir.davola()
# Damir.davola()
# Damir.davola()
#
# print(Damir.qollar_soni)


class janchi_shifokor(Shifokor, Jangchi):
    pass


SuperMan = janchi_shifokor()

# SuperMan.jang_qil()
# SuperMan.davola()

"https://plausible-wolfberry-cb2.notion.site/19-1-dars-Konstruktor-va-Destruktor-be6a268c782d40678891f4c04ff7a5d0"
"https://plausible-wolfberry-cb2.notion.site/19-2-dars-Vorisdorlik-va-Polimorfizm-d2258ce127134d8e933287535d76a5ac"

"C++ tilidagi 'switch case'ning python versiyasi"
"https://www.geeksforgeeks.org/python-match-case-statement/"
