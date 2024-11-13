# List comprehensions

# l = ['car', 3, 4, 2, 5, 1, 'car', 'car']
# lt = [i for i in range(len(l)) if l[i] == 'car']
#
# print(lt)

# humans = [('You', 999_000), ('We', 1_789_000), ('Me', 5_710_000), ('They', 111_000), ('He / She / It', 779_000)]
# millionaires = [name for name, money in humans if money > 999_000]
#
# print(millionaires)

# column_name = ['Name', 'Salary', 'Job']
# row_name = [('Abdul', 1_000, 'Designer'),
#             ('Abdul', 500, 'Videographer'),
#             ('Abdul', 777, 'Motion grapher'),
#             ('Abdul', 400, 'Operator'),
#             ('Abdul', 1_500, 'Developer')]
#
# db = [dict(zip(column_name, row)) for row in row_name]
# print(db)

# # lambda:

# x = lambda double: double ** 2  # def x(double): return double**2
# print(x(5))

# # map:

# str_list = ['9', '7', '8', '6', '4', '5', '2', '1', '3']
# int_list = list(map(int, str_list))
# print(sum(int_list))

# the_ns = [4, 5, 6, 7]
# print(list(map(lambda a: a * 2, the_ns)))

# print(list(map(lambda a, b: a - b, [3, 5, 7], [2, 4, 6])))

# # reduce: # faktorialni topish:
# from functools import reduce
#
# a = 5
# print(reduce(lambda x, y: x * y, range(1, a + 1)))

# # The end of codes ;)

# filter: appending only True

# l = [2, 4, 3, 5, 6, 7, 8, 9]
# r = list(filter(lambda z: z % 2 == 0, l))
# print(r)
