import sys
import time
import datetime

def checkYear(y):
    if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0):
        return True
    else:
        return False


def checkMonth(m):
    if m < 1 or m > 12:
        return False
    else:
        return True


def checkDay(y, m, d):
    m30 = [4, 6, 9, 11]
    m31 = [1, 3, 5, 7, 8, 10, 12]
    kt = True
    if m in m30:
        if d > 30 or d < 1:
            kt = False
        elif m in m31:
            if d > 31 or d < 1:
                kt = False
        else:
            if checkYear(y):
                if d > 29 or d < 1:
                    kt = False
            else:
                if d > 28 or d < 1:
                    kt = False
        return kt


def BMI():
    weight = float(input('Cân nặng của bạn(kg): '))
    height = float(input('Chiều cao của bạn(cm): '))
    height /= 100
    bmi = weight / (height ** 2)
    print('Chỉ số BMI của bạn là: {0} và bạn đang: '.format(bmi), end='')
    if (bmi < 16):
        print("Gầy độ III")
    elif (bmi < 17):
        print("Gầy độ II")
    elif (bmi < 18.5):
        print("Gầy độ I")
    elif (bmi < 30):
        print("Thừa cân")
    elif (bmi < 35):
        print("Béo phì độ I")
    elif (bmi < 40):
        print("Béo phì độ II")
    else:
        print("Béo phì độ III")
    time.sleep(3)
    menu()

def Thoigian():
    print("Mời bạn nhập ngày bắt đầu: ")
    y1 = int(input("Mời bạn nhập năm bắt đầu: "))
    m1 = int(input("Mời bạn nhập tháng bắt đầu: "))
    while checkMonth(m1) == False:
        print("Tháng không hợp lệ!")
        m1 = int(input("Mời bạn nhập lại tháng bắt đầu: "))
    d1 = int(input('Mời bạn nhập ngày bắt đầu: '))
    while checkDay(y1, m1, d1) == False:
        print('Ngày không hợp lệ!')
        d1 = int(input("Mời bạn nhập lại ngày bắt đầu: "))
    date1 = datetime.date(y1, m1, d1)
    print('\nNhập ngày kết thúc:')
    y2 = int(input('Mời bạn nhập năm kết thúc: '))
    m2 = int(input('Mời bạn nhập tháng kết thúc: '))
    while checkMonth(m2) == False:
        print("Tháng không hợp lệ!")
        m2 = int(input("Mời bạn nhập lại tháng kết thúc: "))
    d2 = int(input('Mời bạn nhập ngày kết thúc: '))
    while checkDay(y2, m2, d2) == False:
        print('Ngày không hợp lệ!')
        d2 = int(input("Mời bạn nhập lại ngày kết thúc: "))
    date2 = datetime.date(y2, m2, d2)
    songay = date2 - date1
    print('Số ngày là: ', songay.days)
    time.sleep(3)
    menu()


def Tuoi():
    print("Mời bạn nhập ngày sinh: ")
    y1 = int(input("Mời bạn nhập năm sinh: "))
    m1 = int(input("Mời bạn nhập tháng sinh: "))
    while checkMonth(m1) == False:
        print("Tháng không hợp lệ!")
        m1 = int(input("Mời bạn nhập lại tháng sinh: "))
    d1 = int(input('Mời bạn nhập ngày sinh: '))
    while checkDay(y1, m1, d1) == False:
        print('Ngày không hợp lệ!')
        d1 = int(input("Mời bạn nhập lại ngày sinh: "))
    date_of_birth1 = str(m1) + '/' + str(d1) + '/' + str(y1)
    date_of_birth = datetime.datetime.strptime(date_of_birth1, '%m/%d/%Y')
    current_date = datetime.datetime.now()
    daysLeft = date_of_birth - current_date
    years = ((daysLeft.total_seconds()) / (365.242 * 24 * 3600))
    yearsInt = int(years)
    months = (years - yearsInt) * 12
    monthsInt = int(months)
    days = (months - monthsInt) * (365.242 / 12)
    daysInt = int(days)
    hours = (days - daysInt) * 24
    hoursInt = int(hours)
    minutes = (hours - hoursInt) * 60
    minutesInt = int(minutes)
    seconds = (minutes - minutesInt) * 60
    secondsInt = int(seconds)
    print('Bạn đã sống {0:d} năm, {1:d}  tháng, {2:d}  ngày, {3:d}  giờ, {4:d} phút, {5:d} giây.'.format(- yearsInt,
                                                                                                         - monthsInt,
                                                                                                         - daysInt,
                                                                                                         - hoursInt,
                                                                                                         - minutesInt,
                                                                                                         - secondsInt))
    time.sleep(3)
    menu()


