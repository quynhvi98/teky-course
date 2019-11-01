black = lambda text: '\033[0;30m' + text + '\033[0m'
red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'
yellow = lambda text: '\033[0;33m' + text + '\033[0m'
blue = lambda text: '\033[0;34m' + text + '\033[0m'
magenta = lambda text: '\033[0;35m' + text + '\033[0m'
cyan = lambda text: '\033[0;36m' + text + '\033[0m'
white = lambda text: '\033[0;37m' + text + '\033[0m'

print(green("-----------... ----------" + "\n" + "Developed by UwU PRODUCTION" + "\n" + "Loading..." + "\n"))
print("""Tiếng nhạc báo thức đang kêu. Bạn sẽ làm gì? : 
1. Thức dậy (Bắt đầu Game)
2. Ngủ tiếp (Tắt Game) 
""")
yc = input(green("Lựa chọn của bạn : "))
while yc != '1' and yc != '2':
    yc = input("Chúng tôi khuyến khích sự sáng tạo nhưng không phải trong trường hợp này. Xin hãy chọn lại :")
if yc == '2':
    print("...Chúc ngủ ngon. Mọi feedback xin hãy gửi về email baohanmi@gmail.com" + "\n" + "zzZZ")
if yc == '1':
    # import Instruction
    # import Start
    import Story

    current_storyline = 0
    for index in range(len(Story.chapter1)):
        if index < current_storyline:
            continue
        storyline = Story.chapter1[index]
        content = storyline[1]
        print(content)
        input()
        if len(storyline) > 2:
            choices = storyline[2:]
            for choice in choices:
                print(choice[0])
            lua_chon = int(input("Lựa chọn : "))
            current_storyline = choices[lua_chon - 1][1]
            print(current_storyline)
        if storyline[0] == 9:
            break
    current_storyline = 0
    for index in range(len(Story.chapter2)):
        if index < current_storyline:
            continue
        storyline = Story.chapter2[index]
        content = storyline[1]
        print(content)
        input()
