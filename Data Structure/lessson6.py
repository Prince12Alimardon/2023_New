# n = int(input())
# i = 0
# while i <= n:
#     if i % 3 == 0:
#         print(i, end=" ")
#     i += 1


# n = int(input())
# i = 0
# while i <= n:
#     print(i, end=" ")
#     i += 3
# n = int(input())
# for i in range(n+1):
#     if i % 3 == 0:
#         print(i, end=" ")

# n = int(input())
# for i in range(0, n+1, 3):
#     print(i, end=" ")

# def uchga_karrali():
#     n = int(input())
#     for i in range(n, 1, 1):
#         if i % 3 == 0:
#             print(i, end=" ")
#
#
# uchga_karrali()

# def max_min(x, y, z, f):


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# max_min(a, b, c, d)


# def max_min(a, b, c, d):
#     if a >= b and a >= c and a >= d:
#         print("Max =", a)
#     elif b >= a and b >= c and b >= d:
#         print("Max =", b)
#     elif c >= a and c >= b and c >= d:
#         print("Max =", c)
#     elif d >= a and d >= b and d >= c:
#         print("Max =", d)
#     if a <= b and a <= c and a <= d:
#         print("Min =", a)
#     elif b <= a and b <= c and b <= d:
#         print("Min =", b)
#     elif c <= a and c <= b and c <= d:
#         print("Min =", c)
#     elif d <= a and d <= c and d <= b:
#         print("Min =", d)
#
# q = int(input())
# w = int(input())
# r = int(input())
# e = int(input())
# max_min(q, w, r, e)

# def summa(n):
#     suma = 0
#     for i in range(n+1):
#         suma += i
#     print(suma)
#
#
# a = int(input())
# summa(a)

# def total(n):  # n = 4
#     a = int(input())  # 8
#     summa = 0
#     for i in range(n, a+1):  # 4 <= 8
#         summa += i  # 30 += 4 + 5 + 6 + 7 + 8
#     print(summa)  # 30
#
#
# a = int(input())  # 4
# total(a)

# def summ(n):
#     return n * (n + 1)
#
#
# n = int(input('son = '))
# print(summ(n))

#
# def print_row1(n):
#     print(n,end="")
#     print(n,end="")
#     print(n,end="")
#     print(n)
#
# def print_row2(n):
#     print(n, end="  ")
#     print(n)
#     print(n, end="  ")
#     print(n)
#
# a = int(input('son: '))
# print_row1(a)
# print_row2(a)
# print_row1(a)


# def print_row1(n):
#     for i in range(n):
#         print(n, end="")
#
# def print_row2(n):
#     print(n, end="")
#     for i in range(n-2):
#         print(' ', end='')
#     print(n)
#     print(n, end="")
#     for i in range(n - 2):
#         print(' ', end='')
#     print(n)
#
#
# d = int(input('son: '))
# print_row1(d)
# print()
# print_row2(d)
# print_row1(d)


# def star(n):
#     for i in range(n):
#         for j in range(i+1):
#             print('*', end=" ")
#         print()
#
#
# a = []
# j = int(input())
# while j > 0:
#     a.append(j)
#     j = int(input())
#
#
# for i in a:
#     star(i)

# a = [2, 3, 123, 12, 3412, 4, 1]
# a = [1, 2, 3, 4, 5, 6, 7]
# print(a[4])  # 5
# print(a[6])  # 7
# print(a[-1])  # 7
# print(a[-2])  # 2
# print(a)  # [1, 2, 3, 4, 5, 6, 7]
# print(a[:])  # [1, 2, 3, 4, 5, 6, 7]
# print(a[1:5])  # [2, 3, 4, 5]
# print(a[2:6])  # [3, 4, 5, 6]
# print(a[2:6 + 1])  # [3, 4, 5, 6, 7]
# print(a[2:])  # [3, 4, 5, 6, 7]
# print(a[2: -2])  # [3,4,5]
# print(a[:-1])  # [1, 2, 3, 4, 5, 6]
# print(a[::])  # [1, 2, 3, 4, 5, 6, 7]
# print(a[1::])  # [2, 3, 4, 5, 6, 7]
# print(a[1:5])  # [2, 3, 4, 5]
# print(a[::-1])  # [7, 6, 5, 4, 3, 2, 1]
# print(a[:6:2])  # [1, 3, 5]
# print(a[::2])  # [1, 3, 5, 7]
# print(a[::1])  # [1,2,3,4,5,6,7]
#
# c = a[1] + a[4]
# print(c)
# a = a[5] * a[0]
# print(a)

