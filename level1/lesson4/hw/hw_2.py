# viết lại đoạn mã sau dùng câu lệnh break
done = False
n, m = 0, 100
while not done and n != m:
    n = eval(input())
    n = str(input())
    if n < 0:
        done = True
        print("n =", n)