def Tocdo():
    dlnhap = input('Đại lượng nhập vào (km/h, m/s, ips, mile per second) \nYêu cầu nhập chính xác tên đại lượng: ')
    slnhap = float(input('Chỉ số nhập vào: '))
    if dlnhap == 'km/h':
        sl = slnhap * 1000 / 3600
    if dlnhap == 'ips':
        sl = slnhap * 0.0254
    if dlnhap == 'mile per second':
        sl = slnhap * 1609.344
    dlxuat = input(
        'Đại lượng muốn chuyển đổi(km/h, m/s, ips, mile per second) \nYêu cầu nhập chính xác tên đại lượng: ')
    if dlxuat == 'km/h':
        slxuat = sl * 3.6
    elif dlxuat == 'ips':
        slxuat = sl * 39.3701
    elif dlxuat == 'mile per second':
        slxuat = sl * 0.000621371
    else:
        slxuat = sl
    print(slnhap, dlnhap, "=", slxuat, dlxuat)
    time.sleep(3)
    menu()


def Khoiluong():
    dlnhap = input('Đại lượng nhập vào (cg,mg,dg,g,dag,hg,kg)\nYêu cầu nhập chính xác tên đại lượng: ')
    slnhap = float(input('Chỉ số nhập vào: '))
    if dlnhap == 'kg':
        sl = slnhap * (1000000)
    if dlnhap == 'hg':
        sl = slnhap * (100000)
    if dlnhap == 'dag':
        sl = slhap * (10000)
    if dlnhap == 'g':
        sl = slnhap * (1000)
    if dlnhap == 'dg':
        sl = slnhap * (100)
    if dlnhap == 'cg':
        sl = slnhap * (10)
    dlxuat = input('Đại lượng muốn chuyển đổi(cg,mg,dg,g,dag,hg,kg)\nYêu cầu nhập chính xác tên đại lượng: ')
    if dlxuat == 'kg':
        slxuat = sl * 1000000
    elif dlxuat == 'hg':
        slxuat = sl * 100000
    elif dlxuat == 'dag':
        slxuat = sl * 10000
    elif dlxuat == 'g':
        slxuat = sl * 1000
    elif dlxuat == 'dg':
        slxuat = sl * 100
    elif dlxuat == 'cg':
        slxuat = sl * 10
    else:
        slxuat = sl
    print(slnhap, dlnhap, '=', slxuat, dlxuat)
    time.sleep(3)
    menu()


def Thetich():
    dlnhap = input('Đại lượng nhập vào(cm3,mm3,dm3,m3,dam3,hm,km3)\nYêu cầu nhập chính xác tên đại lượng: ')
    slnhap = float(input('Chỉ số nhập vào: '))
    if dlnhap == 'km3':
        sl = slnhap * (1000000) ** 3
    if dlnhap == 'hm3':
        sl = slnhap * (100000) ** 3
    if dlnhap == 'dam3':
        sl = slhap * (10000) ** 3
    if dlnhap == 'm3':
        sl = slnhap * (1000) ** 3
    if dlnhap == 'dm3':
        sl = slnhap * (100) ** 3
    if dlnhap == 'cm3':
        sl = slnhap * (10) ** 3
    dlxuat = input('Đại lượng muốn chuyển đổi(cm3,mm3,dm3,m3,dam3,hm,km3)\nYêu cầu nhập chính xác tên đại lượng: ')
    if dlxuat == 'km3':
        slxuat = sl * 0.000000000000000001
    elif dlxuat == 'hm3':
        slxuat = sl * 0.000000000000001
    elif dlxuat == 'dam3':
        slxuat = sl * 0.000000000001
    elif dlxuat == 'm3':
        slxuat = sl * 0.000000001
    elif dlxuat == 'dm3':
        slxuat = sl * 0.000001
    elif dlxuat == 'cm3':
        slxuat = sl * 0.001
    else:
        slxuat = sl
    print(slnhap, dlnhap, '=', slxuat, dlxuat)
    time.sleep(3)
    menu()


