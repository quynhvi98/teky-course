cyan = lambda text: '\033[0;36m' + text + '\033[0m'
print ("(Lưu ý : Một khi đã đặt tên bạn sẽ không đổi được nữa, hãy suy nghĩ cẩn thận)")
print (cyan("-----------------------------------------------------------"))
print (cyan("                       THẺ HỌC SINH"))
print (cyan(" __________"))
name = input (cyan("|          |  Tên học sinh : Carl (Điền tên bạn) "))
print (cyan("|          |"))
print (cyan("|          |  Lớp : S2"))
print (cyan("|          |") )
print (cyan("|          |  HỌC VIỆN DESAULNIER"))
print (cyan("|__________|")  )
print(cyan("-----------------------------------------------------------"))

#CHAP 1
chapter1 = [
[0 ,"~ CHAPTER 1 : Cuộc gặp gỡ ~"],
[1 , "Hôm nay là ngày đầu tiên trong thời cấp 3 đẹp đẽ của {}. Nhưng cậu vốn là một người ngại giao tiếp, nên đây sẽ chẳng phải một thời gian mơ mộng với những ước mơ tuổi trẻ như có bạn gái, đến tụ tập nhà thằng đồng chí, quẩy game thâu đêm,... đối với {} gì cho cam.".format(name,name)],
[2 , "Mải suy nghĩ, đã sắp muộn học rồi! Cậu vớ vội cái bánh mì gối nhét vào mồm rồi vụt chạy đến trường" ],
[3 , "{} : Phải nhanh nữa... Ối!".format(name)],
[4 , "Một cô gái cũng đang vội vã chạy, bộ đồng phục qua quen thuộc của Học viện Desaulnier được mặc gọn gàng trên người cô. Mái tóc cô trắng, màu trắng của OMO...à nhầm tuyết, đôi mắt xanh, màu xanh của bầu trời cao vời vợi... Cả hai đều không chú ý đến nhau nên tất nhiên sau đó là tiếng 'RUỲNH', 2 người đâm nhau."],
[5 , "Cú va chạm làm cô gái ngã ra đường. Con bạch tuộc aka bữa sáng của cô ấy cũng vui vẻ bay ra khỏi mồm mà giãy đành đạch trên đất.  Bạn sẽ làm gì?",
 ["1. Đỡ dậy",6],
 ["2. Mặc kệ",8],
 ["",10],
 ["(Gợi ý: Nó có thể không hiện hữu, nhưng nó có tồn tại)"]],
[6 , "Bạn lựa chọn đỡ con bạch tuộc"],
[7 , "Bạch tuộc đỏ mặt"],
[8 , "Cô gái : Anh dám bơ tôi như vậy hả...?"],
[9 , "Bad Ending 1 : Chết vì gái"],
[10 , "Bạn đỡ cô gái dậy" ],
[11 , "Josephine : Cảm ơn cậu. Josephine, còn cậu?"],
[12 ,"{} : ...{}. {} Carl. ".format(name,name,name) ]
]

#CHAP 2
chapter2 = [
[0 , "~ CHAPTER 2 : Yếu tố bất ngờ mà bất kỳ câu chuyện tình nào cũng có :v ~"],
[1 , "- Ở TRƯỜNG -"],
[2 , "(Bạn tiến lại gần tấm bảng phân lớp."],
[3 , "Naib : Ồ, không phải {} đấy ư! Chúng ta lại học chung lớp rồi, lớp S2 ở tầng 3 khu 2, mình cùng đi nhé?".format(name)],
[4 , "{} :...Ừ".format(name)],
[5 , "(Bạn cùng Naib đi đến khu nhà 2)"],
[6 , "Naib : Oa~ Hôm nay quả là một ngày đẹp trời. À, Ellie và William cũng học cùng mình đấy!"],
[7 , "{} : Ừm, vậy  à. Vui nhỉ.".format(name)],
[8 , "Naib : Haha, cậu lúc nào cũng vậy...Mà cậu đã quen ai ngoài bọn học chung cấp 2 chúng tớ ở trường này chưa?"],
[9 , "{} :...Không hẳn là quen. Tớ gặp cô ấy trên đường đến trường. Tụi tớ vô tình va vào nhau, thế là tớ đỡ cổ dậy.".format(name)],
[10 , "Naib : Ái chà, ái chà chà... Cậu có hỏi tên cô ấy không?"],
[11 , "{} : Im ngay tên kia. Josephine, cô ấy chủ động nói trước.".format(name)],
[12 , "Naib : Ừm ừm ~...Khoan, Josephine?"],
[13 , "{} : Ờ, đúng, sao vậy?".format(name)],
[14 , "Naib : Josephine là học sinh ưu tú của trường, học sinh năm 2. Thành tích học tập không nhất thì nhì trường! Cô ấy cũng là Hội trưởng hội HS đấy."],
[15 , "{} : Ồ, khủng quá.".format(name)],
[16 , "Naib :...Hợ, nói chuyện với cậu chán phèo."],
[17 , "............."],
[18 , "- TRONG LỚP -"],
[19 , "Ellie : Hế lô mấy bro~"],
[20 , "Ellie Clark là một cô gái kỳ lạ tôn sùng một tín ngưỡng kỳ lạ. Cô không bao giờ để lộ ra mắt mình (chắc nó cũng kỳ lạ) mà chỉ luôn đeo một chiếc băng kỳ lạ mang hình vẽ kỳ lạ. Cô có một khả năng kỳ lạ là tiên tri và thường thì cô tiên tri đúng đến kỳ lạ. Nhưng tính cách cô thì không có gì kỳ lạ."],
[21 , "Naib : Chào cậu Ellie. Cậu biết không, {} vừa gặp ngay một học sinh thuộc hàng top của trường - Josephine rồi đó~~~ "],
[22 , "Ellie : Ồ ~~~~ Để tớ phái Eule đi điều tra về nàng nhé? - Eule là con cu...à nhầm con cú của cô ấy, vì lý do nào đó mà lại là động vật duy nhất được mang vào trường. Nó cũng kỳ lạ nhưng thôi khỏi kể đi." ],
[26 , "Đúng lúc đó, chuông vào lớp vang lên"],
[27 , "Ellie : Không biết giáo viên nhìn như nào? "],
[28 , "Phía cửa lớp, tiếng 'Xoạch' vang lên. Thầy giáo bước vào. Ellie bỗng há hốc miệng, lấy tay che."],
[29 , "Một nam nhân khôi ngô, tuấn tú bước vào. Đôi mắt đỏ rực hút hồn, mái tóc trắng dài  càng làm nổi bật sự nam tính. Có lẽ cậu hiểu lý do Ellie ngạc nhiên rồi."],
[30 , "Ellie : Thầy Hastur??? - Có lẽ họ đã quen nhau từ trước. "],
[31 , "Hastur : Chào các em. Thầy là Hastur -  GVCN của lớp mình cho đến hết năm cuối, nếu như không có gì thay đổi. "],
[32 , "Naib : (hỏi nhỏ) Sao vậy Ellie? " ],
[33 , "Ellie : Thầy ấy là người bảo hộ của tớ. Tớ không sống với bố mẹ, bố mẹ tớ... mất lâu rồi."],
[34 , "Naib:...Chia buồn...Cơ mà tối đến cậu ngủ cùng phòng với thầy ấy à? ( ͡° ͜ʖ ͡°)"],
[35 , "Ellie :...Đồ đầu óc đen tối."],

]
