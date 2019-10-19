"""
Yêu cầu: Viết chương trình Python thực hiện các công việc sau:
-   Nhập vào số nguyên dương n
-   Kiểm tra số n có phải là số nguyên tố không
"""
# Nhập số nguyên n
n = int(input("Nhập n="))
flag = True  # Giả sử n là số nguyên tố
# Tìm xem có số x nào mà x là ước của n không?
# Nếu có số x là ước của n thì => n không là nguyên tố
x = 2  # khởi tạo biến lặp
while x <= int(n / 2):
    if n % x == 0:  # lúc này x là ước
        flag = False
        break
    x += 1  # Tăng biến lặp
if flag == True:
    print(n, "là số nguyên tố!")
else:
    print(n, "không là số nguyên tố")