black = lambda text: '\033[0;30m' + text + '\033[0m'
red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'
yellow = lambda text: '\033[0;33m' + text + '\033[0m'
blue = lambda text: '\033[0;34m' + text + '\033[0m'
magenta = lambda text: '\033[0;35m' + text + '\033[0m'
cyan = lambda text: '\033[0;36m' + text + '\033[0m'
white = lambda text: '\033[0;37m' + text + '\033[0m'
cyan = lambda text: '\033[0;36m' + text + '\033[0m'

intro = "Chào mừng đến với chương trình quản lý học sinh của tôi"

print(cyan("-----------------------------------------------------------"))
print(cyan("                       THẺ NGƯỜI QUẢN LÝ"))
print(cyan(" __________"))
name = input(cyan("|          |  Tên người quản lý : "))
print(cyan("|          |"))
print(cyan("|  ( ◠‿◠ ) |  Lớp : SNLT1"))
print(cyan("|          |"))
print(cyan("|          |  HỌC VIỆN TEKY"))
print(cyan("|__________|"))
print(cyan("-----------------------------------------------------------"))

menu = """
==Đây là phần mềm quản lý học sinh==
#1.  Số điểm cao nhất.
#2.  Số điểm thấp nhất.
#3.  In ra học sinh có số điểm thấp nhất.
#4.  In ra học sinh có điểm cao nhất.
#5.  Đếm số lượng học sinh ở mỗi lớp (1-12)
#6.  Tính điểm trung bình của tất cả học sinh.
#7.  Tính điểm trung bình của từng lớp.
#8.  Đếm số học sinh có điểm trên 8.
#9.  Danh sách học sinh.
#10. Thêm 1 học sinh vào danh sách.
#11. In ra danh sách học sinh có số điểm bằng với số điểm nhập từ bàn phím.
#12. Print grade that have the most students
#0.  Exit program

"""
good_bye = "Chao ban chuc ban vui ve , ban co feedback cho phan mem cua toi ve email vi.quynh@gmail.com"
StudentList = [
    [1, "Nguyễn Ngọc Huy", 7, 8.56],
    [2, "Nguyễn Đắc Tâm", 7, 1.95],
    [3, "Nguyễn Phan Anh", 8, 9.56],
    [4, "Lê Hữu Thanh Liêm", 8, 1.24],
    [5, "Hồ Đức Trịnh", 4, 2.77],
    [6, "Hà Vinh Khoa", 5, 0.98],
    [7, "Đinh Thắm Tăng", 6, 6.65],
    [8, "Lâm Dung Kha", 12, 3.21],
    [9, "Lý Ngô Sa", 1, 9.44],
    [10, "Đinh Tú Tăng", 4, 8.81],
    [11, "Phan Thủy Tuân", 5, 6.24],
    [12, "Hồ Tú Kim", 8, 9.70],
    [13, "Tăng Dung Thắgn", 8, 0.03],
    [14, "Nguyễn Lê Thắm", 1, 0.11],
    [15, "Hồ Nhung Mai", 11, 1.28],
    [16, "Phạm Sa Nguyễn", 10, 4.84],
    [17, "Tăng Tiến Đào", 8, 5.38],
    [18, "Dương Kha Thắm", 10, 8.34],
    [19, "Đào Đinh Tiến", 7, 6.31],
    [20, "Đào Cường Nam", 3, 2.00],
    [21, "Phùng Thu Tăng", 4, 3.51],
    [22, "Đào Triệu Thắgn", 1, 9.66],
    [23, "Hoàng Dương Đặng", 11, 6.63],
    [24, "Hồ Thủy Phong", 3, 8.73],
    [25, "Đỗ Mai Thu", 11, 1.50],
    [26, "Hà Kim Tô", 12, 5.03],
    [27, "Vũ Nhân Minh", 9, 9.84],
    [28, "Lý Minh Tăng", 4, 2.21],
    [29, "Đào Thi Hoàng", 10, 8.61],
    [30, "Tăng Phùng Lý", 11, 1.89],
    [31,"Phạm Lâm Lý", 3, 6.23],
    [32, "Phạm Phùng Trần", 10, 3.48],
    [33, "Đỗ Minh Nhân", 5, 4.72],
    [34, "Trần Thắgn Dung", 4, 4.61],
    [35, "Phạm Đức Bửu", 6, 7.33],
    [36, "Nguyễn Trinh Cường", 9, 4.79],
    [37, "Mai Lâm Tăng", 10, 4.61],
    [38, "Đặng Thắm Lê", 3, 5.73],
    [39, "Trương Dương Thanh", 7, 9.12],
    [40, "Đào Sinh Tăng", 3, 0.75],
    [41, "Lê Hiền Hải", 9, 1.02],
    [42, "Ngô Hải Đỗ", 11, 8.10],
    [43, "Đào Phú Dương", 6, 5.71],
    [44, "Dương Kim Phong", 6, 8.67],
    [45, "Vương Tú Tuân", 9, 7.74],
    [46, "Đoàn Thắm Triệu", 8, 6.45],
    [47, "Hồ Cường Thảo", 3, 3.94],
    [48, "Trương Bửu Lâm", 4, 3.78],
    [49, "Hà Lê Khang", 4, 3.78],
    [50, "Phan Loan Đinh", 3, 2.67],
]

