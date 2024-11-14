# # Recursive functions


# def factorial(a):
#     if a == 1:
#         return 1
#     else:
#         return factorial(a - 1) * a
#
#
# print(factorial(5))


# def countdown(n):
#     print(n)
#     if n > 0:
#         countdown(n - 1)


# def factorial(n):
#     return 1 if n <= 1 else n * factorial(n - 1)
#
#
# print(factorial(4))


# def is_palindrome(word):
#     """Agarda so'z palindrom so'z bo'lsa True, yo'qsa False."""
#     if len(word) <= 1:
#         return True
#     else:
#         return word[0] == word[-1] and is_palindrome(word[1:-1])
#
#
# print(is_palindrome('kiyik'))


# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci(num - 1) + fibonacci(num - 2)
#
#
# print(fibonacci(9))


# # With cache:
# def fibonacci(num, cache={}):
#     if num in cache:
#         return cache[num]
#     if num == 0:
#         result = 0
#     elif num == 1:
#         result = 1
#     else:
#         result = fibonacci(num - 1) + fibonacci(num - 2)
#     cache[num] = result
#     return result
#
#
# print(fibonacci(100))


# # Quick sort VS Tim sort;
"""
Tim sort xotirani kamroq yeydi va murakkab funksiya (python foydalanadi, tezkor);
Quick sort esa xotiradan ko'proq joy oladi.
"""

# def quick_sort(lst):
#     if len(lst) <= 1:
#         return lst
#     else:
#         pivot = lst[0]
#         left = [x for x in lst[1:] if x <= pivot]
#         right = [x for x in lst[1:] if x > pivot]
#         return quick_sort(left) + [pivot] + quick_sort(right)
#
#
# print(quick_sort([4, 7, 1, -2, 5, 6, 3]))


#                                        Vazifa                                         #

# # Tower of Hanoi: Solving the puzzle:
# def TowerOfHanoi(n, tayoqdan='A', tayoqqa='C', yordamchi='B'):
#     # Agar faqat bitta disk bo'lsa, uni bevosita maqsaddagi tayoqqa ko'chirish
#     if n == 1:
#         print(n, "- diskni oling", tayoqdan, 'dan', tayoqqa, "ga")
#         return
#
#     # 1-qadam: n-1 ta diskni yordamchi tayoqqa ko'chirish
#     TowerOfHanoi(n - 1, tayoqdan, yordamchi, tayoqqa)
#
#     # 2-qadam: eng katta (n) diskni boshlang'ich tayoqdan maqsaddagi tayoqqa ko'chirish
#     print(n, "- diskni ko'chiring", tayoqdan, 'dan', tayoqqa, "ga")
#
#     # 3-qadam: yordamchi tayoqdagi disklarni maqsaddagi tayoqqa ko'chirish
#     TowerOfHanoi(n - 1, yordamchi, tayoqqa, tayoqdan)
#
#
# # Misol
# n = int(input("Disklar sonini kiriting: "))
# TowerOfHanoi(n)
