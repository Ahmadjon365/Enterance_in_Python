"""Solved code"""

"""
1."Texnika" parent klass. Konstruktorida esa (brand, model, type) parametrlari bor.
    info() - (brand, model, type) ni print qilib beradi.

  "Laptops" child klassi bor. Unda konstruktirida qo'shimcha (video_card, ram, display).
    more_info() - (brand, model, type, video_card, ram, display) ni print qilib beradi.

  "Televisions" child klassi bor. Unda konstruktirida (size, display) parametrlari bor.
    more_info() - (brand, model, type, size, display) ni print qilib beradi.

  "Smartphones" child klassi bor. Unda konstruktirida (size, sim_count) parametrlari bor.
    more_info() - (brand, model, type, size, sim_count) ni print qilib beradi.
"""


class Texnika:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type

    def info(self):
        print(f"Brand: {self.brand},\nModel: {self.model},\nType: {self.type}")


class Laptops(Texnika):
    def __init__(self, brand, model, type, video_card, ram, display):
        super().__init__(brand, model, type)
        self.video_card = video_card
        self.ram = ram
        self.display = display

    def more_info(self):
        super().info()
        print(f"Video Card: {self.video_card},\nRAM: {self.ram},\nDisplay: {self.display}")


class Televisions(Texnika):
    def __init__(self, brand, model, type, size, display):
        super().__init__(brand, model, type)
        self.size = size
        self.display = display

    def more_info(self):
        super().info()
        print(f"Size: {self.size},\nDisplay: {self.display}")


class Smartphones(Texnika):
    def __init__(self, brand, model, type, size, sim_count):
        super().__init__(brand, model, type)
        self.size = size
        self.sim_count = sim_count

    def more_info(self):
        super().info()
        print(f"Size: {self.size},\nSIM Count: {self.sim_count}")


# laptop = Laptops("Lenovo", "83A1", "Notebook", "Intel Core i5 Gen 13", "8GB", "15.6-inch")
# laptop.more_info()
#
# television = Televisions("Samsung", "UE55NU7000", "LED", "UHD 4K", "55 inch")
# television.more_info()
#
# smartphone = Smartphones("Vivo", "v21e", "Mobile Phone", "6.5-inch", 3)
# smartphone.more_info()

"""
2."Transport" parent klass. Konstruktorida esa (brand, model, type) parametrlari bor.
    info() - (brand, model, type) ni print qilib beradi.

  "ElectroCars" - child klassi bor. Unda konstruktirida qo'shimcha (battery_life, charging_time).
    more_info() - (brand, model, type, battery_life, charging_time) ni print qilib beradi.

  "SportCars" - child klassi bor. Unda konstruktirida qo'shimcha (motor, color).
    more_info() - (brand, model, type, motor, color) ni print qilib beradi.

  "Truck" - child klassi bor. Unda konstruktirida qo'shimcha (motor, height, long, weight).
    more_info() - (brand, model, type, height, long, weight) ni print qilib beradi.
"""


class Transport:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type

    def info(self):
        print(f"Brand: {self.brand},\nModel: {self.model},\nType: {self.type}")


class ElectroCars(Transport):
    def __init__(self, brand, model, type, battery_life, charging_time):
        super().__init__(brand, model, type)
        self.battery_life = battery_life
        self.charging_time = charging_time

    def more_info(self):
        super().info()
        print(f"Battery Life: {self.battery_life},\nCharging Time: {self.charging_time}")


class SportCars(Transport):
    def __init__(self, brand, model, type, motor, color):
        super().__init__(brand, model, type)
        self.motor = motor
        self.color = color

    def more_info(self):
        super().info()
        print(f"Motor: {self.motor},\nColor: {self.color}")


class Truck(Transport):
    def __init__(self, brand, model, type, motor, height, long, weight):
        super().__init__(brand, model, type)
        self.motor = motor
        self.height = height
        self.long = long
        self.weight = weight

    def more_info(self):
        super().info()
        print(f"Motor: {self.motor},\nHeight: {self.height},\nLong: {self.long},\nWeight: {self.weight}")


# car = ElectroCars("Tesla", "Model S", "Electric Car", "22-37 years", "7 hours")
# car.more_info()
#
# sport_car = SportCars("Ferrari", "F8", "Sports Car", "6000 cc", "Red")
# sport_car.more_info()
#
# truck = Truck("Ford", "Mustang", "Truck", "6000 cc", 4.5, 200, 2000)
# truck.more_info()

