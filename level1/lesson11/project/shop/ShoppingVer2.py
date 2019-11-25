black = lambda text: '\033[0;30m' + text + '\033[0m'
red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'
yellow = lambda text: '\033[0;33m' + text + '\033[0m'
blue = lambda text: '\033[0;34m' + text + '\033[0m'
magenta = lambda text: '\033[0;35m' + text + '\033[0m'
cyan = lambda text: '\033[0;36m' + text + '\033[0m'
white = lambda text: '\033[0;37m' + text + '\033[0m'
intro = "Chào mừng đến với shop của tôi"
menu = """
=== Mua hàng
1. Xem danh sách sản phẩm
2. Chọn sản phẩm
3. Xem hóa đơn của tôi
4. Thanh toán
==== Quản lý shop
5. Xem doanh thu
6. Xem lợi nhuận
====
0. Exit 
"""
chao_tam_biet = "Chao ban chuc ban vui ve , ban co feedback cho phan mem cua toi ve email huyhuy17@gmail.com"
ds_sp = [
    ["1. Kẹo mút", 1000, 20],
    ["2. Bim bim tonies", 5000, 20],
    ["3. Mỳ tôm hỏ hảo", 10000, 20],
    ["4. Xúc xích thịt lợn", 5000, 20],
    ["5. Xúc xích thịt ga", 10000, 20],
    ["6. Cháo ăn liền:", 20000, 20],
    ["7. Dầu gội pantin", 20000, 20],
    ["8. Bóng:", 300000, 20],
    ["9. Trà chanh:", 5000, 20],
    ["10. Trà đá:", 3000, 20],
    ["11. Máy cạo đầu:", 200000, 20],
    ["12. Máy cạo râu:", 200000, 20],
]
doanhthu = 0
margin = 0.7
print(intro)
hoadon = ""
while True:
    print(cyan(menu))
    yc = input("Nhap yc  :")
    if yc == '0':
        break
    if yc == '3':
        print("Hóa đơn của bạn là \n")
        print("\n***********************************")
        print("               Hóa đơn             ")
        print("***********************************")
        print(hoadon)
        print("***********************************")
    if yc == '1':
        print("Mời bạn xem menu của chúng tôi")
        for sp in ds_sp:
            print("{: <20} : {: >6}VN".format(sp[0], sp[1]))
    if yc == '2':
        buy = int(input(red("Bạn muốn mua gì: ")))
        amount = int(input(red("Bạn muốn mua bao nhiêu: ")))
        gia = ds_sp[buy][1]
        hoadon = hoadon + "\n{}  {}    x    {}  =    {} VNĐ".format(ds_sp[buy - 1][0], ds_sp[buy - 1][1], amount,
                                                                    amount * gia)
        doanhthu += amount * gia
    if yc == '4':
        print("Hóa đơn của bạn: \n")
        print("\n***********************************")
        print("               Hóa đơn             ")
        print("***********************************")
        print(hoadon)
        print("***********************************")
        print(green("Bạn đã thanh toán thành công!"))
        hoadon = ""
    if yc == '5':
        print("Doanh thu của cửa hàng là : {}".format(doanhthu))
    if yc == '6':
        print("Lợi nhuận của cửa hàng là : {}".format(doanhthu * (1 - margin)))
    input("Enter to next")