print(intro)
while True:
    print(yellow(menu))
    yc = input("Nhap vao yeu cau:")
    if yc == '0':
        break
    elif yc == '1':
        highest_score = StudentList[0][2]
        for student in StudentList:
            score = student[2]
            if score > highest_score:
                highest_score = score
        print('Diem cao nhat la :', highest_score)
    elif yc == '2':
        lowest_score = StudentList[0][2]
        for student in StudentList:
            score = student[2]
            if score < lowest_score:
                lowest_score = score
        print('Diem cao nhat la :', lowest_score)
    elif yc == '3':
        for st in StudentList:
            if st[2] == lowest_score:
                print(st)
    elif yc == '4':
        highest_score = StudentList[0][2]
        for student in StudentList:
            score = student[2]
            if score > highest_score:
                highest_score = score
        for student in StudentList:
            score = student[2]
            if score == highest_score:
                print("Ban {} co diem cao nhat la {}".format(
                    student[0], highest_score))
    elif yc == '5':
        StudentListByGrade = []
        for i in range(0, 12):
            StudentListByGrade.append([])
        for student in StudentList:
            grade = student[1]
            StudentListByGrade[grade - 1].append(student)
        for i in range(0, 12):
            print("Cac hoc sinh khoi {}: {}".format(
                i + 1, len(StudentListByGrade[i])))
    elif yc == '6':
        print("Số học sinh là: ", len(StudentList))
    elif yc == '7':
        diem_so_khoi = []
        for i in range(1, 13):
            diem_so_khoi = []
            for st in StudentList:
                if st[1] == i:
                    diem_so_khoi.append(st[2])
            print("Tong diem khoi ", i, " la ", sum(diem_so_khoi) / len(diem_so_khoi))
    elif yc == '8':
        sohocsinhlonhon8 = 0
        for s in StudentList:
            if s[2] >= 8:
                sohocsinhlonhon8 += 1
        print("So hoc sinh co diem lon hon 8 la", sohocsinhlonhon8)
    elif yc == '9':
        print(black("STT  |        Tên học sinh        |  Khối lớp  |   Điểm tổng kết"))
        for st in StudentList:
            print(st[0], "\t", "|\t\t", st[1], st[2], st[3])
    elif yc == '10':
        StudentList.append(
            [input("Ten cua hoc sinh "), int(input("Hoc sinh hoc khoi nao?")), int(input("Diem so cua hoc sinh"))])
        print(StudentList[100])
    elif yc == '11':
        diem_so = input("Nhap vao diem ma ban muon tim:")
        for student in StudentList:
            if diem_so == str(student[2]):
                print(student)
    elif yc == '12':
        StudentListByGrade = []
        for i in range(0, 12):
            StudentListByGrade.append([])
        for student in StudentList:
            grade = student[1]
            StudentListByGrade[grade - 1].append(student)
        so_hoc_sinh_nhieu_nhat_1_khoi = len(StudentListByGrade[0])
        khoi_co_nhieu_hs_nhat = 0
        for i in range(0, 12):
            if so_hoc_sinh_nhieu_nhat_1_khoi < len(StudentListByGrade[i]):
                so_hoc_sinh_nhieu_nhat_1_khoi = len(StudentListByGrade[i])
                khoi_co_nhieu_hs_nhat = i
        print(
            "Khoi co nhieu hoc sinh nhat la {} ({} hoc sinh)".format(
                khoi_co_nhieu_hs_nhat + 1, so_hoc_sinh_nhieu_nhat_1_khoi))

    input()
print(good_bye)
