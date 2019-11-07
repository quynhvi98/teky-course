cyan = lambda text: '\033[0;36m' + text + '\033[0m'
red = lambda text: '\033[0;31m' + text + '\033[0m'
print("(Lưu ý : Một khi đã đặt tên bạn sẽ không đổi được nữa, hãy suy nghĩ cẩn thận)")
print(cyan("-----------------------------------------------------------"))
print(cyan("                       THẺ HỌC SINH"))
print(cyan(" __________"))
name = input(cyan("|          |  Tên học sinh : Carl (Điền tên bạn) "))
print(cyan("|          |"))
print(cyan("|          |  Lớp : SNLT1"))
print(cyan("|          |"))
print(cyan("|          |  HỌC VIỆN Teky"))
print(cyan("|__________|"))
print(cyan("-----------------------------------------------------------"))
print('Combo red heart')
print(red('💜') + ' you and me 👫')

# CHAP 1
chapter1 = [
    [0, "~ CHAPTER 1 : Cuộc gặp gỡ ~"],
    [1,
     "Hôm nay là ngày đầu tiên trong thời cấp 3 đẹp đẽ của {}. Nhưng cậu vốn là một người ngại giao tiếp, nên đây sẽ chẳng phải một thời gian mơ mộng với những ước mơ tuổi trẻ như có bạn gái, đến tụ tập nhà thằng đồng chí, quẩy game thâu đêm,... đối với {} gì cho cam.".format(
         name, name)],
    [2, "Mải suy nghĩ, đã sắp muộn học rồi! Cậu vớ vội cái bánh mì gối nhét vào mồm rồi vụt chạy đến trường"],
    [3, "{} : Phải nhanh nữa... Ối!".format(name)],
    [4,
     "Một cô gái cũng đang vội vã chạy, bộ đồng phục qua quen thuộc của Học viện Desaulnier được mặc gọn gàng trên người cô. Mái tóc cô trắng, màu trắng của OMO...à nhầm tuyết, đôi mắt xanh, màu xanh của bầu trời cao vời vợi... Cả hai đều không chú ý đến nhau nên tất nhiên sau đó là tiếng 'RUỲNH', 2 người đâm nhau."],
    [5,
     "Cú va chạm làm cô gái ngã ra đường. Con bạch tuộc aka bữa sáng của cô ấy cũng vui vẻ bay ra khỏi mồm mà giãy đành đạch trên đất.  Bạn sẽ làm gì?",
     ["1. Đỡ dậy", 6],
     ["2. Mặc kệ", 8],
     ["", 10],
     ["(Gợi ý: Nó có thể không hiện hữu, nhưng nó có tồn tại)"]],
    [6, "Bạn lựa chọn đỡ con bạch tuộc"],
    [7, "Bạch tuộc đỏ mặt"],
    [8, "Cô gái : Anh dám bơ tôi như vậy hả...?"],
    [9, "Bad Ending 1 : Chết vì gái"],
    [10, "Bạn đỡ cô gái dậy"],
    [11, "Josephine : Cảm ơn cậu. Josephine, còn cậu?"],
    [12, "{} : ...{}. {} Carl. ".format(name, name, name)]
]

# CHAP 2
chapter2 = [
    [0, "~ CHAPTER 2 : Yếu tố bất ngờ mà bất kỳ câu chuyện tình nào cũng có :v ~"],
    [1, "- Ở TRƯỜNG -"],
    [2, "(Bạn tiến lại gần tấm bảng phân lớp."],
    [3,
     "Naib : Ồ, không phải {} đấy ư! Chúng ta lại học chung lớp rồi, lớp S2 ở tầng 3 khu 2, mình cùng đi nhé?".format(
         name)],
    [4, "{} :...Ừ".format(name)],
    [5, "(Bạn cùng Naib đi đến khu nhà 2)"],
    [6, "Naib : Oa~ Hôm nay quả là một ngày đẹp trời. À, Ellie và William cũng học cùng mình đấy!"],
    [7, "{} : Ừm, vậy  à. Vui nhỉ.".format(name)],
    [8, "Naib : Haha, cậu lúc nào cũng vậy...Mà cậu đã quen ai ngoài bọn học chung cấp 2 chúng tớ ở trường này chưa?"],
    [9,
     "{} :...Không hẳn là quen. Tớ gặp cô ấy trên đường đến trường. Tụi tớ vô tình va vào nhau, thế là tớ đỡ cổ dậy.".format(
         name)],
    [10, "Naib : Ái chà, ái chà chà... Cậu có hỏi tên cô ấy không?"],
    [11, "{} : Im ngay tên kia. Josephine, cô ấy chủ động nói trước.".format(name)],
    [12, "Naib : Ừm ừm ~...Khoan, Josephine?"],
    [13, "{} : Ờ, đúng, sao vậy?".format(name)],
    [14,
     "Naib : Josephine là học sinh ưu tú của trường, học sinh năm 2. Thành tích học tập không nhất thì nhì trường! Cô ấy cũng là Hội trưởng hội HS đấy."],
    [15, "{} : Ồ, khủng quá.".format(name)],
    [16, "Naib :...Hợ, nói chuyện với cậu chán phèo."],
    [17, "............."],
    [18, "- TRONG LỚP -"],
    [19, "Ellie : Hế lô mấy bro~"],
    [20,
     "Ellie Clark là một cô gái kỳ lạ tôn sùng một tín ngưỡng kỳ lạ. Cô không bao giờ để lộ ra mắt mình (chắc nó cũng kỳ lạ) mà chỉ luôn đeo một chiếc băng kỳ lạ mang hình vẽ kỳ lạ. Cô có một khả năng kỳ lạ là tiên tri và thường thì cô tiên tri đúng đến kỳ lạ. Nhưng tính cách cô thì không có gì kỳ lạ."],
    [21,
     "Naib : Chào cậu Ellie. Cậu biết không, {} vừa gặp ngay một học sinh thuộc hàng top của trường - Josephine rồi đó~~~ "],
    [22,
     "Ellie : Ồ ~~~~ Để tớ phái Eule đi điều tra về nàng nhé? - Eule là con cu...à nhầm con cú của cô ấy, vì lý do nào đó mà lại là động vật duy nhất được mang vào trường. Nó cũng kỳ lạ nhưng thôi khỏi kể đi."],
    [26, "Đúng lúc đó, chuông vào lớp vang lên"],
    [27, "Ellie : Không biết giáo viên nhìn như nào? "],
    [28, "Phía cửa lớp, tiếng 'Xoạch' vang lên. Thầy giáo bước vào. Ellie bỗng há hốc miệng, lấy tay che."],
    [29,
     "Một nam nhân khôi ngô, tuấn tú bước vào. Đôi mắt đỏ rực hút hồn, mái tóc trắng dài  càng làm nổi bật sự nam tính. Có lẽ cậu hiểu lý do Ellie ngạc nhiên rồi."],
    [30, "Ellie : Thầy Hastur??? - Có lẽ họ đã quen nhau từ trước. "],
    [31,
     "Hastur : Chào các em. Thầy là Hastur -  GVCN của lớp mình cho đến hết năm cuối, nếu như không có gì thay đổi. "],
    [32, "Naib : (hỏi nhỏ) Sao vậy Ellie? "],
    [33, "Ellie : Thầy ấy là người bảo hộ của tớ. Tớ không sống với bố mẹ, bố mẹ tớ... mất lâu rồi."],
    [34, "Naib:...Chia buồn...Cơ mà tối đến cậu ngủ cùng phòng với thầy ấy à? ( ͡° ͜ʖ ͡°)"],
    [35, "Ellie :...Đồ đầu óc đen tối."],

]

