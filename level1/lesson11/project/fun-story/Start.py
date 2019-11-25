red = lambda text: '\033[0;31m' + text + '\033[0m'
notice = [
["1. Đây là game tán gái,nhưng tác giả đâu có để các bạn phái nữ thiệt thòi đâu nha. Nhưng trước đó thì các bạn nữ chịu khó tưởng tượng và thay các từ 'anh' thành 'em' và ngược lại cho phù hợp nhé~"],
["2. Nếu có bất kỳ sự trùng hợp nào, thì không hề có sự cố ý mà hoàn toàn do cố tình."],
["3. Khi Game Over, bạn sẽ tự động được Restart đến Checkpoint gần nhất. Nếu thoát chương trình thì xác định chạy lại từ đầu~"],
["4. Ý tưởng dựa trên tựa game mobile đang hot - Identity V~"],
["~ Thương hiệu mũ bảo hiểm Protect hân hạnh được tài trợ cho game ( và người chơi) ~"]
]
print(red("*Lưu ý :"))
for index in range (len(notice)):
  print (red(notice[index][0]))
  input ()

opening = [
["Giờ hãy cùng dõi theo câu chuyện của cậu ấy nào..."],

["*"*50],
["(Nhạc báo thức)*RUỲNH*"],
["??? :Oáp~"],
["??? :...Buồn ngủ quá."],
["(Bạn đi ra khỏi giường và mặc đồng phục trường. Xong xuôi, bạn không quên vớ lấy chiếc thẻ học sinh đang đặt trên bàn. )"]
]
for index in range (len (opening)):
  print (opening[index][0])
  input()