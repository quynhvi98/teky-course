# ANS
# 1.
# a, 100
# b, infinity
# c, 0
# d, 0
# e, 1
# f, 100
# g, 300
# 6.
# The sum of first 9 integers:  1
# The sum of  2 number is: 1
# The sum of first 9 integers:  3
# The sum of  3 number is: 3
# The sum of first 9 integers:  6
# The sum of  4 number is: 6

n = int(input("Nhập n: "))
hello = 0
i = 1

while i <= n:
    hello = hello + i
    i = i+1

print("Tổng là", hello)

n = int(input("Nhập n: "))
hello = 0
i = 1

while i <= n:
    hello = hello + i
    i = i+2

print("Tổng là", hello)

done = False
n, m = 0, 100
while not done and n != m:
    n = eval(input())
    if n < 0:
        done = True
        break
        print("n =", n)

x = 100
while x > 0:
    y = eval(input())
    if y == 25:
        x += 1
        continue
        x = eval(input())
        print('x=', x)