"""
3.1"University" - parent klass. Konstruktorida esa (university) parametrlari bor.
    info() - (university) ni print qilib beradi.

  "Staff" - child klass. Unda konstruktirida qo'shimcha (first_name, last_name, age) parametrlari bor.
    staff_info() - (university, first_name, last_name, age) ni print qilib beradi.

  "Student" - child klass. U "Staff" dan vorislik oladi. Unda konstruktirida qo'shimcha (group) parametrlari bor.
    more_info() - (university, first_name, last_name, age, group) ni print qilib beradi.

  "Teacher" - child klass. U "Staff" dan vorislik oladi. Unda konstruktirida qo'shimcha (position, subject) parametrlari bor.
    more_info() - (university, first_name, last_name, position, subject) ni print qilib beradi.

  "OtherStaff" - child klass. U "Staff" dan vorislik oladi. Unda konstruktirida qo'shimcha (position) parametrlari bor.
    more_info() - (university, first_name, last_name, position,) ni print qilib beradi.
"""


class University:
    def __init__(self, university):
        self.university = university

    def info(self):
        print(f"University: {self.university}")


class Staff(University):
    def __init__(self, university, first_name, last_name, age):
        super().__init__(university)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def staff_info(self):
        super().info()
        print(f"First Name: {self.first_name},\nLast Name: {self.last_name},\nAge: {self.age}")


class Student(Staff):
    def __init__(self, university, first_name, last_name, age, group):
        super().__init__(university, first_name, last_name, age)
        self.group = group

    def more_info(self):
        super().staff_info()
        print(f"Group: {self.group}")


class Teacher(Staff):
    def __init__(self, university, first_name, last_name, age, position, subject):
        super().__init__(university, first_name, last_name, age)
        self.position = position
        self.subject = subject

    def more_info(self):
        super().staff_info()
        print(f"Position: {self.position},\nSubject: {self.subject}")


class OtherStaff(Staff):
    def __init__(self, university, first_name, last_name, age, position):
        super().__init__(university, first_name, last_name, age)
        self.position = position

    def more_info(self):
        super().staff_info()
        print(f"Position: {self.position}")


# university = University("TATU")
# staff = Staff(university, "John", "Doe", 25)
# staff.staff_info()
#
# student = Student(university, "Jane", "Smith", 20, "Mathematics")
# student.more_info()
#
# teacher = Teacher(university, "Mike", "Johnson", "Professor", "Physics")
# teacher.more_info()
#
# other_staff = OtherStaff(university, "Sarah", "Williams", "Manager")
# other_staff.more_info()

"""
3.2"Object" - child klass. U "University" dan vorislik oladi. Unda konstruktirida qo'shimcha (name) parametrlari bor.
    object_info() - (university, name) ni print qilib beradi.

  "Computer" - child klass. U "Object" dan vorislik oladi. Unda konstruktirida qo'shimcha (soni, tizimi, holati) parametrlari bor.
    object_more_info() - (university, name, soni, tizimi, holati) ni print qilib beradi.

  "Mebel" - child klass. U "Object" dan vorislik oladi. Unda konstruktirida qo'shimcha (soni, turi, holati) parametrlari bor.
    object_more_info() - (university, name, soni, turi, holati) ni print qilib beradi.
"""


class Object(University):
    def __init__(self, university, name):
        super().__init__(university)
        self.name = name

    def object_info(self):
        super().info()
        print(f"Name: {self.name}")


class Computer(Object):
    def __init__(self, university, name, soni, tizimi, holati):
        super().__init__(university, name)
        self.soni = soni
        self.tizimi = tizimi
        self.holati = holati

    def object_more_info(self):
        super().object_info()
        print(f"Number of CPUs: {self.soni},\nMemory Size: {self.tizimi},\nHolati: {self.holati}")


class Mebel(Object):
    def __init__(self, university, name, soni, turi, holati):
        super().__init__(university, name)
        self.soni = soni
        self.turi = turi
        self.holati = holati

    def object_more_info(self):
        super().object_info()
        print(f"Number of pieces: {self.soni},\nType: {self.turi},\nHolati: {self.holati}")


# university = University("TATU")
# object = Object(university, "Notebook")
# object.object_info()
#
# computer = Computer(university, "PC", 4, "Windows 10", "Intel Core i5")
# computer.object_more_info()
#
# mebel = Mebel(university, "Table", 1, "Wood", "Yangi")
# mebel.object_more_info()
