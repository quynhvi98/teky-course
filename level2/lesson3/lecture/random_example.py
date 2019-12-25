import random

#tạo số ngẫu nhiên nhỏ hơn 1 số cho trước với hàm randrange(a)
random.randrange(100)

#Tạo số ngẫu nhiên với randrange(a,b[, step]) => sỉnh ra một số ngẫu nhiên trong khoảng tù 0 đến 100 và chia hết cho 3
random.randrange(0, 100, 3)

# Tạo số nguyên int với ranint(a, b)
random.randint(1, 6)

# Tạo số thực float ngẫu nhiên với uniform(a, b)

random.uniform(1, 20)

# Sử dụng module random với kiểu dữ liệu list
# trả về 1 giá trị ngẫu nhiên trong list
random.choice(list)
#trả về 1 danh sách đã xáo trộn ngẫu nhiên
random.shuffle(list)
#Trả về n phẩn tử duy nhất trong list đã cho
#random.sample(list, n)

ids = [1, 8, 10, 12, 15, 17, 25]

random.choice(ids)
random.choice(ids)

names = ['Tom', 'Harry', 'Andrew', 'Robert']
random.choice(names)
random.choice(names)

random.shuffle(names)
names

random.sample(names, 2)
random.sample(names, 2)

names