"""Tasks that third lesson"""

"""
Instance Method Tasks:

1. Create a class BankAccount with an attribute balance. Implement methods deposit, withdraw, and check_balance to deposit, withdraw, and check the balance of the bank account, respectively.
2. Create a class Rectangle with attributes length and width. Implement methods area, perimeter, and is_square to calculate the area, perimeter, and check if the rectangle is a square, respectively.
3. Create a class Student with attributes name, age, and grades. Implement methods add_grade, calculate_average, and print_summary to add a grade, calculate the average grade, and print the student's summary, respectively.
4. Create a class Circle with attribute radius. Implement methods area, circumference, and diameter to calculate the area, circumference, and diameter of the circle, respectively.
5. Create a class Book with attributes title, author, and current_page. Implement methods open, turn_page, and restart to open the book at a specific page, turn the page, and restart the book at page 1, respectively.
"""


# 1
class BankAccount:
    def __init__(self, balance: int):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"

    def check_balance(self):
        return self.balance


# 2
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def is_square(self):
        return self.length == self.width


# 3
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def print_summary(self):
        print(f"Name: {self.name}\nAge: {self.age}\nAverage Grade: {self.calculate_average():.2f}")


# 4
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14159 * self.radius

    def diameter(self):
        return 2 * self.radius


# 5
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.current_page = 1

    def open(self, page):
        self.current_page = page

    def turn_page(self, pages=1):
        self.current_page += pages

    def restart(self):
        self.current_page = 1


# Example usage:
# BankAccount
account = BankAccount(15000)
account.deposit(5000)
account.withdraw(11000)
print("Current Balance:", account.check_balance())

# Rectangle
rect = Rectangle(5, 5)
print("Rectangle Area:", rect.area())
print("Rectangle Perimeter:", rect.perimeter())
print("Is Square:", rect.is_square())

# Student
student = Student("John", 16)
student.add_grade(90)
student.add_grade(80)
student.add_grade(85)
student.print_summary()

# Circle
circle = Circle(7)
print("Circle Area:", circle.area())
print("Circle Circumference:", circle.circumference())
print("Circle Diameter:", circle.diameter())

# Book
book = Book("Python Programming", "Author Name")
book.open(100)
print("Current Page:", book.current_page)
book.turn_page(10)
print("Current Page after turning pages:", book.current_page)
book.restart()
print("Current Page after restart:", book.current_page)

"""
Class Method Tasks:

6. Create a class Dog with a class-level attribute total_dogs and a method get_total_dogs that returns the number of dog instances created.
7. Create a class Computer with class-level attributes total_computers and computers_list. Implement a method add_computer that adds a computer instance to the list and updates the total_computers count.
8. Create a class Employee with class-level attributes total_employees and employees_list. Implement a method hire_employee that adds an employee instance to the list and updates the total_employees count.
9. Create a class Television with a class-level attribute average_screen_size and a method update_average_screen_size that updates the average screen size when a new television instance is created.
10. Create a class Course with class-level attributes total_courses and courses_list. Implement a method add_course that adds a course instance to the list and updates the total_courses count.
"""


class Dog:
    total_dogs = 0

    def __init__(self):
        Dog.total_dogs += 1

    @classmethod
    def get_total_dogs(cls):
        return cls.total_dogs


class Computer:
    total_computers = 0
    computers_list = []

    def __init__(self, name):
        self.name = name
        Computer.add_computer(self)

    @classmethod
    def add_computer(cls, computer):
        cls.computers_list.append(computer)
        cls.total_computers += 1


class Employee:
    total_employees = 0
    employees_list = []

    def __init__(self, name):
        self.name = name
        Employee.hire_employee(self)

    @classmethod
    def hire_employee(cls, employee):
        cls.employees_list.append(employee)
        cls.total_employees += 1


class Television:
    average_screen_size = 0
    total_televisions = 0

    def __init__(self, screen_size):
        self.screen_size = screen_size
        Television.update_average_screen_size(screen_size)

    @classmethod
    def update_average_screen_size(cls, screen_size):
        cls.total_televisions += 1
        cls.average_screen_size = (
                                          ((cls.total_televisions - 1) * cls.average_screen_size) + screen_size
                                  ) / cls.total_televisions


class Course:
    total_courses = 0
    courses_list = []

    def __init__(self, name):
        self.name = name
        Course.add_course(self)

    @classmethod
    def add_course(cls, course):
        cls.courses_list.append(course)
        cls.total_courses += 1


# Example usage:
# Dog
dog1 = Dog()
dog2 = Dog()
print("Total Dogs:", Dog.get_total_dogs())

# Computer
comp1 = Computer("Laptop")
comp2 = Computer("Desktop")
print("Total Computers:", Computer.total_computers)
print("Computer List:", [comp.name for comp in Computer.computers_list])

# Employee
emp1 = Employee("Alice")
emp2 = Employee("Bob")
print("Total Employees:", Employee.total_employees)
print("Employee List:", [emp.name for emp in Employee.employees_list])

# Television
tv1 = Television(55)
tv2 = Television(65)
print("Average Screen Size:", Television.average_screen_size)

# Course
course1 = Course("Math")
course2 = Course("Physics")
print("Total Courses:", Course.total_courses)
print("Courses List:", [course.name for course in Course.courses_list])

"""
Static Method Tasks:

11. Create a class Math with a static method multiply that takes two numbers and returns their product.
12. Create a class Temperature with a static method celsius_to_fahrenheit that converts a given Celsius temperature to Fahrenheit.
13. Create a class Distance with a static method miles_to_kilometers that converts a given distance in miles to kilometers.
14. Create a class Utility with a static method is_even that checks if a given number is even or not.
15. Create a class Time with a static method seconds_to_minutes that converts a given time in seconds to minutes and seconds (as a tuple).
"""


class Math:
    @staticmethod
    def multiply(a, b):
        return a * b


class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32


class Distance:
    @staticmethod
    def miles_to_kilometers(miles):
        return miles * 1.60934


class Utility:
    @staticmethod
    def is_even(number):
        return number % 2 == 0


class Time:
    @staticmethod
    def seconds_to_minutes(seconds):
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        return minutes, remaining_seconds


# Example usage:
# Math.multiply
print(Math.multiply(5, 3))  # Output: 15

# Temperature.celsius_to_fahrenheit
print(Temperature.celsius_to_fahrenheit(25))  # Output: 77.0

# Distance.miles_to_kilometers
print(Distance.miles_to_kilometers(10))  # Output: 16.0934

# Utility.is_even
print(Utility.is_even(4))  # Output: True
print(Utility.is_even(5))  # Output: False

# Time.seconds_to_minutes
print(Time.seconds_to_minutes(125))  # Output: (2, 5)