def Dodai():
    dlnhap = input('Đại lượng nhập vào(mm,cm,dm,m,dam,hm,km)\nYêu cầu nhập chính xác tên đại lượng: ')
    slnhap = float(input('Chỉ số nhập vào:'))
    if dlnhap == 'km':
        sl = slnhap * 1000000
    if dlnhap == 'hm':
        sl = slnhap * 100000
    if dlnhap == 'dam':
        sl = slnhap * 1609344
    if dlnhap == 'm':
        sl = slnhap * 10000
    if dlnhap == 'dm':
        sl = slnhap * 1000
    if dlnhap == 'cm':
        sl = slnhap * 100
    dlxuat = input('Đại lượng muốn chuyển đổi(km,hm,dam,m,dm,cm,mm)\nYêu cầu nhập chính xác tên đại lượng : ')
    if dlxuat == 'km':
        slxuat = sl * 0.000001
    elif dlxuat == 'hm':
        slxuat = sl * 0.00001
    elif dlxuat == 'dam':
        slxuat = sl * 6.21504039776e-7
    elif dlxuat == 'm':
        slxuat = sl * 0.0001
    elif dlxuat == 'dm':
        slxuat = sl * 0.001
    elif dlxuat == 'cm':
        slxuat = sl * 0.01
    else:
        slxuat = sl
    print(slnhap, dlnhap, '=', slxuat, dlxuat)
    time.sleep(3)
    menu()


def Dientich():
    dlnhap = input('Đại lượng nhập vào(mm2,cm2,dm2,m2,dam2,hm2,km2)\nYêu cầu nhập chính xác đại lượng:')
    slnhap = float(input('Chỉ số nhập vào: '))
    if dlnhap == 'km**2':
        sl = slnhap * (1000000) ** 2
    if dlnhap == 'hm**2':
        sl = slnhap * (100000) ** 2
    if dlnhap == 'dam**2':
        sl = slnhap * (1609344) ** 2
    if dlnhap == 'm**2':
        sl = slnhap * (10000) ** 2
    if dlnhap == 'dm**2':
        sl = slnhap * (1000) ** 2
    if dlnhap == 'cm**2':
        sl = slnhap * (100) ** 2
    dlxuat = input('Đại lượng muốn chuyển đổi(km2,hm2,dam2,m2,dm2,cm2,mm2)\nYêu cầu nhập chính xác đại lượng:')
    if dlxuat == 'km**2':
        slxuat = sl * (0.000001) ** 2
    elif dlxuat == 'hm**2':
        slxuat = sl * (0.00001) ** 2
    elif dlxuat == 'dam**2':
        slxuat = sl * (6.21504039776e-7) ** 2
    elif dlxuat == 'm**2':
        slxuat = sl * (0.0001) ** 2
    elif dlxuat == 'dm**2':
        slxuat = sl * (0.001) ** 2
    elif dlxuat == 'cm**2':
        slxuat = sl * (0.01) ** 2
    else:
        slxuat = sl
    print(slnhap, dlnhap, '=', slxuat, dlxuat)
    time.sleep(3)
    menu()