# import math
# def max_ildiz(a, b):
#     j = max(a, b)
#     return int(math.sqrt(j))
#
#
# n = int(input('son1 = '))
# m = int(input('son2 = '))
# print(max_ildiz(n, m))


# def register(name, email, password1, password2):
#     if password1 == password2:
#         print(name, "Muvafaqqiyatli o'tdingiz!\n", "Email:", email)
#     else:
#         print(name, 'Qayta urining!')
#
#
# ism = input('ism: ')
# pochta = str(input('pochta: '))
# parol1 = int(input('parol1: '))
# parol2 = int(input('parol2: '))
# register(ism, pochta, parol1, parol2)


# a = []
# print(type(a), a)

# a = ['apple', 'banana', 'orange', 'peach']
# print(a[2])
# print(a[3])
# print(a[-1])
# a = [2, 13, 123, 1, 312, 321, 421, 421, 412]
# print(a[2:])
# print(a[::-1])
# for i in a:
#     print(i, end=" ")

# for i in a:
#     if i % 2 == 0:
#         print(i, end=' ')

# print(len(a))
# a = []
# a.append(12)
# a.append('salom')
# # print(a)
# b = 0
# for i in range(1, 10+1):
#     a.append(i)
#     b.append(i)
#
# print(a)
# print(len(a))
# print(min(a))
# print(max(a))
# print(sum(a))
# a.append(12)
# print(a)
# print(a[::-1])
# # a.sort(reverse=False)
# print(a)
# a.reverse()
# print(a)

# g = []
# g.append('salom')
# g.append('Hello')
# g.append('Python')
# print(g)
#
# g.insert(0, 12)
# g.insert(2, 'Dasturchilar')
# print(g)
# a = [1, 2, 3]
# b = ['a', 'b', 'c']
# # print(b+a)
# a.extend(b)
# print(a)  # [1,2,3,a,b,c]
# b.extend(a)  # [a, b, c] + [1,2,3,a,b,c]
# print(b)

# a = [12, 45, 87, -98]
# h = [21, 35, 66, 5]
# d = a + h
# print(sum(d))
# d = a + h
# summa = 0
# for i in d:
#     summa += i
#
# print(summa)

# for i in range(len(d)):
#     summa += d[i]
# print(summa)


# a = [12, 45, 87, -98]
# h = [21, 35, 66, 5]
# print(a[1] + h[1])
# print(a[3] + h[3])

# a = [1, 2, 3, 42, 4, 2, 235, 2352]
# a.pop()
# a.pop()
# a.pop(1)
# print(a)
# a.remove(4)
# print(a)
# a.remove(42)
# print(a)
# # a.clear()
# # print(a)
# del a[0]
# print(a)
# del a
# print(a)

m = []
for i in range(1, 15 + 1):
    m.append(i)
# print(m)
# for i in m:
#     if i % 2 == 0:
#         m.remove(i)
# print(m)
# j = []
# for i in range(0, len(m)):
#     if m[i] % 2 != 0:
#         j.append(m[i])
# print(j)
#
# for i in m:
#     if i % 2 == 0:
#         m.remove(i)
# print(m)

a = [1, 2, 3]
b = a.copy()
# b = list(a)
b.append(12)
print(a)
print(b)
# b = a
# b.append(12)
# print(a)
# print(b)
