a = int(input("Nhap vao so tien ban muon gui tiet kiem"))
b = int(input("Nhap vao so nam ban dinh gui tiet kiem"))
c = 0
while c <= b:
    a = a + (a * 12 / 100)
c = c + 1
print("So tien ban se nhan sau khi het ki han la:" + str(a))


while c <= b:
    a = a + (a * 12 / 100)
c = c + 1
rut = a - (a / 10)
print("So tien ban se nhan sau khi het ki han la:" + str(a))
print("Neu moi nam ban lay ra 1/10 so tien thi so tien sau khi het ki han la:" + str(rut))
