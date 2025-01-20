# Methods
# Encapsulation

"""
Encapsulation - Inkapsulatsiya

Encapsulation - bu ma’lumotlar va metodlarni bitta birlikda saqlash imkoniyati.

Ya’ni class yaratganimizda biz inkapsulatsiyadan foydalangan bo’lamiz. Chunki bir class da biz ham attribut,
ham metodlardan foydalanamiz:
"""


# Encapsulation: https://plausible-wolfberry-cb2.notion.site/21-dars-ENCAPSULATION-7684d82dd6884e8388377a409b4a6843
class Employee:
    def __init__(self, name, project):
        self.name = name
        self.project = project  # These are data members

    def work(self):  # And this is Method
        print(self.name, 'is works', self.project)


# Methods:
"""
https://plausible-wolfberry-cb2.notion.site/20-dars-Metodlar-536d8aa551414cceaad20a799037039e

- Instance method: obyektning o’zgaruvchilaridan foydalanish uchun ishlatiladigan method. Unda self parametri bo’lishi shart. self - obyektni anglatadi.
- Class method: Class ning o’zgaruvchilaridan foydalanish uchun ishlatiladigan method.  Unda cls parametri bo’lishi kerak. cls - o’sha classning o’zini anglatadi.
- Static method: Qo’shimcha funksionallar uchun funksiya bo’lib, unda biz obyektning yoki class ning o’zgaruvchilaridan foydalanmaymiz. self va cls kabi parametrlari bo'lmaydi.
"""


class Student:
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Class method
    @classmethod
    def change_school(cls, school_name):
        # class_name.class_variable
        cls.school_name = school_name

    # Instance method
    def show(self):
        print(self.name, self.age, 'School:', Student.school_name)


jon = Student('Jessa', 20)
jon.show()

# change school_name
Student.change_school('XYZ School')
jon.show()


# Static method:
class Employe:
    @staticmethod
    def sample(x):
        print('Inside static method', x)


# call static method
Employe.sample(10)

# can be called using object
emp = Employe()
emp.sample(10)


class Test:
    @staticmethod
    def static_method_1():
        print('static method 1')

    @staticmethod
    def static_method_2():
        Test.static_method_1()

    @classmethod
    def class_method_1(cls):
        cls.static_method_2()


# call class method
Test.class_method_1()

"""
- Public Member: Classdan tashqarida ishlatsa bo’ladigan
- Private Member: Faqat class ichida ishlatsa bo’ladigan
- Protected Member: Classda va unda voris olgna sub-class larda ishlatsa bo’ladigan
"""
