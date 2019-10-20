import datetime
import sys
import time

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