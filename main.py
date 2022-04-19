# def task_1():
#     s = '7' * 2022
#     while '777' in s or '333' in s:
#         s = s.replace('777', '3', 1)
#         s = s.replace('333', '7', 1)
#     print(s)


# def task_2():
#     def f(x, y, z, w):
#         return (x <= y) and ((not x) <= (not z)) or w
#
#     print("x y z w")
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 for w in range(2):
#                     if f(x, y, z, w) == 0:
#                         print(x, y, z, w)
#
# task_2()

# print(int('111', 2))
# def task_3():
#     x = 0
#     while True:
#         x += 1
#         x_bin = bin(x)[2:]
#         if x_bin[-1] == '0':
#             x_bin += '10'
#         else:
#             x_bin += '11'
#
#         if x_bin.count('1') % 2 == 0:
#             x_bin += '0'
#         else:
#             x_bin += '1'
#
#         if int(x_bin, 2) > 53:
#             print(x)
#             break
#
# task_3()
def task_4():
    s = 0
    while True:
        s += 1
        n = 200
        sc = s
        while sc > 0:
            sc = sc // 4
            n = n - 6

        if n == 170:
            print(s)
            break


# task_4()

# def task_10():
#     def to4(x):
#         s = ''
#         while x > 0:
#             s += str(x % 4)
#             x //= 4
#         return s[::-1]
#
#     s = 16 ** 23 + 4 ** 12 - 32 ** 6
#     print(to4(s).count('3'))
#
# task_10()

def f(x, y):
    if x == y:
        return 1
    elif x > y or x == 24:
        return 0
    else:
        return f(x + 1, y) + f(x * 3, y)


# print(f(2, 12) * f(12, 72))

def task_12():
    x = 0
    while True:
        x += 1
        xc = x
        L = 0
        M = 0
        while xc > 0:
            L = L + 1
            if M < (xc % 8):
                M = xc % 8
            xc = xc // 8
        if L == 4 and M == 7:
            print(x)
            break


# task_12()
def task_13():
    def deli(x, a):
        return not x % a

    def f(x, n):
        return (not deli(x, 54) or not deli(x, 80)) <= (not deli(x, n))

    A = 0
    while True:
        A += 1
        for x in range(1, 10000):
            if not f(x, A):
                break
        else:
            print(A)
            break


# task_13()

def task_14():
    data = list(map(int, open('14.txt').read().splitlines()))
    max_sum = 0
    count = 0
    for i in range(len(data)-1):
        if data[i] % 4 == 0 and data[i + 1] % 4 == 0:
            count += 1
            max_sum = max(max_sum, data[i] + data[i + 1])

    print(count, max_sum)

# task_14()
