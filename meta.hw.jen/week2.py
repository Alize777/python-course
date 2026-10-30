#  №A.        является ли данный год високосным.
# year = int(input())
# if year % 400 == 0:
#     print("YES")
# elif year % 100 == 0:
#     print("NO")
# elif year % 4 == 0:
#     print("YES")
# else:
#     print("NO")





# №2 B. {ладья}
# x1 = int(input())
# y1 = int(input())

# x2 = int(input())
# y2 = int(input())

# if x1 == x2 or y1 == y2:
#     print("YES")
# else:
#     print("NO")




# №С слон.
# x1 = int(input())
# y1 = int(input())

# x2 = int(input())
# y2 = int(input())


# if abs(x1 - x2) == abs(y1 - y2):
#     print("YES")
# else:
#     print("NO")







# Задача №256. Ферзь
x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())


if (x1 != x2 or y1 != y2) and (x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)):
    print("YES")
else:
    print("NO")







# Задача №257. Конь
# x1 = int(input())
# y1 = int(input())


# x2 = int(input())
# y2 = int(input())

# if abs(x1 - x2) / abs(y1 - y2) == 2:
#     print("yes")
# else:
#     print("nooo")




# Задача №258. Шоколадка
n, m, k = map(int, input().split())

if k % n == 0 or k % m == 0:
    print("YES")
else:
    print("NO")



# фишки  №259

n = int(input())

if n >= 4 and n % 4 == 0:
    print("YES")
else:
    print("NO")


# №260 уравнение

a, b = map(int, input().split())

if a == 0:
    if b == 0:
        print("INF")
    else:
        print("NO")
elif -b % a == 0:
    print(-b // a)
else:
    print("NO")




# № сложно уравнение
a, b, c, d = map(int, input().split())

if a == 0:
    if b == 0:
        print("INF")
    else:
        print("NO")
elif (-b) % a != 0:
    print("NO")
else:
    x = -b // a

    if c * x + d == 0:
        print("NO")
    else:
        print(x)






# № сдача

a, b, c, d = map(int, input().split())

price = a * 100 + b
paid = c * 100 + d

change = paid - price

print(change // 100, change % 100)



# № мороженое

k = int(input())

if k >= 3 and (k % 3 == 0 or k % 5 == 0 or k >= 8):
    print("YES")
else:
    print("NO")






# № котлеты

k, m, n = map(int, input().split())

if n <= k:
    print(2 * m)
else:
    print((2 * n * m + k - 1) // k)


# № координатные точки

x1, y1, x2, y2 = map(int, input().split())

if (x1 > 0 and x2 > 0 or x1 < 0 and x2 < 0) and (y1 > 0 and y2 > 0 or y1 < 0 and y2 < 0):
    print("YES")
else:
    print("NO")





# № максимум из двух чискл
a = int(input())
b = int(input())

print(max(a, b))




# № макс из 3 чисел

a = int(input())
b = int(input())
c = int(input())

print(max(a, b, c))



# №существует ли треугольник

a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")





# № количество равных из 3

a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(0)





# №ход короля

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if abs(a - c) <= 1 and abs(b - d) <= 1:
    print("YES")
else:
    print("NO")



# № квадратное уравнение

import math

a, b, c = map(float, input().split())

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(x1, x2)
elif D == 0:
    x = -b / (2 * a)
    print(x)



# № тип треугольника

a, b, c = map(int, input().split())

x, y, z = sorted([a, b, c])

if x + y <= z:
    print("impossible")
elif x ** 2 + y ** 2 == z ** 2:
    print("right")
elif x ** 2 + y ** 2 > z ** 2:
    print("acute")
else:
    print("obtuse")





# № коровы

n = int(input())

if n % 10 == 1 and n != 11:
    print(n, "korova")
elif n % 10 in [2, 3, 4] and n not in [12, 13, 14]:
    print(n, "korovy")
else:
    print(n, "korov")


# № билеты на метро
n = int(input())

best = float('inf')
answer = (0, 0, 0)

for sixty in range(n // 60 + 2):
    for ten in range(n // 10 + 2):
        one = max(0, n - sixty * 60 - ten * 10)
        cost = sixty * 440 + ten * 125 + one * 15

        if cost < best:
            best = cost
            answer = (one, ten, sixty)

print(*answer)



# № билеты на метро -2
n = int(input())

tickets = [1, 5, 10, 20, 60]
prices = [15, 70, 125, 230, 440]

limit = n + 59

dp = [float('inf')] * (limit + 1)
dp[0] = 0

prev = [0] * (limit + 1)

for i in range(1, limit + 1):
    for j in range(5):
        if i >= tickets[j]:
            cost = dp[i - tickets[j]] + prices[j]

            if cost < dp[i]:
                dp[i] = cost
                prev[i] = j

best = min(range(n, limit + 1), key=lambda x: (dp[x], -x))

answer = [0] * 5

while best > 0:
    j = prev[best]
    answer[j] += 1
    best -= tickets[j]

print(*answer)




# № координаты соседей
m, n, x, y = map(int, input().split())

if y > 1:
    print(x, y - 1, end=" ")

if x > 1:
    print(x - 1, y, end=" ")

if y < n:
    print(x, y + 1, end=" ")

if x < m:
    print(x + 1, y)


# № апельсины бочками
n = int(input())

if n % 10 == 1 and n % 100 != 11:
    print(n, "bochka")
elif n % 10 in [2, 3, 4] and n % 100 not in [12, 13, 14]:
    print(n, "bochki")
else:
    print(n, "bochek")



# № четные и нечетные числа

a, b, c = map(int, input().split())

if (a % 2 == 0 or b % 2 == 0 or c % 2 == 0) and (a % 2 != 0 or b % 2 != 0 or c % 2 != 0):
    print("YES")
else:
    print("NO")



# № римская система числения

x = int(input())

values = [
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
]

result = ""

for value, symbol in values:
    while x >= value:
        result += symbol
        x -= value

print(result)


# № знак числа
x = int(input())

if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)






# №
a, b = map(int, input().split())

if (a == 1 and b == 1) or (a != 1 and b != 1):
    print("YES")
else:
    print("NO")



# тест система..
a, b = map(int, input().split())

if (a == 1 and b == 1) or (a != 1 and b != 1):
    print("YES")
else:
    print("NO")




 # № 2961 упорядочить число
a = int(input())
b = int(input())
c = int(input())

x = sorted([a, b, c])

print(x[0], x[1], x[2])