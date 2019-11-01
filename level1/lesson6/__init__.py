"""
Yêu cầu: Viết chương trình Python thực hiện các công việc sau:
-   Nhập vào số nguyên dương n
-   Kiểm tra số n có phải là số nguyên tố không
"""

n = int(input("Nhập n="))
flag = True
x = 2
while x <= int(n / 2):
    if n % x == 0:
        flag = False
        break
    x += 1
if flag:
    print(n, "là số nguyên tố!")
else:
    print(n, "không là số nguyên tố")
