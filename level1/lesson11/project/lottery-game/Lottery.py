import time
import random
import os

xo_so_giai_hai_so = random.randint(10, 99)
xo_so_giai_ba_so = random.randint(100, 999)
xo_so_giai_bon_so = random.randint(1000, 9999)
xo_so_giai_nam_so = random.randint(10000, 99999)
xo_so_giai_sau_so = random.randint(100000, 999999)
black = lambda text: '\033[0;30m' + text + '\033[0m'
red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'
yellow = lambda text: '\033[0;33m' + text + '\033[0m'
blue = lambda text: '\033[0;34m' + text + '\033[0m'
magenta = lambda text: '\033[0;35m' + text + '\033[0m'
cyan = lambda text: '\033[0;36m' + text + '\033[0m'
white = lambda text: '\033[0;37m' + text + '\033[0m'
print(red("Hiện tại giải thưởng cao nhất(giải đặc biệt) đang là 1109,2503 tỷ(đủ loại mệnh giá)"))
print(yellow("Bạn muốn chơi loại xổ số gì nà?🤔🤔"))
print(cyan(""""
1,Xổ số miền Bắc
2,Xổ số miền Trung
3,Xổ số miền Nam
4,Xổ số nước Mỹ
5,Xổ số nước Anh
6,Xem các mức giải thưởng
"""))
while True:
    a = int(input("Nhập lựa chọn của bạn:"))
    if a == 1:
        b = input(
            "Nhập cơ cấu giải thưởng bạn muốn(có từ 2-6 số,tùy độ dài của số mà giải thưởng cũng tỉ lệ thuận theo):")
        b = int(b)
        if b == 1 or b == 0:
            print("Try hard tí đê!😡😡😡")
        elif b == 2:
            so_xo_so_hai = int(input("Nhập số xổ số :"))
            os.system('clear')
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_hai == xo_so_giai_hai_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 100.000 VNĐ 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        elif b == 3:
            so_xo_so_ba = int(input("Nhập số xổ số:"))
            os.system('clear')
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_ba == xo_so_giai_ba_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 100.000 VNĐ 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        elif b == 4:
            so_xo_so_bon = int(input("Nhập số xổ số:"))
            os.system('clear')
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_bon == xo_so_giai_bon_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 1.000.000 VNĐ 👏👏👏"))
            elif so_xo_so_bon >= xo_so_giai_bon_so - 100 and so_xo_so_bon <= xo_so_giai_bon_so + 100:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 400.000 VNĐ 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        elif b == 5:
            so_xo_so_nam = int(input("Nhập số xổ số:"))
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_nam == xo_so_giai_nam_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 30.000.000 VNĐ 👏👏👏"))
            elif so_xo_so_nam >= xo_so_giai_nam_so - 100 and xo_so_giai_nam_so <= xo_so_giai_nam_so + 100:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 15.000.000 VNĐ 👏👏👏"))
            elif so_xo_so_nam >= xo_so_giai_nam_so - 500 and xo_so_giai_nam_so <= xo_so_giai_nam_so + 500:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 10.000.000 VNĐ 👏👏👏"))
            elif so_xo_so_nam >= xo_so_giai_nam_so - 700 and xo_so_giai_nam_so <= xo_so_giai_nam_so + 700:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 3.000.000 VNĐ 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        elif b == 6:
            so_xo_so_sau = int(input("Nhập số xổ số:"))
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_sau == xo_so_giai_sau_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 2.000.000.000 VNĐ 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        else:
            for i in range(10):
                print(" " * i, "Error, trying to fix problems...")
                time.sleep(0.5)
                os.system('clear')
    elif a == 2:
        b = int(input(
            "Nhập cơ cấu giải thưởng bạn muốn(có từ 2-6 số,tùy độ dài của số mà giải thưởng cũng tỉ lệ thuận theo):"))
        if b == 1 or b == 0:
            print("Try hard tí đê!😡😡😡")
        elif b == 2:
            so_xo_so_hai = int(input("Nhập số xổ số :"))
            os.system('clear')
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_hai == xo_so_giai_hai_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 100.000 VNĐ 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        elif b == 3:
            so_xo_so_ba = int(input("Nhập số xổ số:"))
            os.system('clear')
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_ba == xo_so_giai_ba_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 100.000 VNĐ 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        elif b == 4:
            so_xo_so_bon = int(input("Nhập số xổ số:"))
            os.system('clear')
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_bon == xo_so_giai_bon_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 1.000.000 VNĐ 👏👏👏"))
            elif so_xo_so_bon >= xo_so_giai_bon_so - 100 and so_xo_so_bon <= xo_so_giai_bon_so + 100:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 400.000 VNĐ 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        elif b == 5:
            so_xo_so_nam = int(input("Nhập số xổ số:"))
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_nam == xo_so_giai_nam_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 30.000.000 VNĐ 👏👏👏"))
            elif so_xo_so_nam >= xo_so_giai_nam_so - 100 and xo_so_giai_nam_so <= xo_so_giai_nam_so + 100:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 15.000.000 VNĐ 👏👏👏"))
            elif so_xo_so_nam >= xo_so_giai_nam_so - 500 and xo_so_giai_nam_so <= xo_so_giai_nam_so + 500:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 10.000.000 VNĐ 👏👏👏"))
            elif so_xo_so_nam >= xo_so_giai_nam_so - 700 and xo_so_giai_nam_so <= xo_so_giai_nam_so + 700:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 3.000.000 VNĐ 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        elif b == 6:
            so_xo_so_sau = int(input("Nhập số xổ số:"))
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_sau == xo_so_giai_sau_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 2.000.000.000 VNĐ 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        else:
            for i in range(10):
                print(" " * i, "Error, trying to fix problems...")
                time.sleep(0.5)
                os.system('clear')
    elif a == 3:
        b = int(input(
            "Nhập cơ cấu giải thưởng bạn muốn(có từ 2-6 số,tùy độ dài của số mà giải thưởng cũng tỉ lệ thuận theo):"))
        if b == 1 or b == 0:
            print("Try hard tí đê!😡😡😡")
        elif b == 2:
            so_xo_so_hai = int(input("Nhập số xổ số :"))
            os.system('clear')
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_hai == xo_so_giai_hai_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 100.000 VNĐ 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        elif b == 3:
            so_xo_so_ba = int(input("Nhập số xổ số:"))
            os.system('clear')
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_ba == xo_so_giai_ba_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 100.000 VNĐ 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        elif b == 4:
            so_xo_so_bon = int(input("Nhập số xổ số:"))
            os.system('clear')
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_bon == xo_so_giai_bon_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 1.000.000 VNĐ 👏👏👏"))
            elif so_xo_so_bon >= xo_so_giai_bon_so - 100 and so_xo_so_bon <= xo_so_giai_bon_so + 100:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 400.000 VNĐ 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        elif b == 5:
            so_xo_so_nam = int(input("Nhập số xổ số:"))
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_nam == xo_so_giai_nam_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 30.000.000 VNĐ 👏👏👏"))
            elif so_xo_so_nam >= xo_so_giai_nam_so - 100 and xo_so_giai_nam_so <= xo_so_giai_nam_so + 100:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 15.000.000 VNĐ 👏👏👏"))
            elif so_xo_so_nam >= xo_so_giai_nam_so - 500 and xo_so_giai_nam_so <= xo_so_giai_nam_so + 500:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 10.000.000 VNĐ 👏👏👏"))
            elif so_xo_so_nam >= xo_so_giai_nam_so - 700 and xo_so_giai_nam_so <= xo_so_giai_nam_so + 700:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 3.000.000 VNĐ 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        elif b == 6:
            so_xo_so_sau = int(input("Nhập số xổ số:"))
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_sau == xo_so_giai_sau_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 2.000.000.000 VNĐ 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        else:
            for i in range(10):
                print(" " * i, "Error, trying to fix problems...")
                time.sleep(0.5)
                os.system('clear')
    elif a == 4:
        b = int(input(
            "Nhập cơ cấu giải thưởng bạn muốn(có từ 2-6 số,tùy độ dài của số mà giải thưởng cũng tỉ lệ thuận theo):"))
        if b == 1 or b == 0:
            print("Try hard tí đê!😡😡😡")
        elif b == 2:
            so_xo_so_hai = int(input("Nhập số xổ số :"))
            os.system('clear')
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_hai == xo_so_giai_hai_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 100.000 USD 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        elif b == 3:
            so_xo_so_ba = int(input("Nhập số xổ số:"))
            os.system('clear')
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_ba == xo_so_giai_ba_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 100.000 USD 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        elif b == 4:
            so_xo_so_bon = int(input("Nhập số xổ số:"))
            os.system('clear')
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_bon == xo_so_giai_bon_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 1.000.000 USD 👏👏👏"))
            elif so_xo_so_bon >= xo_so_giai_bon_so - 100 and so_xo_so_bon <= xo_so_giai_bon_so + 100:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 400.000 USD 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        elif b == 5:
            so_xo_so_nam = int(input("Nhập số xổ số:"))
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_nam == xo_so_giai_nam_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 30.000.000 USD 👏👏👏"))
            elif so_xo_so_nam >= xo_so_giai_nam_so - 100 and xo_so_giai_nam_so <= xo_so_giai_nam_so + 100:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 15.000.000 USD 👏👏👏"))
            elif so_xo_so_nam >= xo_so_giai_nam_so - 500 and xo_so_giai_nam_so <= xo_so_giai_nam_so + 500:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 10.000.000 USD 👏👏👏"))
            elif so_xo_so_nam >= xo_so_giai_nam_so - 700 and xo_so_giai_nam_so <= xo_so_giai_nam_so + 700:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 3.000.000 USD 👏👏👏"))
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        elif b == 6:
            so_xo_so_sau = int(input("Nhập số xổ số:"))
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_sau == xo_so_giai_sau_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 2.000.000.000 USD 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        else:
            for i in range(10):
                print(" " * i, "Error, trying to fix problems...")
                time.sleep(0.5)
                os.system('clear')
    elif a == 5:
        b = int(input(
            "Nhập cơ cấu giải thưởng bạn muốn(có từ 2-6 số,tùy độ dài của số mà giải thưởng cũng tỉ lệ thuận theo):"))
        if b == 1 or b == 0:
            print("Try hard tí đê!😡😡😡")
        elif b == 2:
            so_xo_so_hai = int(input("Nhập số xổ số :"))
            os.system('clear')
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_hai == xo_so_giai_hai_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 100.000 £ 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        elif b == 3:
            so_xo_so_ba = int(input("Nhập số xổ số:"))
            os.system('clear')
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_ba == xo_so_giai_ba_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 100.000 £ 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        elif b == 4:
            so_xo_so_bon = int(input("Nhập số xổ số:"))
            os.system('clear')
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_bon == xo_so_giai_bon_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 1.000.000 £ 👏👏👏"))
            elif so_xo_so_bon >= xo_so_giai_bon_so - 100 and so_xo_so_bon <= xo_so_giai_bon_so + 100:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 400.000 £ 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        elif b == 5:
            so_xo_so_nam = int(input("Nhập số xổ số:"))
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_nam == xo_so_giai_nam_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 30.000.000 £ 👏👏👏"))
            elif so_xo_so_nam >= xo_so_giai_nam_so - 100 and xo_so_giai_nam_so <= xo_so_giai_nam_so + 100:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 15.000.000 £ 👏👏👏"))
            elif so_xo_so_nam >= xo_so_giai_nam_so - 500 and xo_so_giai_nam_so <= xo_so_giai_nam_so + 500:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 10.000.000 £ 👏👏👏"))
            elif so_xo_so_nam >= xo_so_giai_nam_so - 700 and xo_so_giai_nam_so <= xo_so_giai_nam_so + 700:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 3.000.000 £ 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        elif b == 6:
            so_xo_so_sau = int(input("Nhập số xổ số:"))
            for i in range(10):
                print(" " * i, "Xổ số đang chờ,vui lòng đợi giây lát")
                time.sleep(0.5)
                os.system('clear')
            if so_xo_so_sau == xo_so_giai_sau_so:
                print(yellow("Uầy, chúc mừng bạn đã trúng giải, mệnh giá 2.000.000.000 £ 👏👏👏"))
            else:
                print("buồn ghê, bạn đã phí thời gian vô ích😥")
                print("thử lại đi")
        else:
            for i in range(10):
                print(" " * i, "Error, trying to fix problems...")
                time.sleep(0.5)
                os.system('clear')
    elif a == 6:
        print("""
    CƠ CẤU GIẢI THƯỞNG
    01,Giải đặc biệt	( 6 số ):2.000.000.000đ
    01,Giải nhất	( 5 số ):30.000.000đ
    01,Giải hai	( 5 số ):15.000.000đ
    02,Giải ba	( 5 số ):10.000.000đ
    07,Giải bốn	( 5 số ):3.000.000đ
    10,Giải năm	( 4 số ):1.000.000đ
    30,Giải sáu	( 4 số ):400.000đ
    100,Giải bảy	( 3 số ):200.000đ
    1.000,Giải tám	( 2 số ):100.000đ
    """)
    else:
        for i in range(10):
            print(" " * i, "Error, trying to fix problems...")
            time.sleep(0.5)
            os.system('clear')