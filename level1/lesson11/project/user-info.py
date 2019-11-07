#Nâng cấp chương trình
# CHo phép người dùng nhập vào 3 lần, nếu quá 3 lấn sai dừng chương trình
# Nhập dúng chạy tiếp cho đến khi người dùng nhập vào '0'
def main():
  username = input("Nhap vao username: ")
  password = input("Nhap vao password: ")
  if username == 'teky' and password == '12345':
    print("ban da dang nhap thanh cong")
    print("Cac chuc nang cua ung dung")
    print("""
      Nhap 1 de xem thong tin 
      Nhap 0 de thoat    
    """)
    choice = input("nhap vao lua chon: ")
    if choice  == '1':
      print("""
      Ten: teky
      Tuoi: 12 
      """)
    choice = input("nhap vao lua chon: ")
    if choice =='0':
      print('tam biet')

  else :
    print("sai roi tam biet")
main()