# CHAP 3
chapter3 = [
    [0, "~ CHAPTER 3 : Ai cũng có một câu chuyện tình ~ "],
    [1, "Ngày đầu ở Học viện trôi qua rất nhanh."],
    [2,
     "Ellie : Bái bai nhé, mai gặp lại! À Naib, lúc đi về nhớ để ý xem có ai theo dõi không, cẩn thận bị bắt vào ngõ ( ͡° ͜ʖ ͡°). - Ellie vừa đi cùng Hastur vừa nhìn lại, vẫy tay chào họ."],
    [3, "{} :...Ý cô ấy là sao? Lại tiên tri vớ vẩn à?".format(name)],
    [4, "Naib : Chơi lại tôi vố trước thôi, cậu không cần biết~ "],
    [5, "{} :...Tôi chỉ tự hỏi cô ấy làm gì ở nhà với... ừm....( ͡° ͜ʖ ͡°)".format(name)],
    [6, "Naib : Không can cậu nói ra =]"],
    [7, "Đúng là chỉ có bọn đầu óc đen tối mới hiểu nhau."],
    [8, "Naib : Thôi, tui về. Cậu thì sao?",
     ["1. Về nhà", 9],
     ["2. Ở lại trường một lúc", 11]],
    [9, "{} : Thì về nhà thôi.".format(name)],
    [10, "Naib : Vậy thì tạm biệt nhé, mai lại gặp!"],
    [11, "{} : Tớ ở trường dạo chơi một chút...".format(name)],
    [12,
     "Naib : {} ở riêng mà, thích nhỉ? Thích làm gì, về lúc nào cũng không ai mắng... Thôi bye, tui về không mẹ lại la.".format(
         name)],
    [13, "{} : Ừm, bye.".format(name)],
    [14, "Bạn rảo bước trên sân trường. Đi đâu giờ?",
     ["1. Thư viện", 15],
     ["2. Khu khối H", ],
     ["3. Sân sau của trường", ]],
    [15,
     "Bạn bước vào Thư viện của trường. Đó là một thư viện nhìn khá cổ, tuy không rộng nhưng lại cao. Những giá sách gỗ xoáy thành hình xoắn ốc lên đến trần nhà, muốn lấy được những cuốn sách ở trên cùng phải bắc thang lên mà lấy."],
    [16, "Bạn nhìn thấy một ai đó rất quen thuộc."],
    [17,
     "{} : Josephine? - Tuy cố hắng giọng xuống để không làm phiền mọi người trong thư viện, một  gì đó khiến bạn không làm được".format(
         name)],
    [18,
     "Josephine : Hửm? A, chẳng phải {} đấy ư? Chúng ta lại gặp nhau rồi!- Cô trả lời sau tiếng 'Suỵt' của mọi người. - Em làm gì ở đây vậy?".format(
         name),
     ["1.Stalk chị _|･ω･)-<3", 19],
     ["2.Nghiên cứu về Học viện Desaulnier", 21],
     ],
    [19, "Josephine :...Moshi moshi, police desuka?"],
    [20, "BAD ENDING 2 : Nước chè ở đồn rất ngon"],
    [21, "{} : Ừm, em muốn tìm hiểu thêm một chút về trường mình..."],
    [22, "Josephine : Nếu vậy thì em ra tủ sách đằng kia nhé, dãy thứ 3 từ dưới lên là tìm được ngay thứ em muốn."],
    [23,
     "Bạn đi đến đó, lấy ra một quyển sách có đề 'HV Desaulnier và lịch sử huy hoàng' rồi ngồi ở ghế đối diện với Josephine."],
    [24, "Josephine : Em biết không, em là đàn em khóa dưới đầu tiên chị gặp đấy!"],
    [25, "{} : Dạ, vậy ạ..."],
    [26, "...Josephine dường như nhận ra "],
]
