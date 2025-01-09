"""Tasks for practicing"""
from pandas.io.clipboard import clipboard_set

"""
Oson1. "Oson1" nomli klass elon qiling. Bu klassda "a" integer o'zgaruvchi bor.
output_a() - bu funksiya klassdagi "a" ni qiymatini print qilsin.
"""


class Oson1:
    def __init__(self, a):
        self.a = a

    def output_a(self):
        print(self.a)


obj = Oson1(10)
obj.output_a()

"""
Oson2. "Oson2" nomli klass elon qililar. Bu klassda "a" va "b" integer o'zgaruvchilari bor.
summa() - bu funksiya klassdagi "a" va "b" ni yig'indisini print qilsin.
"""


class Oson2:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def summa(self):
        print(self.a + self.b)


obj = Oson2(10, 11)
obj.summa()

"""
Oson3. "Oson3" nomli klass elon qililar. Bu klassda "a" integer o'zgaruvchisi bor.
plus_minus() - bu funksiya klassdagi "a" ni musbat yoki manfiy ekanligini print qilsin.
"""


class Oson3:
    def __init__(self, a):
        self.a = a

    def plus_minus(self):
        if self.a > 0:
            print("Musbat")
        elif self.a < 0:
            print("Manfiy")
        else:
            print("U ham bu ham emas")


obj = Oson3(0)
obj.plus_minus()

"""
Oson4. "Oson4" nomli klass elon qililar. Bu klassda "a" integer o'zgaruvchi bor.
odd_even() - bu funksiya klassdagi "a" ni toq yoki juft ekanligini print qilib bersin.
"""


class Oson4:
    def __init__(self, a):
        self.a = a

    def odd_even(self):
        if self.a % 2 == 0:
            print("Toq")
        else:
            print("Juft")


obj = Oson4(10)
obj.odd_even()

"""
Oson5. "Oson5" nomli klass elon qililar. Bu klassda "a" va "b" integer o'zgaruvchisi bor.
daraja() - bu funksiya klassdagi "a" ni "b" chi darajasini print qilsin.
"""


class Oson5:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def daraja(self):
        print(self.a ** self.b)


obj = Oson5(10, 10)
obj.daraja()

"""
6. "MyClass6" nomli klass elon qililar. Bu klassda "words" list bo'sh o'zgaruvchisi bor.
add_word(word) - bu funksiya "words" ga element qo'shib qo'ysin.
remove(word) = bu funksiya "words" da "word" ni o'chirib tashlasin.
"""


class MyClass6:
    words = []

    def add_word(self, word):
        self.words.append(word)

    def remove(self, word):
        if word in self.words:
            self.words.remove(word)


# Create an object and test
obj = MyClass6()
obj.add_word("BMW")
obj.add_word("Mers")
obj.add_word("BYD")
obj.remove("BYD")

print(obj.words)

"""
7. "MyClass7" nomli klass elon qiling. Bu klassda bo'sh "myDict" dictionary o'zgaruvchisi bor.
add_elem(key, val) - bu funksiya "myDict" "key" ni qiymatiga teng bo'lgan key bo'lmasa "val" ni add qilsin,
bor bolsa xech narsa qilmasin.
update_elem(key, val) - bu funksiya "myDict" shu "key" ni qiymatiga teng bolgan key bo'lsa "val" ni update qilsin,
yoq bolsa xech narsa qilmasin.
"""


class MyClass7:
    myDict = {}

    def add_some(self, key, value):
        if key in self.myDict.keys():
            pass
        else:
            self.myDict[key] = value

    def update_some(self, key, value):
        if key in self.myDict:
            self.myDict[key] = value
        else:
            pass

    def chop_et(self):
        print(self.myDict)


some = MyClass7

some.add_some(MyClass7, "sen", "men")
some.chop_et(MyClass7)
some.update_some(MyClass7, "sen", "siz")
some.chop_et(MyClass7)

"""
8. "MyClass8" nomli klass elon qililar. Bu klassdan "numbers" list o'zgaruvchisi bor.
compare_lists(new_list) - bu funksiya klassdagi "numbers" ni elementlar yig'indisi 
"new_list" ni elementlar yig'indisidan katta aniqlab katta listni print qilsin.
"""

"""
9. "MyClass9" nomli klass elon qililar. Bu klassdan "list1" va "list2" list o'zgaruvchilari bor.
list1_max() - bu funksiya klassdagi "list1" dan maximumni topib return qilsin.
list2_max() - bu funksiya klassdagi "list2" dan maximumni topib return qilsin.
sum_of_two_max() - bu funksiya klassdagi list1_max() va list2_max() foydalanib ikkita maximumni topib yig'indisini print qilsin.
"""

"""
10. "MyClass10" nomli klass elon qililar. Bu klass "numbers" list o'zgaruvchilari bor.
divide(d) - bu funksiya klassadagi "numbers" list elementlarini "d" qoldiqsiz bo'linsa bitta list yig'sin funksiyani ichida.
va funksiya oxirida bolinadigonlarni listini return qilsin.
"""
