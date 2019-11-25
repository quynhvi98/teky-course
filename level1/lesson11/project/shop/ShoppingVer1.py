cyan = lambda text: '\033[0;36m' + text + '\033[0m'
intro = "Chào mừng bạn đến với shop của tôi,shop của tôi  bán điện thoại và dụng cụ máy tính"
menu = """
1. Danh sách sản phẩm
2. Chọn sản phẩm và thanh toán
0. Exit

"""
chao_tam_biet = "Chào bạn chúc bạn vui vẻ,bạn có ý kiến gì cho shop của tôi tốt hơn không ? "

print(intro)
tong_gia = 0
hoadon = ""
list_sp = [
    ["1.Điện thoại samsung S8 18000VND", 18000000],
    ["2.Iphone XS 23000VND", 23000000],
    ["3.Iphone 7 Plus 20000VND", 20000000],
    ["4.Oppo S7 19000VND", 19000000],
    ["5.Laptop Win 10 15000VND", 15000000]]
while True:
    print(cyan(menu))
    yc = input("Nhập yêu cầu  :")
    if yc == '0':
        print("Chào bạn chúc bạn vui vẻ,bạn có ý kiến gì cho shop của tôi tốt hơn không ? ")
        break
    if yc == '1':
        for sp in list_sp:
            print(sp[0])
    if yc == '2':
        for sp in list_sp:
            print(sp[0])
        thanh_toan = 0
        while True:
            mua = int(input("Bạn muốn mua sản phẩm thứ bao nhiêu ? "))
            soluong = int(input("Bạn muốn mua bao nhiêu? "))
            muon_thanh_toan = input("Bạn có muốn thanh toán không (y/n)")
            thanh_toan = thanh_toan + list_sp[mua - 1][1] * (soluong)
            hoadon += "\n {: <35} - {: >10} * {: >2} = {:>11}".format(list_sp[mua - 1][0], list_sp[mua - 1][1], soluong,
                                                                      list_sp[mua - 1][1] * (soluong))
            if muon_thanh_toan == "y":
                break
        print("=================")
        print("=====Hóa đơn=====")
        print(hoadon)
        print("=================")
        print("Bạn đã mua thành công, số tiền bạn cần phải trả là {}VND".format(thanh_toan))
