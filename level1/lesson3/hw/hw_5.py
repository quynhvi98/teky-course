# case 1: val = 3
# case 2: val = 21
# case 3: val = 5
# case 4: val = 17
# case 5: val = -5
val = eval(input())
if val < 10:
    if val != 5:
        print("wow", end='')
    else:
        val += 1
else:
    if val == 17:
        val += 10
    else:
        print("whoa", end='')
print(val)
