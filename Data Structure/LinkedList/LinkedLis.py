# i = 1
# while i <= 10:  # 10 < 10
#     print(i, end=" ")  # 1 2 3 4 5 6 7 8 9
#     i += 1  # 1 += 1 + 1 + 1+1+1+1+1+1+1=10


# i = 1
# a = int(input())  # 12
# while i <= a:  # 14 <= 12
#     print(i, end=" ")  # 0 2 4 6 8 10 12
#     i += 2  # 0 += 2+2+2+2+2+2+2

# i = 0
# while True:  # cheksiz sikl xosil qilish
#     i += 1
#     print(i, '. I Love Python🤍')
#     if i == 100:
#         break  # siklni to'xtatish

# i = 0
# n = int(input())  # 12
# while i <= n:  # 0 <= 0
#     print(n, end=" ")  # 12 11 10 9 8 7 ... 0
#     n -= 1  # 12 -= 1-1-1-1-1....-1

# i = 0
# while i < 10:
#     i += 1
#     if i == 5:
#         continue  # davom etish/tashlab otib ketish
#     print(i, end=" ")

# a = int(input('son1 = '))
# b = int(input('son2 = '))
# if a < b:
#     while a <= b:
#         print(a, end=" ")
#         a += 1
# else:
#     while b <= a:
#         print(b, end=" ")
#         b += 1

# i = 1
# summa = 0
# while i <= 10:
#     summa += i
#     # print(summa, end=" ")
#     i += 1
# print(summa)


# -------------------------------------------------------------
# Pythonda for sikli

# for i in range(1, 10+1, 2):
#     print(i, end=" ")

# i = 1
# while i <= 10:
#     print(i, end=" ")
#     i += 2

# a = int(input('son = '))
# for i in range(0, a+1, 5):
#     print(i, end=" ")

# for i in range(0, 15):
#     if i % 2 == 0:
#         print(i, end=" ")

# n = int(input('son = '))
# for son in range(n):
#     pass

# m = int(input())  # 4
# for j in range(m+1):  # 4 <= 4
#     print(j*j, end=" ")  # 0 1 4 9 16


# for i in range(5, 10):
#     print(i, end=" ")

# a = int(input('son1 = '))
# b = int(input('son2 = '))
# if a < b:
#     for i in range(a, b):
#         print(i, end=" ")
# else:
#     for obj in range(b, a):
#         print(obj, end=" ")

# a = int(input())
# for i in range(a, -1, -1):
#     print(i, end=" ")

# a = int(input())
# for i in range(a, -1, -1):
#     if i % 2 != 0:
#         print(i, end=" ")

# Pythonda nested looplar

# i = 1
# while i <= 5:  # 2 <= 5
#     j = 1
#     while j <= 6:  # 1 <= 6
#         print(j, end=" ")  # 1 2 3 4 5 6
#         j += 1  # 1+1+1+1+1+1+1
#     print()
#     i += 1 # 1+1

# a = int(input())
# i = 1
# while i <= a:
#     j = 1
#     while j <= a:
#         print('*', end=" ")
#         j += 1
#     print()
#     i += 1

# i = 1
# while i <= 5:  # 2 <= 5
#     j = 1
#     while j <= i:  # 2 < 2
#         print('*', end=" ")  # 0 1
#         j += 1  # 0+1+1
#     print()
#     i += 1

# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print('*', end=" ")
#     print()


# for k in range(1, 5+1):
#     for g in range(1, k+1):
#         print('*', end=" ")
#     print()

# for j in range(1, 5+1):  # 1 <= 5
#     i = 5-j  # i = 10-1
#     for i in range(j, 5+1, 1):  # 0< 10
#         print('*', end=" ")  # 0 1 2 3 4 5
#     print()
# n = 5
# for i in range(1, n+1):  # 1 <= 5
#     for j in range(n-i):  # 1 < 5
#         print(' ', end="")
#     for k in range(1, i+1):
#         print(k, end=" ")
#     print()





















