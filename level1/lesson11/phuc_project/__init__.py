import sys
import time

def sum(a, b):
    print("Tong cua 2 so la:", a+b)
    # menu()
def diff(a, b):
    print("Hieu cua 2 so la:", a-b)
    menu()
def tich(a, b):
    print("Tich cua 2 so la:", a*b)
    menu()
def thuong(a, b):
    print("Thuong cua 2 so la:", float(a/b))
    menu()

def menu():
    a = int(input("Moi ban nhap so a:"))
    b = int(input("Moi ban nhap so b:"))
    choice = input(
        """
        1. Tong cua 2 so.
        2. Hieu cua 2 so.
        3. Tich cua 2 so.
        4. Thuong cua 2 so.
        5. Quit
        """)
    if choice == '1':
        sum(a, b)
    elif choice == '2':
        diff(a, b)
    elif choice == '3':
        tich(a, b)
    elif choice == '4':
        thuong(a, b)
    elif choice == '5':
        print("Đang thoát...")
        time.sleep(1)
        sys.exit()

menu()

