"""

Yêu cầu: Viết chương trình Python thực công việc sau:

-   Nhập vào số nguyên n

-   In ra các số

"""

# Nhập số nguyên n

n = int(input("Nhập n="))

i = 0

tong = 0

while i:

    if i % 3 == 0 or i % 5 == 0:
        tong += i

        print(i)

    i += 1

# Tổng

print("Tổng các số chia hết cho 3 hoặc 5:", tong)

# =========================================================
