# case 1: i=3, j=5, k=7
# case 2: i=3, j=7, k=5
# case 3: i=5, j=3, k=7
# case 4: i=5, j=7, k=3
# case 5: i=7, j=3, k=5
# case 6: i=7, j=5, k=3

i = int(input("Please enter value of i:"))
j = int(input("Please enter value of j:"))
k = int(input("Please enter value of k:"))
if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print("i = ", i, "j = ", j, "k = ", k)
