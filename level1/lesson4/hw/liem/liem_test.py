a = int(input('Moi cac ban nhap mot so nguyen bat ki:'))
s = 0
i = 1
while i <= a:
    if i % 2 == 1:
        s = s + i
    i = i + 2
print('Tong bang:', s)
