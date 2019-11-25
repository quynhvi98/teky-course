black = lambda text: '\033[0;30m' + text + '\033[0m'
red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'
yellow = lambda text: '\033[0;33m' + text + '\033[0m'
blue = lambda text: '\033[0;34m' + text + '\033[0m'
magenta = lambda text: '\033[0;35m' + text + '\033[0m'
cyan = lambda text: '\033[0;36m' + text + '\033[0m'
white = lambda text: '\033[0;37m' + text + '\033[0m'
intro = "Chào mừng đến với cửa hàng điện tử của tôi"
cyan = lambda text: '\033[0;36m' + text + '\033[0m'
print("(Lưu ý : Một khi đã đặt tên bạn sẽ không đổi được nữa, hãy suy nghĩ cẩn thận)")
print(cyan("-----------------------------------------------------------"))
print(cyan("                       THẺ KHÁCH HÀNG"))
print(cyan(" __________"))
name = input(cyan("|          |  Tên khách hàng : Carl (Điền tên bạn) "))
print(cyan("|          |"))
print(cyan("|  ( ◠‿◠ ) |  Lớp : SNLT1"))
print(cyan("|          |"))
print(cyan("|          |  HỌC VIỆN TEKY"))
print(cyan("|__________|"))
print(cyan("-----------------------------------------------------------"))

menu = """
=== Mua hàng
1. Xem danh sách sản phẩm
2. Chọn sản phẩm
3. Xem hóa đơn của tôi
4. Nhập mã khuyến mãi
5. Thanh toán
==== Quản lý shop
6. Xem doanh thu
7. Xem lợi nhuận
====
0. Exit 
"""
good_bye  = "Chao ban chuc ban vui ve , ban co feedback cho phan mem cua toi ve email vi.quynh@gmail.com"

print(intro)
while True :
  print(yellow(menu))
  yc = input("Nhap yc  :")
  if yc == '0':
    break
  if yc == '1':
   print("menu 1")
  input()
print(good_bye)