# Coding languages;
# Tuple; Set; Dictionary;
# Mutable & Immutable; Operators & operands;
from setuptools.command.build_ext import if_dl

# JavaScript is weak; Python is strong:

# # ver num = 42 + "666"
# # "42666"

num = 42  # + "666"
num_ = str(42) + "666"
num__ = 42 + int("666")
num___ = "42" + "666"  # "42666"

# Collecting information:

my_tuple = (3, 2, 1)  # Immutable collection
my_set = {3, 2, 1}  # Orderly collection
my_dict = {
    "Firstname": "Ahmadjon",
    "Lastname": "Abdulfotih",
    "Age": 16.1,
    "Class": 10
}  # Key: Value, ...; Mutable collection

# Mutable VS Immutable:

my_num = 333
print(id(my_num))  # 1737340315984
my_num += 333
print(id(my_num))  # 1737355479088

l: list = [1, 2.1]
print(id(l))  # 1737392366400
l.append("This")
print(id(l))  # 1737392366400

# Operands in operators:

# Unary operands: +, -, *, /;
# Binary operands: ==, !=, <=, >=, <, >, ...;
# Ternary operands: if, elif, else, and, ...;
