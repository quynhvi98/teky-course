print("Chao mung ban den voi shop ADC book")
print("Chung toi ban nhieu loai sach, chat luong bthuong")
doanh_thu = 0
while True:
    name = input("Ban ten gi?")
    print("Chao " + name)
    if (name == '0'):
        break
    print("""
        1. Sach toan – 10000VND
        2. Sach van – 10000VND
        3. Sach CN – 10000VND
        4. Sach CD – 10000VND
        5. Sach TA – 13000VND
        6. Sach sinh hoc – 10000VND
        7. Sach hoa hoc – 10000VND
        8. Sach lich su – 10000VND
        9. Sach dia – 10000VND
        10. Sach am nhac va my thuat – 10000VND
        """)
    hoa_don = ""
    tong_tien_hoa_don = 0
    while True:
        mua = input("ban muon mua gi?")
        if (mua == '0'):
            print(hoa_don)
            print("tong : ", tong_tien_hoa_don)
            tong_tien_hoa_don = 0
            break
        if mua == '1':
            so_luong = int(input("mua bao nhieu cai"))
            print(so_luong, 'sach toan : ', so_luong * 10000)
            tong_tien_hoa_don = tong_tien_hoa_don + so_luong * 10000
            hoa_don += str(so_luong) + "sach toan"
            hoa_don += "=" + str(so_luong * 10000)
            hoa_don += "\n"
            doanh_thu = doanh_thu + so_luong * 10000
        if mua == '2':
            so_luong = int(input("mua bao nhieu cai"))
            print(so_luong, 'sach van : ', so_luong * 10000)
            tong_tien_hoa_don = tong_tien_hoa_don + so_luong * 10000
            hoa_don += str(so_luong) + "sach van"
            hoa_don += "=" + str(so_luong * 10000)
            hoa_don += "\n"
            doanh_thu = doanh_thu + so_luong * 10000
        if mua == '3':
            so_luong = int(input("mua bao nhieu cai"))
            print(so_luong, 'sach CN : ', so_luong * 10000)
            tong_tien_hoa_don = tong_tien_hoa_don + so_luong * 10000
            hoa_don += str(so_luong) + "sach CN"
            hoa_don += "=" + str(so_luong * 10000)
            hoa_don += "\n"
            doanh_thu = doanh_thu + so_luong * 10000
        if mua == '4':
            so_luong = int(input("mua bao nhieu cai"))
            print(so_luong, 'sach CD : ', so_luong * 10000)
            tong_tien_hoa_don = tong_tien_hoa_don + so_luong * 10000
            hoa_don += str(so_luong) + "sach CD"
            hoa_don += "=" + str(so_luong * 10000)
            hoa_don += "\n"
            doanh_thu = doanh_thu + so_luong * 10000
        if mua == '5':
            so_luong = int(input("mua bao nhieu cai"))
            print(so_luong, 'sach TA : ', so_luong * 13000)
            tong_tien_hoa_don = tong_tien_hoa_don + so_luong * 13000
            hoa_don += str(so_luong) + "sach TA"
            hoa_don += "=" + str(so_luong * 13000)
            hoa_don += "\n"
            doanh_thu = doanh_thu + so_luong * 13000
        if mua == '6':
            so_luong = int(input("mua bao nhieu cai"))
            print(so_luong, 'sach sinh hoc : ', so_luong * 10000)
            tong_tien_hoa_don = tong_tien_hoa_don + so_luong * 10000
            hoa_don += str(so_luong) + "sach sinh hoc"
            hoa_don += "=" + str(so_luong * 10000)
            hoa_don += "\n"
            doanh_thu = doanh_thu + so_luong * 10000
        if mua == '7':
            so_luong = int(input("mua bao nhieu cai"))
            print(so_luong, 'sach hoa hoc : ', so_luong * 10000)
            tong_tien_hoa_don = tong_tien_hoa_don + so_luong * 10000
            hoa_don += str(so_luong) + "sach hoa hoc"
            hoa_don += "=" + str(so_luong * 10000)
            hoa_don += "\n"
            doanh_thu = doanh_thu + so_luong * 10000
        if mua == '8':
            so_luong = int(input("mua bao nhieu cai"))
            print(so_luong, 'sach lich su : ', so_luong * 10000)
            tong_tien_hoa_don = tong_tien_hoa_don + so_luong * 10000
            hoa_don += str(so_luong) + "sach lich su"
            hoa_don += "=" + str(so_luong * 10000)
            hoa_don += "\n"
            doanh_thu = doanh_thu + so_luong * 10000
        if mua == '9':
            so_luong = int(input("mua bao nhieu cai"))
            print(so_luong, 'sach dia : ', so_luong * 10000)
            tong_tien_hoa_don = tong_tien_hoa_don + so_luong * 10000
            hoa_don += str(so_luong) + "sach dia"
            hoa_don += "=" + str(so_luong * 10000)
            hoa_don += "\n"
            doanh_thu = doanh_thu + so_luong * 10000
        if mua == '10':
            so_luong = int(input("mua bao nhieu cai"))
            print(so_luong, 'sach am nhac va my thuat : ', so_luong * 10000)
            tong_tien_hoa_don = tong_tien_hoa_don + so_luong * 10000
            hoa_don += str(so_luong) + "sach am nhac va my thuat"
            hoa_don += "=" + str(so_luong * 10000)
            hoa_don += "\n"
            doanh_thu = doanh_thu + so_luong * 10000
print("Tong doanh thu la ", doanh_thu)
print("Tam biet")

