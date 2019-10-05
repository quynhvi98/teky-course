x = 1;
s = 0
while (x < 10):
    s = s + x
    x = x + 1
    if (x == 5):
        break
else:
    print('The sum of first 9 integers : ', s)
print('The sum of ', x, ' numbers is :', s)