def Hinhcau():
    r = float(input("Mời bạn nhập bán kính của hình cầu(cm): "))
    print("Thể tích hình cầu đó là: ", 4 / 3 * 3.14 * r * r * r, ' cm3')
    print("Diện tích mặt cầu đó là: ", 3.14 * r * r * 4, ' cm2')
    time.sleep(3)
    menu()


def Hopchunhat():
    a = float(input("Mời bạn nhập vào chiều dài của hình hộp chữ nhật(cm): "))
    b = float(input("Mời bạn nhập vào chiều rộng của hình hộp chữ nhật(cm): "))
    h = float(input("Mời bạn nhâp vào chiều cao của hình hộp chữ nhật(cm): "))
    print("Diện tích xung quanh của hình hộp chữ nhật đó là: ", (a + b) * 2 * h, ' cm2')
    print("Diện tích toàn phần của hình hộp chữ nhật đó là: ", (a + b) * 2 * h + 2 * a * b, ' cm2')
    print("Thể tích của hình hộp chữ nhật đó là: ", a * b * h, ' cm3')
    time.sleep(3)
    menu()


def Lapphuong():
    a = float(input("Mời bạn nhập cạnh của hình lập phương(cm): "))
    print("Thể tích hình lập phương đó là: ", a * a * a, ' cm3')
    print("Diện tích xung quanh hình lập phương đó là: ", a * a * 4, ' cm2')
    print("Diện tích toàn phần hình lập phương đó là: ", a * a * 6, ' cm2')
    time.sleep(3)
    menu()


def Hinhnon():
    h = float(input("Mời bạn nhập chiều cao của hình nón(cm): "))
    r = float(input("Mời bạn nhập bán kính của hình nón(cm): "))
    l = float(input("Mời bạn nhập đường sinh của hình nón(cm): "))
    print("Thể tích của hình nón đó là: ", r * r * 3.14 / 3 * h, ' cm3')
    print("Diện tích xung quanh của hình nón đó là: ", 3.14 * r * l, ' cm2')
    print("Diện tích toàn phần của hình nón đó là: ", 3.14 * r * l + r * r * 3.14, ' cm2')
    time.sleep(3)
    menu()


def Hinhtru():
    r = float(input("Mời bạn nhập bán kính của hình trụ (cm): "))
    h = float(input("Mời bạn nhập chiều cao của hình trụ (cm): "))
    print("Thể tích của hình trụ là:", r * r * 3.14 * h, ' cm3')
    print("Diện tích xung quanh của hình trụ là:", 2 * 3.14 * r * h, ' cm2')
    print("Diện tích toàn phần của hình trụ:", 2 * 3.14 * r * h + r * r * 3.14 * 2, ' cm2')
    time.sleep(3)
    menu()


def menu():
    choice = input(
        """
        /Các công cụ tính toán/
        1. Tính chỉ số BMI.
        2. Tính khoảng thời gian giữa hai ngày.
        3. Tính tuổi.
        /Các công cụ chuyển đổi/
        4. Chuyển đổi tốc độ.
        5. Chuyển đổi khối lượng.
        6. Chuyển đổi thể tích.
        7. Chuyển đổi độ dài.
        8. Chuyển đổi diện tích.
        /Các công cụ tính toán với hình không gian/
        9. Hình cầu.
        10. Hình hộp chữ nhật.
        11. Hình lập phương.
        12. Hình nón.
        13. Hình trụ. 
        14. Quit
        """)
    if choice == '1':
        BMI()
    elif choice == '2':
        Thoigian()
    elif choice == '3':
        Tuoi()
    elif choice == '4':
        Tocdo()
    elif choice == '5':
        Khoiluong()
    elif choice == '6':
        Thetich()
    elif choice == '7':
        Dodai()
    elif choice == '8':
        Dientich()
    elif choice == '9':
        Hinhcau()
    elif choice == '10':
        Hopchunhat()
    elif choice == '11':
        Lapphuong()
    elif choice == '12':
        Hinhnon()
    elif choice == '13':
        Hinhtru()
    elif choice == '14':
        print("Đang thoát...")
        time.sleep(1)
        sys.exit()

menu()
