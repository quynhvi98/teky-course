black = lambda text: '\033[0;30m' + text + '\033[0m'
red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'
yellow = lambda text: '\033[0;33m' + text + '\033[0m'
blue = lambda text: '\033[0;34m' + text + '\033[0m'
magenta = lambda text: '\033[0;35m' + text + '\033[0m'
cyan = lambda text: '\033[0;36m' + text + '\033[0m'
white = lambda text: '\033[0;37m' + text + '\033[0m'
intro = "Chào mừng đến với chương trình quản lý học sinh của tôi"
cyan = lambda text: '\033[0;36m' + text + '\033[0m'
print("(Lưu ý : Một khi đã đặt tên bạn sẽ không đổi được nữa, hãy suy nghĩ cẩn thận)")
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
#11. Thêm 1 học sinh vào danh sách.
#12. In ra danh sách học sinh có số điểm bằng với số điểm nhập từ bàn phím.
#13. In ra danh sách học sinh có số điểm bằng với Print list of student have grade equal input
#14. Print list of student have score in range equal input
#15. Print grade that have the most students
#0.  Exit program

"""
good_bye  = "Chao ban chuc ban vui ve , ban co feedback cho phan mem cua toi ve email vi.quynh@gmail.com"
StudentList = [
    ["Trần Mai Ngô", 10, 8.56],
    ["Lý Quốc Tuân", 1, 1.95],
    ["Nguyễn Minh Phú", 1, 9.56],
    ["Lê Nhân Tô", 6, 1.24],
    ["Hồ Đức Trịnh", 4, 2.77],
    ["Hà Vinh Khoa", 5, 0.98],
    ["Đinh Thắm Tăng", 6, 6.65],
    ["Lâm Dung Kha", 12, 3.21],
    ["Lý Ngô Sa", 1, 9.44],
    ["Đinh Tú Tăng", 4, 8.81],
    ["Phan Thủy Tuân", 5, 6.24],
    ["Hồ Tú Kim", 8, 9.70],
    ["Tăng Dung Thắgn", 8, 0.03],
    ["Nguyễn Lê Thắm", 1, 0.11],
    ["Hồ Nhung Mai", 11, 1.28],
    ["Phạm Sa Nguyễn", 10, 4.84],
    ["Tăng Tiến Đào", 8, 5.38],
    ["Dương Kha Thắm", 10, 8.34],
    ["Đào Đinh Tiến", 7, 6.31],
    ["Đào Cường Nam", 3, 2.00],
    ["Phùng Thu Tăng", 4, 3.51],
    ["Đào Triệu Thắgn", 1, 9.66],
    ["Hoàng Dương Đặng", 11, 6.63],
    ["Hồ Thủy Phong", 3, 8.73],
    ["Đỗ Mai Thu", 11, 1.50],
    ["Hà Kim Tô", 12, 5.03],
    ["Vũ Nhân Minh", 9, 9.84],
    ["Lý Minh Tăng", 4, 2.21],
    ["Đào Thi Hoàng", 10, 8.61],
    ["Tăng Phùng Lý", 11, 1.89],
    ["Phạm Lâm Lý", 3, 6.23],
    ["Phạm Phùng Trần", 10, 3.48],
    ["Đỗ Minh Nhân", 5, 4.72],
    ["Trần Thắgn Dung", 4, 4.61],
    ["Phạm Đức Bửu", 6, 7.33],
    ["Nguyễn Trinh Cường", 9, 4.79],
    ["Mai Lâm Tăng", 10, 4.61],
    ["Đặng Thắm Lê", 3, 5.73],
    ["Trương Dương Thanh", 7, 9.12],
    ["Đào Sinh Tăng", 3, 0.75],
    ["Lê Hiền Hải", 9, 1.02],
    ["Ngô Hải Đỗ", 11, 8.10],
    ["Đào Phú Dương", 6, 5.71],
    ["Dương Kim Phong", 6, 8.67],
    ["Vương Tú Tuân", 9, 7.74],
    ["Đoàn Thắm Triệu", 8, 6.45],
    ["Hồ Cường Thảo", 3, 3.94],
    ["Trương Bửu Lâm", 4, 3.78],
    ["Hà Lê Khang", 4, 3.78],
    ["Trịnh Thị Đào", 3, 5.74],
    ["Phan Đỗ Khang", 2, 2.02],
    ["Hoàng Thị Triệu", 4, 6.90],
    ["Đoàn Lý Hồ", 5, 9.55],
    ["Hà Phùng Vân", 5, 4.96],
    ["Đào Thắgn Trần", 9, 2.17],
    ["Phan Hoàng Đoàn", 3, 7.01],
    ["Hoàng Thi Hoàng", 10, 1.34],
    ["Đỗ Bùi Kha", 5, 1.31],
    ["Phùng Loan Đinh", 12, 3.01],
    ["Đinh Như Loan", 7, 6.72],
    ["Trịnh Phan Đặng", 7, 4.24],
    ["Nguyễn Thắgn Hòa", 7, 2.32],
    ["Đinh Tâm Phong", 7, 8.66],
    ["Nguyễn Thu Hồ", 4, 2.73],
    ["Vương Mai Thi", 2, 0.81],
    ["Đỗ Phạm Vũ", 2, 6.21],
    ["Hoàng Nhân Tăng", 1, 2.39],
    ["Đặng Vũ Trịnh", 10, 8.89],
    ["Trần Phong Ngọc", 2, 1.01],
    ["Đoàn Quốc Trịnh", 2, 9.63],
    ["Trần Cường Phan", 6, 7.95],
    ["Lê Lê Nhân", 5, 3.25],
    ["Đoàn Phùng Thảo", 4, 0.72],
    ["Trần Thắm Đoàn", 2, 0.45],
    ["Đỗ Hải Tăng", 12, 5.11],
    ["Trương Đặng Phùng", 5, 4.77],
    ["Lâm Vũ Tâm", 9, 2.48],
    ["Phùng Cường Mai", 6, 4.70],
    ["Lý Nhàn Vân", 11, 0.97],
    ["Mai Thủy Tú", 3, 6.06],
    ["Phạm Tuân Thắgn", 4, 9.59],
    ["Trương Thu Hữu", 3, 6.31],
    ["Tăng Ngọc Quốc", 6, 3.12],
    ["Hồ Trương Phan", 3, 3.90],
    ["Lý Ngọc Đức", 4, 9.84],
    ["Ngô Triệu Khoa", 5, 1.44],
    ["Vương Minh Hồ", 3, 6.04],
    ["Vương Tăng Nhung", 5, 8.05],
    ["Dương Hữu Trung", 9, 1.04],
    ["Phạm Sa Dung", 4, 3.08],
    ["Mai Hiền Lý", 5, 5.62],
    ["Tăng Trịnh Tăng", 6, 7.88],
    ["Ngô Phan Phú", 2, 3.72],
    ["Lâm Đặng Thi", 3, 5.03],
    ["Lâm Thắgn Trần", 9, 0.83],
    ["Hồ Thị Dương", 5, 0.07],
    ["Dương Sa Long", 9, 9.39],
    ["Đặng Vũ Mai", 10, 8.02],
    ["Bùi Thi Tuân", 12, 6.82],
    ["Phan Loan Đinh", 3, 2.67],
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
        print("Số học sinh là: ", len(StudentList))
    elif yc == '9':
        print("Số học sinh là: ", len(StudentList))
    elif yc == '10':
        print("Số học sinh là: ", len(StudentList))
    elif yc == '11':
        StudentList.append(
            [input("Ten cua hoc sinh "), int(input("Hoc sinh hoc khoi nao?")), int(input("Diem so cua hoc sinh"))])
        print(StudentList[100])
    elif yc == '12':
        diem_so = input("Nhap vao diem ma ban muon tim:")
        for student in StudentList:
            if diem_so == str(student[2]):
                print(student)
    elif yc == '15':
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
