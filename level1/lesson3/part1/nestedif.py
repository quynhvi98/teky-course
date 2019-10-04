# Nhập điểm của 3 môn thi
print("Điểm toán:")
math = int(input())
print("Điểm văn:")
literature = int(input())
print("Điểm anh:")
english = int(input())
# Tổng điểm của 3 môn
ave = (math + literature + english) / 3
print("Điểm trung bình 3 môn là:", ave)
# Check role học sinh
if ave >= 9:
    print("Bạn đạt loại xuất sắc")
elif ave >= 8:
    print("Bạn đạt loại giỏi")
elif ave >= 6:
    print("Bạn đạt loại khá")
elif ave <= 5:
    print("Bạn đạt loại trung bình")
