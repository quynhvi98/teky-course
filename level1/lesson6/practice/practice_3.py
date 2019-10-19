"""

Ví dụ về continue

    - Nhập vào số nguyên dương n

    - In ra các số tự nhiên

"""

# Nhập số n

n = int(input("Nhập số n="))

x = 1

while x:

    if x % 3 == 0:
        x += 1  # tăng x lên 1

        continue  # bắt đầu vòng lặp mới và không in

    print(x)

    x += 1

print("Kết thúc")

# =========================================================
