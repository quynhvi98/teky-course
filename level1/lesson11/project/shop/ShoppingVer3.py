a=b=c=d=e=f=g=h=i=k=10
tongtien=0
hoadon=""
doanhthu=0
danh_sach_san_pham = """1.Sách lập trình Python  |10 quyển | 100000/quyển
2.Sách lập trình Scratch |10 quyển |  20000/quyển
3.Sách lập trình Java    |10 quyển | 150000/quyển
4.Sách van               |10 quyển | 140000/quyển
5.Sách tieng anh         |10 quyển | 200000/quyển
6.Sách gdcd              |10 quyển |  10000/quyển
7.Sách hoa               |10 quyển | 350000/quyển
8.Sách sinh              |10 quyển |  90000/quyển
9.Sách li                |10 quyển |  85000/quyển
10.Sách toan             |10 quyển |  63000/quyển
"""
print("**Phần mềm bán hàng của Quốc Bảo**")
print(" < qb shop >")

tien=0

while True:
    ten=input('ten ban la j')
    tongtien=0
    hoadon="Hoa don cua " +ten + ": "
    if ten=='0':
        print("Thank you for shopping")
        break
    else :
        print("Chúng tôi có bán :")
        print(danh_sach_san_pham)
        while True:
            sanpham=(input('nhap san pham m muon mua'))
            if sanpham=='0':
                print('------')
                print(hoadon)
                print('tong tien la:',tongtien)
                print('------')
                doanhthu+=tongtien
                break
            elif sanpham=="1":
                baonhieu=int(input('ban mua bao nhieu python '))
                hoadon=hoadon+'\n'+ str(baonhieu) +'sach python:'+str(baonhieu*100000)
                tongtien+=baonhieu*100000
                a-=baonhieu
            elif sanpham=="2":
                baonhieu=int(input('ban mua bao nhieu scratch'))
                hoadon=hoadon+'\n'+ str(baonhieu) +'sach scratch:'+str(baonhieu*20000)
                tongtien+=baonhieu*20000
                b-=baonhieu
            elif sanpham=="3":
                baonhieu=int(input('ban mua bao nhieu java'))
                hoadon=hoadon+'\n'+ str(baonhieu) +'sach java:'+str(baonhieu*150000)
                tongtien+=baonhieu*150000
                c-=baonhieu
            elif sanpham=="4":
                baonhieu=int(input('ban mua bao nhieu van '))
                hoadon=hoadon+'\n'+ str(baonhieu) +'sach van:'+str(baonhieu*140000)
                tongtien+=baonhieu*140000
                d-=baonhieu
            elif sanpham=="5":
                baonhieu=int(input('ban mua bao nhieu tieng anh'))
                hoadon=hoadon+'\n'+ str(baonhieu) +'sach tieng anh:'+str(baonhieu*200000)
                tongtien+=baonhieu*200000
                e-=baonhieu
            elif sanpham=="6":
                baonhieu=int(input('ban mua bao nhieu gdcd'))
                hoadon=hoadon+'\n'+ str(baonhieu) +'sach gdcd:'+str(baonhieu*10000)
                tongtien+=baonhieu*10000
                f-=baonhieu
            elif sanpham=="7":
                baonhieu=int(input('ban mua bao nhieu hoa'))
                hoadon=hoadon+'\n'+ str(baonhieu) +'sach hoa:'+str(baonhieu*350000)
                tongtien+=baonhieu*350000
                g-=baonhieu
            elif sanpham=="8":
                baonhieu=int(input('ban mua bao nhieu sinh '))
                hoadon=hoadon+'\n'+ str(baonhieu) +'sach sinh:'+str(baonhieu*90000)
                tongtien+=baonhieu*90000
                h-=baonhieu
            elif sanpham=="9":
                baonhieu=int(input('ban mua bao nhieu li'))
                hoadon=hoadon+'\n'+ str(baonhieu) +'sach li:'+str(baonhieu*85000)
                tongtien+=baonhieu*85000
                i-=baonhieu
            elif sanpham=="10":
                baonhieu=int(input('ban mua bao nhieu toan'))
                hoadon=hoadon+'\n'+ str(baonhieu) +'sach toan:'+str(baonhieu*63000)
                tongtien+=baonhieu*63000
                k-=baonhieu
            else:
                print('chung toi ko ban sp do . moi ban nhap lai !!! ')
print(doanhthu)
print( """Shop da ban duoc
1.Sách lập trình Python  |{} quyển | 100000/quyển
2.Sách lập trình Scratch |{} quyển |  20000/quyển
3.Sách lập trình Java    |{} quyển | 150000/quyển
4.Sách van               |{} quyển | 140000/quyển
5.Sách tieng anh         |{} quyển | 200000/quyển
6.Sách gdcd              |{} quyển |  10000/quyển
7.Sách hoa               |{} quyển | 350000/quyển
8.Sách sinh              |{} quyển |  90000/quyển
9.Sách li                |{} quyển |  85000/quyển
10.Sách toan             |{} quyển |  63000/quyển
""".format(10-a,10-b,10-c,10-d,10-e,10-f,10-g,10-h,10-i,10-k))
intk= min(a,b,c,d,e,f,g,h,i,k)
if intk==a :
    print("""ban chay nhat:
Sách lập trình Python  |{} quyển |
""".format(10-intk))
    if 10-a<=baonhieu:
        print('chung toi da het sach r.moi ban mua sp khac !')
