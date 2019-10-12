n = int(input("Nhập n: "))  # Nhập số n tùy ý
s = 0  # khai báo và gán giá trị cho tong
i = 1  # khai báo và gán giá trị cho biến đếm i

while i <= n:
    if i % 2 == 1:
        s = s + i
        i = i + 2  # cập nhật biến đếm
print("Tổng là", s)
