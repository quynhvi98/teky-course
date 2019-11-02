import sys
import time

print("*"*33)
print("* PHẦN MỀM QUẢN LÝ ĐIỂM VER 1.0\t*")
print("* Create by: Nguyễn Văn A   \t*")
print("*"*33)
print("Nhấn phím: 1 để tiếp tục| nhấn phím:0 để thoát")

def avg(a, b, c):
    d = (a + b + c)/3;
    print("Tong cua 3 mon la:", float(d))
    if d >= 8:
        print("Bạn học rất tốt. Đạt học sinh giỏi")
    if d >= 9:
        print("Bạn rất xuất sắc")
    if d >= 7 and d <8:
        print("Bạn học khá")
    if d >=5 and d<7:
        print("Bạn học trung bình")
    if d <5:
        print("Bạn học kém ")
    menu()

def menu():
    a = int(input("Moi ban nhap so a:"))
    b = int(input("Moi ban nhap so b:"))
    c = int(input("Moi ban nhap so c:"))
    choice = input(
        """
        1. Tính điểm tổng kết trung bình 3 môn.
        0. Quit
        """)
    if choice == '1':
        avg(a, b, c)
    elif choice == '0':
        print("Đang thoát...")
        time.sleep(1)
        sys.exit()
menu()

