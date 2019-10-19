print("Ví dụ về break")

# Tạo một biến x và gán giá trị 2 cho nó.

x = 2

while (x < 15) :

    print("----------------------\n")

    print("x = ", x)

    # Kiểm tra nếu x = 5 thì thoát ra khỏi vòng lặp.

    if (x == 5) :

        break

    # Tăng giá trị của x thêm 1

    x = x + 1

    print("x after + 1 = ", x)

print("Kết thúc")

#=========================================================



n = int(input("Nhập n="))
flag = True
x = 2
while x <= int(n / 2):
    if n % x == 0:
        flag = False
        break
    x += 1
if flag == True:
    print(n, "là số nguyên tố!")
else:
    print(n, "không là số nguyên tố")