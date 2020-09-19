# http://ozzmaker.com/add-colour-to-text-in-python/
import os
import random
import time

from board import *
from getch import getch

wking = u'\u2654'
wqueen = u'\u2655'
wrock = u'\u2656'
wbishop = u'\u2657'
wknight = u'\u2658'
wpawn = u'\u2659'
bking = u'\u265a'
bqueen = u'\u265b'
brock = u'\u265c'
bbishop = u'\u265d'
bknight = u'\u265e'
bpawn = u'\u265f'
brick = u'\u2588'
res, color = [0, 0], [31, 32, 30]
play, checkMate, comPlayer, acDraw, aDraw, bigPlay, turn = True, False, False, False, False, True, False
bQueenSideCastle, bKingSideCastle, wQueenSideCastle, wKingSideCastle = True, True, True, True
enPassant, enPassantCol = False, 0
wKMoved, bKMoved = False, False
choice, canMove, cantMove, specMove = [], [], [], []
countDown = 50
num = -1
go, rowt, colt, row, col, c, r, rc, cc, rk, ck = '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
command = False
type = 'unicode'
board = [
    [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
    ['1', brock, bknight, bbishop, bqueen, bking, bbishop, bknight, brock],
    ['2', bpawn, bpawn, bpawn, bpawn, bpawn, bpawn, bpawn, bpawn],
    ['3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['4', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['5', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['6', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['7', wpawn, wpawn, wpawn, wpawn, wpawn, wpawn, wpawn, wpawn],
    ['8', wrock, wknight, wbishop, wqueen, wking, wbishop, wknight, wrock],
]
'''
board = [
  [' ','a','b','c','d','e','f','g','h'],
  ['1',' ',' ',' ',wking,' ',' ',' ',' '],
  ['2',' ',' ',' ',' ',wqueen,' ',' ',' '],
  ['3',' ',wpawn,' ',' ',wqueen,' ',' ',' '],
  ['4',bbishop,' ',' ',' ',' ',' ',' ',bbishop],
  ['5',' ',' ',' ',' ',' ',bbishop,' ',' '],
  ['6',' ',' ',' ',' ',' ',' ',' ',' '],
  ['7',' ',' ',' ',' ',' ',' ',' ',' '],
  ['8',' ',' ',bqueen,brock,' ',' ',' ',' '],
]
'''
danger = []
checkWay = []
for k in range(2):
    danger.append([])
    for i in range(9):
        danger[k].append([])
        for j in range(9):
            danger[k][i].append('o')
danger[0][0] = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
danger[1][0] = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for j in range(2):
    for i in range(1, 9):
        danger[j][i][0] = str(i)


def point(x):
    if x == wpawn:
        return 10
    elif x == wknight or x == wbishop:
        return 30
    elif x == wrock:
        return 50
    elif x == wqueen:
        return 90
    return 0


def gotoxy(x, y):
    print("\033[{};{}H".format(y, x), end='')


def printBoard(start, end, step):
    if type == 'unicode':
        for i in range(start, end, step):
            for j in range(start, end, step):
                if i < 1 or j < 1:
                    print("\033[0;37;40m{} ".format(board[i][j]), end='')
                else:
                    print('\033[1;{};{}m{} '.format(color[BW(board[i][j])], str(abs(i % 2 - j % 2) * -7 + 47),
                                                    board[i][j]), end='')
            print()
    else:
        for i in range(start, end, step):
            for j in range(start, end, step):
                p = board[i][j]
                x = ''
                if p in [wpawn, bpawn]:
                    x = pawn
                elif p in [wbishop, bbishop]:
                    x = bishop
                elif p in [wknight, bknight]:
                    x = knight
                elif p in [wrock, brock]:
                    x = rock
                elif p in [wqueen, bqueen]:
                    x = queen
                elif p in [wking, bking]:
                    x = king
                elif p >= '1' and p <= '8':
                    x = numbers[ord(p) - 49]
                    for k in range(len(x)):
                        gotoxy((j * 8), i * 4 + k + 1)
                        print("\033[0;37;40m{}".format(x[k]))
                    continue
                elif p >= 'a' and p <= 'h':
                    x = letters[ord(p) - 97]
                    for k in range(len(x)):
                        gotoxy((j * 8), i * 4 + k + 1)
                        print("\033[0;37;40m{}".format(x[k]))
                    continue
                elif i != 0 and j != 0:
                    x = space
                for k in range(len(x)):
                    gotoxy((j * 8), i * 4 + k + 1)
                    print('\033[1;{};{}m{} '.format(color[BW(p)], str(abs(i % 2 - j % 2) * -7 + 47), x[k]), end='')
    print("\033[0;37;40m")


def BW(x):
    if x < u'\u265a' and x >= u'\u2654':
        return 1
    elif x >= u'\u265a' and x <= u'\u265f':
        return 0
    else:
        return 2


def check(x, y, z):
    if board[x][y] == ' ' or BW(board[x][y]) == z:
        return 1
    else:
        return 0


def pawnMove(row, col, x):
    if BW(board[row][col]) == x:
        choice[num].append([row, col])


def knightMove(row, col, c, d, a, b, x, y, z):
    if (row + c) * x >= a * x and (col + d) * y >= b * y and check(row, col, z):
        choice[num].append([row, col])


def rockMove(row, col, a, b, c, d, z, king):
    if d != 0:
        tt = col
    else:
        tt = row
    if tt * a > b * a:
        x = row + c
        y = col + d
        if d == 0:
            t = x - c
        else:
            t = y - d
        while t * a >= b * a and check(x, y, z):
            choice[num].append([x, y])
            if BW(board[x][y]) == z and board[x][y] != ' ':
                if 1 <= x + c and x + c <= 8 and y + d >= 1 and y + d <= 8 and board[x][y] == king and board[x + c][
                    y + d] == ' ':
                    danger[z ^ 1][x + c][y + d] = 'x'
                break
            x += c
            y += d
            if d == 0:
                t = x
            else:
                t = y


def bishopMove(row, col, a, b, c, d, m, n, z, king):
    y = col + a
    x = row + b
    while y * c >= m * c and x * d >= n * d and check(x, y, z):
        choice[num].append([x, y])
        if BW(board[x][y]) == z and board[x][y] != ' ':
            if 1 <= x + b and x + b <= 8 and y + a >= 1 and y + a <= 8 and board[x][y] == king and board[x + b][
                y + a] == ' ':
                danger[z ^ 1][x + b][y + a] = 'x'
            break
        x += b
        y += a


def kingMove(row, col, x):
    if row >= 1 and row <= 8 and col >= 1 and col <= 8 and check(row, col, x) and danger[x][row][col] == 'o':
        choice[num].append([row, col])


def queenRockMove(z, king):
    rockMove(row, col, 1, 1, -1, 0, z, king)
    rockMove(row, col, -1, 8, 1, 0, z, king)
    rockMove(row, col, -1, 8, 0, 1, z, king)
    rockMove(row, col, 1, 1, 0, -1, z, king)


def queenBishopMove(z, king):
    bishopMove(row, col, -1, -1, 1, 1, 1, 1, z, king)
    bishopMove(row, col, -1, 1, 1, -1, 1, 8, z, king)
    bishopMove(row, col, 1, -1, -1, 1, 8, 1, z, king)
    bishopMove(row, col, 1, 1, -1, -1, 8, 8, z, king)


def valid(s, bw):
    global row, col, command, type, acDraw, aDraw, turn
    if s == 'board a':
        type = 'unicode'
        command = True
        return 0
    elif s == 'board b':
        type = 'ascii'
        command = True
        return 0
    elif s == 'color code':
        command = True
        aDraw = True
        print('COLOR CODE')
        print('Red 	31')
        print('Green 	32')
        print('Yellow 	33')
        print('Blue 	34')
        print('Purple 	35')
        print('Cyan 	36')
    elif s == 'board turn true':
        command = True
        turn = True
    elif s == 'board turn false':
        command = False
        turn = False
    elif len(s) >= 5:
        if len(s) == 11 and s[:8] in ['color.p1', 'color.p2'] and s[9:11].isnumeric() and s[8] == ' ' and int(
                s[9:11]) in range(31, 37) and int(s[9:11]) != color[int(s[7]) - 1]:
            command = True
            color[(int(s[7]) - 1) ^ 1] = int(s[9:11])
        elif s[:8] in ['color.p1', 'color.p2']:
            print('COLOR CODE')
            print('Red 	31')
            print('Green 	32')
            print('Yellow 	33')
            print('Blue 	34')
            print('Purple 	35')
            print('Cyan 	36')
    elif s == 'help':
        command = True
        aDraw = True
        print('  - board a')
        print('  - board b')
        print('  - board turn true | false')
        print('  - color.p? nn  | ? -> 1 or 2 (for P1 or P2) , nn -> 31-36')
        print('  - color code')
        print('  - draw')
    elif s == 'draw':
        command = True
        aDraw = True
        if not comPlayer:
            print('Draw?[y/n] ')
            while 1:
                c = getch()
                if c == 'y' or c == 'Y':
                    acDraw = True
                    return 0
                elif c == 'n' or c == 'N':
                    return 0
        else:
            acDraw = True
            print('Computer: Let me think! Just a moment!')
            time.sleep(2)
            print('Computer: I\'m just a newbie. I can decline to practice my skills')
            time.sleep(1.5)
            print('Computer: ...or not')
            time.sleep(1.5)
            print('Computer: Anyway, I cannot beat you')
            time.sleep(1)
            print('Computer: So I accept :)')
    if len(s) < 2 or not s[1].isnumeric():
        return False
    row = int(s[1])
    col = ord(s[0]) - 96
    if len(s) == 2 and s[0] >= 'a' and s[0] <= 'h' and s[1] >= '1' and s[1] <= '8' and BW(board[row][col]) == bw and \
            board[row][col] != ' ':
        return True
    else:
        return False


def validGo(s, bw):
    global rowt, colt
    if len(s) != 2 or not s[1].isnumeric():
        return False
    rowt = int(s[1])
    colt = ord(s[0]) - 96
    if len(s) == 2 and rowt >= 1 and rowt <= 8 and colt >= 1 and colt <= 8 and (
            BW(board[rowt][colt]) == bw or board[rowt][colt] == ' '):
        return True
    else:
        return False


def findPos(row, col):
    num = 0
    for i in choice:
        if [row, col] in i:
            break
        num += 1
    return num


def checkMateRock():
    if rc > r and cc == c:
        x, y = r + 1, c
        while x != rc:
            checkWay[len(checkWay) - 1].append([x, y])
            x += 1
    if rc < r and cc == c:
        x, y = r - 1, c
        while x != rc:
            checkWay[len(checkWay) - 1].append([x, y])
            x -= 1
    if cc > c and rc == r:
        x, y = r, c + 1
        while y != cc:
            checkWay[len(checkWay) - 1].append([x, y])
            y += 1
    if cc < c and rc == r:
        x, y = r, c - 1
        while y != cc:
            checkWay[len(checkWay) - 1].append([x, y])
            y -= 1


def checkMateBishop():
    if rc > r and cc > c:
        x, y = r + 1, c + 1
        while x != rc and y != cc:
            checkWay[len(checkWay) - 1].append([x, y])
            x += 1
            y += 1
    if rc < r and cc < c:
        x, y = r - 1, c - 1
        while x != rc and y != cc:
            checkWay[len(checkWay) - 1].append([x, y])
            x -= 1
            y -= 1
    if cc > c and rc < r:
        x, y = r - 1, c + 1
        while y != cc and x != rc:
            checkWay[len(checkWay) - 1].append([x, y])
            y += 1
            x -= 1
    if cc < c and rc > r:
        x, y = r + 1, c - 1
        while y != cc and x != rc:
            checkWay[len(checkWay) - 1].append([x, y])
            y -= 1
            x += 1


def funcBishop(z, king):
    specMove.append([])
    count = 0
    if rk > r and ck > c:
        x, y = r, c
        while x != rk and y != ck:
            if check(x, y, z) and board[x][y] != ' ':
                if count:
                    specMove.pop()
                    return 0
                specMove[len(specMove) - 1].insert(0, [x, y])
                count += 1
            elif not check(x, y, z) and (x != r or y != c):
                specMove.pop()
                return 0
            specMove[len(specMove) - 1].append([x, y])
            x += 1
            y += 1
        if not count:
            specMove.pop()
            return 0
    count = 0
    if rk < r and ck < c:
        x, y = r, c
        while x != rk and y != ck:
            if check(x, y, z) and board[x][y] != ' ':
                if count:
                    specMove.pop()
                    return 0
                specMove[len(specMove) - 1].insert(0, [x, y])
                count += 1
            elif not check(x, y, z) and (x != r or y != c):
                specMove.pop()
                return 0
            specMove[len(specMove) - 1].append([x, y])
            x -= 1
            y -= 1
        if not count:
            specMove.pop()
            return 0
    count = 0
    if ck > c and rk < r:
        x, y = r, c
        while x != rk and y != ck:
            if check(x, y, z) and board[x][y] != ' ':
                if count:
                    specMove.pop()
                    return 0
                print((specMove))
                specMove[len(specMove) - 1].insert(0, [x, y])
                count += 1
            elif not check(x, y, z) and (x != r or y != c):
                specMove.pop()
                return 0
            specMove[len(specMove) - 1].append([x, y])
            y += 1
            x -= 1
        if not count:
            specMove.pop()
            return 0
    count = 0
    if ck < c and rk > r:
        x, y = r, c
        while x != rk and y != ck:
            if check(x, y, z) and board[x][y] != ' ':
                if count:
                    specMove.pop()
                    return 0
                specMove[len(specMove) - 1].insert(0, [x, y])
                count += 1
            elif not check(x, y, z) and (x != r or y != c):
                specMove.pop()
                return 0
            specMove[len(specMove) - 1].append([x, y])
            y -= 1
            x += 1
        if not count:
            specMove.pop()


def funcRock(z, king):
    specMove.append([])
    count = 0
    if rk > r and ck == c:
        x, y = r, c
        while x != rk:
            if check(x, y, z) and board[x][y] != ' ':
                if count:
                    specMove.pop()
                    return 0
                specMove[len(specMove) - 1].insert(0, [x, y])
                count += 1
            elif not check(x, y, z) and (x != r or y != c):
                specMove.pop()
                return 0
            specMove[len(specMove) - 1].append([x, y])
            x += 1
        if not count:
            specMove.pop()
            return 0
    if rk < r and ck == c:
        x, y = r, c
        while x != rk:
            if check(x, y, z) and board[x][y] != ' ':
                if count:
                    specMove.pop()
                    return 0
                specMove[len(specMove) - 1].insert(0, [x, y])
                count += 1
            elif not check(x, y, z) and (x != r or y != c):
                specMove.pop()
                return 0
            specMove[len(specMove) - 1].append([x, y])
            x -= 1
        if not count:
            specMove.pop()
            return 0
    if ck > c and rk == r:
        x, y = r, c
        while y != ck:
            if check(x, y, z) and board[x][y] != ' ':
                if count:
                    specMove.pop()
                    return 0
                specMove[len(specMove) - 1].insert(0, [x, y])
                count += 1
            elif not check(x, y, z) and (x != r or y != c):
                specMove.pop()
                return 0
            specMove[len(specMove) - 1].append([x, y])
            y += 1
        if not count:
            specMove.pop()
            return 0
    if ck < c and rk == r:
        x, y = r, c
        while y != ck:
            if check(x, y, z) and board[x][y] != ' ':
                if count:
                    specMove.pop()
                    return 0
                specMove[len(specMove) - 1].insert(0, [x, y])
                count += 1
            elif not check(x, y, z) and (x != r or y != c):
                specMove.pop()
                return 0
            specMove[len(specMove) - 1].append([x, y])
            y -= 1
        if not count:
            specMove.pop()


def pawnDanger(row, col, x):
    if check(row, col, x ^ 1):
        danger[x][row][col] = 'x'


def knightDanger(row, col, c, d, a, b, x, y, z):
    if (row + c) * x >= a * x and (col + d) * y >= b * y and check(row, col, z ^ 1):
        danger[z ^ 1][row][col] = 'x'


def rockDanger(row, col, a, b, c, d, z, king):
    if d != 0:
        tt = col
    else:
        tt = row
    if tt * a > b * a:
        x = row + c
        y = col + d
        if d == 0:
            t = x - c
        else:
            t = y - d
        while t * a >= b * a and (check(x, y, z ^ 1) or board[x][y] == king):
            danger[z ^ 1][x][y] = 'x'
            if BW(board[x][y]) == z ^ 1 and board[x][y] != ' ':
                if 1 <= x + c and x + c <= 8 and y + d >= 1 and y + d <= 8 and board[x][y] == king and board[x + c][
                    y + d] == ' ':
                    danger[z ^ 1][x + c][y + d] = 'x'
                break
            x += c
            y += d
            if d == 0:
                t = x
            else:
                t = y


def bishopDanger(row, col, a, b, c, d, m, n, z, king):
    y = col + a
    x = row + b
    while y * c >= m * c and x * d >= n * d and (check(x, y, z ^ 1) or board[x][y] == king):
        danger[z ^ 1][x][y] = 'x'
        if BW(board[x][y]) == z ^ 1 and board[x][y] != ' ':
            if 1 <= x + b and x + b <= 8 and y + a >= 1 and y + a <= 8 and board[x][y] == king and board[x + b][
                y + a] == ' ':
                danger[z ^ 1][x + b][y + a] = 'x'
            break
        x += b
        y += a


def kingDanger(row, col, x):
    is_in_board = row >= 1 and row <= 8 and col >= 1 and col <= 8

    if is_in_board and check(row, col, x ^ 1) and (danger[x][row][col] == 'k' or danger[x][row][col] == 'o'):
        danger[x ^ 1][row][col] = 'k'


def queenRockDanger(z, king):
    rockDanger(row, col, 1, 1, -1, 0, z, king)
    rockDanger(row, col, -1, 8, 1, 0, z, king)
    rockDanger(row, col, -1, 8, 0, 1, z, king)
    rockDanger(row, col, 1, 1, 0, -1, z, king)


def queenBishopDanger(z, king):
    bishopDanger(row, col, -1, -1, 1, 1, 1, 1, z, king)
    bishopDanger(row, col, -1, 1, 1, -1, 1, 8, z, king)
    bishopDanger(row, col, 1, -1, -1, 1, 8, 1, z, king)
    bishopDanger(row, col, 1, 1, -1, -1, 8, 8, z, king)


def inCanMove(x):
    if x in canMove:
        return True
    return False


def inCheckWay(x):
    for j in checkWay:
        if x in j:
            return True
    return False


def canNotMove():
    for i in choice:
        if len(i) != 1:
            return False
    return True


def inSpecMove(x, y):
    for i in range(0, len(specMove)):
        if [x, y] == specMove[i][0]:
            return i + 1
    return 0


def draw():
    x = ' '
    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] not in [wking, bking]:
                if x != ' ':
                    return False
                x = board[i][j]
    if x in [wknight, wbishop, bknight, bbishop, ' ']:
        return True
    return False


def printPieces(x):
    for i in x:
        print(' ' * 3 + i)


chess = '''
                                                     _:_
                                                    '-.-'
                                           ()      __.'.__
                                        .-:--:-.  |_______|
                                 ()      \\____/    \\=====/
                                 /\\      {====}     )___(
                      (\\=,      //\\\      )__(     /_____\\
      __    |'-'-'|  //  .\\    (    )    /____\\     |   |
     /  \\   |_____| (( \\_  \\    )__(      |  |      |   |
     \\__/    |===|   ))  `\\_)  /____\\     |  |      |   |
    /____\\   |   |  (/     \\    |  |      |  |      |   |
     |  |    |   |   | _.-'|    |  |      |  |      |   |
     |__|    )___(    )___(    /____\\    /____\\    /_____\\
    (====)  (=====)  (=====)  (======)  (======)  (=======)
    }===={  }====={  }====={  }======{  }======{  }======={
   (______)(_______)(_______)(________)(________)(_________)

            ██████╗██╗  ██╗███████╗███████╗███████╗
           ██╔════╝██║  ██║██╔════╝██╔════╝██╔════╝
           ██║     ███████║█████╗  ███████╗███████╗
           ██║     ██╔══██║██╔══╝  ╚════██║╚════██║
           ╚██████╗██║  ██║███████╗███████║███████║
            ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝

'''
while bigPlay:
    print("\033[0;37;40m")
    os.system('clear')
    print(chess)
    name = ['', '']
    ch = ['       Human VS Human        ', ' Human VS Not-Smart-Computer ']
    choice, fore, back = 0, 0, 0
    while 1:
        for i in range(2):
            gotoxy(15, 27 + i)
            if choice == i:
                fore, back = 30, 47
            else:
                fore, back = 37, 40
            print("\033[1;{};{}m{}".format(fore, back, ch[i]))
        l = 1
        while 1:
            c = getch()
            if c == 'w' or c == 'W' or ord(c) == 65:
                choice = (choice + 1) % 2
                break
            elif c == 's' or c == 'S' or ord(c) == 66:
                choice = (choice + 3) % 2
                break
            elif ord(c) == 10:
                l = 0
                if choice == 1:
                    comPlayer = True
                else:
                    comPlayer = False
                break
        if not l:
            break
    print("\033[0;37;40m")
    print('                                ')
    for i in range(0, 1 + (not comPlayer)):
        C = ' '
        gotoxy(33, 27)
        print()
        gotoxy(25, 28)
        print(' ' * 10)
        gotoxy(15, 28)
        print(' ' * 28)
        gotoxy(15, 27)
        print('      Enter player{}\'s name:  '.format(i + 1))
        while ord(C) != 10:
            C = getch()
            if ((C >= 'a' and C <= 'z') or (C >= 'A' and C <= 'Z') or (C >= '0' and C <= '9')) and len(name[i]) < 8:
                name[i] += C
            if ord(C) == 127:
                if len(name[i]) != 0:
                    name[i] = name[i][:-1]
            gotoxy(0, 28)
            print(' ' * (29 - int(len(name[i]) / 2)) + name[i], '        ')
    if name[0] == '':
        name[0] = 'P1'
    if name[1] == '':
        name[1] = 'P2'
    if comPlayer:
        name[1] = 'Computer'
    gotoxy(0, 26)
    print(' ' * (30 - int(len(name[0]) / 2)), name[0], ' ' * 10)
    print(28 * ' ', '=VS=         ')
    print(' ' * (30 - int(len(name[1]) / 2)), name[1], ' ' * 10)
    if comPlayer:
        print('     Computer: It is the first time I play chess so forgive me if I play badly!')
    input('\n                    Press ENTER to continue')
    print('Before we start, would you like to see the instruction?[y/n] ')
    while 1:
        c = getch()
        if c == 'y' or c == 'n' or c == 'Y' or c == 'N':
            if c == 'y' or c == 'Y':
                os.system('clear')
                print(
                    ' I/Move: \n  1. White always moves first, and players alternate turns. Players can only move one piece at a time, except when castling.')
                print('  2. Pieces:')
                print('   a. Unicode Pieces:')
                print('    {} Pawn'.format(wpawn))
                print('    {} Knight'.format(wknight))
                print('    {} Bishop'.format(wbishop))
                print('    {} Rock'.format(wrock))
                print('    {} Queen'.format(wqueen))
                print('    {} King'.format(wking))
                print('   b. ASCII Pieces:')
                print('    Pawn')
                printPieces(pawn)
                print('    Knight')
                printPieces(knight)
                print('    Bishop')
                printPieces(bishop)
                print('    Rock')
                printPieces(rock)
                print('    Queen')
                printPieces(rock)
                print('    King')
                printPieces(king)
                print(
                    '  * Use \'board a\' to convert to Unicode board and \'board b\' to convert to ASCII board (See 3b)')
                print('  3. How to play')
                print('   a. Move')
                print(
                    '    First enter the coordinates to choose you piece. Then enter the next coordinates to move your piece (which you have chosen) to there. Example:')
                type = 'unicode'
                printBoard(0, 9, 1)
                print('  Enter the d7 to choose the pawn at d7, then choose d5 to move your pawn to d5')
                print('   b. Command')
                print('    You can modify your board with some commands are listed below')
                print('    - board a')
                print('    - board b')
                print('    - board turn true | false')
                print('    - color.p? nn  | ? -> 1 or 2 (for P1 or P2) , nn -> 31-36')
                print('    - color code')
                print('    - draw')
                print(' II/Rules:\n   The rules is so long so it\'s impossible to display it here :( Visit:')
                print(
                    '   https://www.instructables.com/id/Playing-Chess/ \n   https://en.wikipedia.org/wiki/Chess#Rules')
                input('\nPress ENTER to continue')
                break
            elif c == 'n' or c == 'N':
                break
    os.system('clear')
    play = True
    while play:
        board = [
            [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
            ['1', brock, bknight, bbishop, bqueen, bking, bbishop, bknight, brock],
            ['2', bpawn, bpawn, bpawn, bpawn, bpawn, bpawn, bpawn, bpawn],
            ['3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['4', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['5', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['6', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['7', wpawn, wpawn, wpawn, wpawn, wpawn, wpawn, wpawn, wpawn],
            ['8', wrock, wknight, wbishop, wqueen, wking, wbishop, wknight, wrock],
        ]
        while 1:
            os.system("clear")
            num = -1
            choice = []
            printBoard(0, 9, 1)
            if checkMate:
                print('Checkmate! ')
            wC = False
            for row in range(1, 9):
                for col in range(1, 9):
                    val = board[row][col]
                    if val == wpawn:
                        num += 1
                        choice.append([[row, col]])
                        if board[row - 1][col] == ' ':
                            choice[num].append([row - 1, col])
                            if row == 7:
                                if board[row - 2][col] == ' ':
                                    choice[num].append([row - 2, col])
                        if col > 1:
                            pawnMove(row - 1, col - 1, 0)
                        if col < 8:
                            pawnMove(row - 1, col + 1, 0)
                        if row == 4 and enPassant and abs(enPassantCol - col) == 1:
                            choice[num].append([3, enPassantCol])
                    elif val == wknight:
                        num += 1
                        choice.append([[row, col]])
                        knightMove(row - 2, col - 1, 2, 1, 3, 2, 1, 1, 0)
                        knightMove(row - 2, col + 1, 2, -1, 3, 7, 1, -1, 0)
                        knightMove(row - 1, col - 2, 1, 2, 2, 3, 1, 1, 0)
                        knightMove(row - 1, col + 2, 1, -2, 2, 6, 1, -1, 0)
                        knightMove(row + 2, col - 1, -2, 1, 6, 2, -1, 1, 0)
                        knightMove(row + 1, col - 2, -1, 2, 7, 3, -1, 1, 0)
                        knightMove(row + 2, col + 1, -2, -1, 6, 7, -1, -1, 0)
                        knightMove(row + 1, col + 2, -1, -2, 7, 6, -1, -1, 0)
                    elif val == wrock:
                        num += 1
                        choice.append([[row, col]])
                        queenRockMove(0, bking)
                    elif val == wbishop:
                        num += 1
                        choice.append([[row, col]])
                        queenBishopMove(0, bking)
                    elif val == wqueen:
                        num += 1
                        choice.append([[row, col]])
                        queenRockMove(0, bking)
                        queenBishopMove(0, bking)
                    elif val == wking:
                        num += 1
                        choice.append([[row, col]])
                        if not checkMate and not wKMoved:
                            if wKingSideCastle and danger[0][8][6] == 'o' and danger[0][8][7] == 'o' and board[8][
                                6] == ' ' and board[8][7] == ' ':
                                choice[num].append([8, 7])
                            if wQueenSideCastle and danger[0][8][4] == 'o' and danger[0][8][3] == 'o' and board[8][
                                4] == ' ' and board[8][3] == ' ':
                                choice[num].append([8, 3])
                        kingMove(row + 1, col + 1, 0)
                        kingMove(row + 1, col, 0)
                        kingMove(row + 1, col - 1, 0)
                        kingMove(row, col + 1, 0)
                        kingMove(row, col - 1, 0)
                        kingMove(row - 1, col + 1, 0)
                        kingMove(row - 1, col, 0)
                        kingMove(row - 1, col - 1, 0)
                        if len(choice[num]) != 1 and checkMate:
                            checkMate = False
                            wC = True
                    if inSpecMove(row, col) and check(row, col, 0):
                        templist = []
                        for i in choice[num]:
                            if i in specMove[inSpecMove(row, col) - 1]:
                                templist.append([row, col])
                        choice[num] = templist.copy()
            enPassant = False
            canMove = []
            if wC or checkMate:
                for i in choice:
                    for j in i:
                        length = len(checkWay)
                        k = 0
                        while k < length:
                            if j in checkWay[k] and board[i[0][0]][i[0][1]] != wking:
                                canMove.append([i[0][0], i[0][1]])
                                break
                            elif board[i[0][0]][i[0][1]] == wking:
                                if len(i) != 1:
                                    canMove.append([i[0][0], i[0][1]])
                                break
                            k += 1
                if len(canMove) != 0 and not len(checkWay) >= 2:
                    checkMate = False
                    wC = True
            if len(checkWay) >= 2 and checkMate:
                for i in range(1, 9):
                    for j in range(1, 9):
                        if board[i][j] == wking:
                            if len(choice[findPos(i, j)]) == 1:
                                break
                            canMove = [i, j]
                            checkMate = False
                            wC = True
                            break
            if checkMate:
                print('{} WIN!'.format(name[1]))
                res[1] += 1
                input('Press enter to continue!')
                break
            elif canNotMove() or not countDown or draw():
                print('DRAW!')
                input('Press enter to continue!')
                break
            d = False
            go = input(
                '{}\'s turn! Enter the coordinates(Ex: a3, h4...) or command(type \'help\' to see command list)! Be careful, you cannot undo! '.format(
                    name[0]))
            while not valid(go, 1):
                if not command:
                    print('Invalid! Please try again! ', end='')
                elif not aDraw:
                    print('Your change will be applied soon! Now enter a command or coordinates! ', end='')
                elif not acDraw:
                    aDraw = False
                    print('Now enter a command or coordinates! ')
                else:
                    print('DRAW! ')
                    print('Press ENTER to continue!')
                    acDraw = False
                    aDraw = False
                    command = False
                    input()
                    d = True
                    break
                acDraw = False
                aDraw = False
                command = False
                go = input()
            if d:
                break
            num = findPos(row, col)
            while len(choice[num]) == 1 or (wC and not inCanMove([row, col])):
                go = input('Can\'t move! Please try again! ')
                while not valid(go, 1):
                    if not command:
                        print('Invalid! Please try again! ', end='')
                    elif not aDraw:
                        print('Your change will be applied soon! Now enter a command or coordinates! ', end='')
                    elif not acDraw:
                        print('Now enter a command or coordinates! ')
                    else:
                        print('DRAW! ')
                        print('Press ENTER to continue!')
                        input()
                        acDraw = False
                        aDraw = False
                        command = False
                        break
                    acDraw = False
                    aDraw = False
                    command = False
                    go = input()
                num = findPos(row, col)
            print('Your choice', board[row][col])
            go = input('Pick a place to move to. Enter the coordinates(Ex: e3, h4...) ')
            validGo(go, 0)
            num = findPos(row, col)
            while [rowt, colt] not in choice[num] or (rowt == row and colt == col) or (
                    wC and not inCheckWay([rowt, colt]) and board[row][col] != wking):
                go = input('Invalid! Please try again! ')
                while not validGo(go, 0):
                    go = input('Invalid! Please try again! ')
                    num = findPos(row, col)
                num = findPos(row, col)
            if board[row][col] == wking and abs(colt - col) == 2:
                board[8][1 + (colt > col) * 7] = ' '
                board[8][4 + (colt > col) * 2] = wrock
            if board[row][col] == wpawn and rowt == 3 and colt == enPassantCol:
                board[4][enPassantCol] = ' '
            if board[row][col] == wrock:
                if row == 8 and col == 8:
                    wKingSideCastle = False
                elif row == 8 and col == 1:
                    wQueenSideCastle = False
            elif board[row][col] == wking:
                wKMoved = True
            elif board[row][col] == wpawn and row == 7 and rowt == 5:
                enPassant = True
                enPassantCol = col
            if board[rowt][colt] == ' ' and board[row][col] != wpawn:
                countDown -= 1
            else:
                countDown = 50
            board[rowt][colt] = board[row][col]
            board[row][col] = ' '
            if rowt == 1 and board[rowt][colt] == wpawn:
                print('Promote your Pawn: ')
                print('1. Queen')
                print('2. Rock')
                print('3. Bishop')
                print('4. Knight')
                choice = '01'
                while len(choice) != 1 or choice < '1' or choice > '4':
                    choice = input('Enter your choice (1-4): ')
                if choice == '1':
                    board[rowt][colt] = wqueen
                if choice == '2':
                    board[rowt][colt] = wrock
                if choice == '3':
                    board[rowt][colt] = wbishop
                if choice == '4':
                    board[rowt][colt] = wknight
            specMove = []
            for i in range(1, 9):
                for j in range(1, 9):
                    if board[i][j] == bbishop:
                        if abs(i - rk) == abs(j - ck):
                            r, c = i, j
                            funcBishop(1, wking)
                    elif board[i][j] == brock:
                        if i == rk or ck == j:
                            r, c = i, j
                            funcRock(1, wking)
                    elif board[i][j] == bqueen:
                        if abs(i - rk) == abs(j - ck):
                            r, c = i, j
                            funcBishop(1, wking)
                        if i == rk or ck == j:
                            r, c = i, j
                            funcRock(1, wking)
            choice, num = [], -1
            for row in range(1, 9):
                for col in range(1, 9):
                    val = board[row][col]
                    if val == wpawn:
                        num += 1
                        choice.append([[row, col]])
                        if board[row - 1][col] == ' ':
                            choice[num].append([row - 1, col])
                            if row == 7:
                                if board[row - 2][col] == ' ':
                                    choice[num].append([row - 2, col])
                        if col > 1:
                            pawnMove(row - 1, col - 1, 0)
                        if col < 8:
                            pawnMove(row - 1, col + 1, 0)
                        if row == 5 and enPassant and abs(enPassantCol - col) == 1:
                            choice[num].append([4, enPassantCol])
                            enPassant = False
                    elif val == wknight:
                        num += 1
                        choice.append([[row, col]])
                        knightMove(row - 2, col - 1, 2, 1, 3, 2, 1, 1, 0)
                        knightMove(row - 2, col + 1, 2, -1, 3, 7, 1, -1, 0)
                        knightMove(row - 1, col - 2, 1, 2, 2, 3, 1, 1, 0)
                        knightMove(row - 1, col + 2, 1, -2, 2, 6, 1, -1, 0)
                        knightMove(row + 2, col - 1, -2, 1, 6, 2, -1, 1, 0)
                        knightMove(row + 1, col - 2, -1, 2, 7, 3, -1, 1, 0)
                        knightMove(row + 2, col + 1, -2, -1, 6, 7, -1, -1, 0)
                        knightMove(row + 1, col + 2, -1, -2, 7, 6, -1, -1, 0)
                    elif val == wrock:
                        num += 1
                        choice.append([[row, col]])
                        queenRockMove(0, bking)
                    elif val == wbishop:
                        num += 1
                        choice.append([[row, col]])
                        queenBishopMove(0, bking)
                    elif val == wqueen:
                        num += 1
                        choice.append([[row, col]])
                        queenRockMove(0, bking)
                        queenBishopMove(0, bking)
                    elif val == wking:
                        num += 1
                        choice.append([[row, col]])
                        kingMove(row + 1, col + 1, 0)
                        kingMove(row + 1, col, 0)
                        kingMove(row + 1, col - 1, 0)
                        kingMove(row, col + 1, 0)
                        kingMove(row, col - 1, 0)
                        kingMove(row - 1, col + 1, 0)
                        kingMove(row - 1, col, 0)
                        kingMove(row - 1, col - 1, 0)
                    if inSpecMove(row, col) and check(row, col, 1):
                        templist = []
                        for i in choice[num]:
                            if i in specMove[inSpecMove(row, col) - 1]:
                                templist.append([row, col])
                        choice[num] = templist.copy()
            for i in range(1, 9):
                for j in range(1, 9):
                    danger[1][i][j] = 'o'
            for row in range(1, 9):
                for col in range(1, 9):
                    val = board[row][col]
                    if val == wking:
                        kingDanger(row + 1, col + 1, 0)
                        kingDanger(row + 1, col, 0)
                        kingDanger(row + 1, col - 1, 0)
                        kingDanger(row, col + 1, 0)
                        kingDanger(row, col - 1, 0)
                        kingDanger(row - 1, col + 1, 0)
                        kingDanger(row - 1, col, 0)
                        kingDanger(row - 1, col - 1, 0)
                    elif val == wpawn:
                        if col > 1:
                            pawnDanger(row - 1, col - 1, 1)
                        if col < 8:
                            pawnDanger(row - 1, col + 1, 1)
                    elif val == wknight:
                        knightDanger(row - 2, col - 1, 2, 1, 3, 2, 1, 1, 0)
                        knightDanger(row - 2, col + 1, 2, -1, 3, 7, 1, -1, 0)
                        knightDanger(row - 1, col - 2, 1, 2, 2, 3, 1, 1, 0)
                        knightDanger(row - 1, col + 2, 1, -2, 2, 6, 1, -1, 0)
                        knightDanger(row + 2, col - 1, -2, 1, 6, 2, -1, 1, 0)
                        knightDanger(row + 1, col - 2, -1, 2, 7, 3, -1, 1, 0)
                        knightDanger(row + 2, col + 1, -2, -1, 6, 7, -1, -1, 0)
                        knightDanger(row + 1, col + 2, -1, -2, 7, 6, -1, -1, 0)
                    elif val == wrock:
                        queenRockDanger(0, bking)
                    elif val == wbishop:
                        queenBishopDanger(0, bking)
                    elif val == wqueen:
                        queenRockDanger(0, bking)
                        queenBishopDanger(0, bking)
                    elif val == bking:
                        rk, ck = row, col
            checkWay = []
            for i in choice:
                for j in range(1, len(i)):
                    r, c = i[0][0], i[0][1]
                    val = board[r][c]
                    rc, cc = i[j][0], i[j][1]
                    if board[rc][cc] == bking:
                        checkMate = True
                        checkWay.append([[r, c]])
                        if val == wrock:
                            checkMateRock()
                        elif val == wbishop:
                            checkMateBishop()
                        elif val == wqueen:
                            checkMateRock()
                            checkMateBishop()
            #########################################
            os.system("clear")
            num = -1
            choice = []
            if turn:
                printBoard(8, -1, -1)
            else:
                printBoard(0, 9, 1)
            if checkMate:
                print('Checkmate! ')
            wC = False
            specMove = []
            for i in range(1, 9):
                for j in range(1, 9):
                    if board[i][j] == wbishop:
                        if abs(i - rk) == abs(j - ck):
                            r, c = i, j
                            funcBishop(0, bking)
                    elif board[i][j] == wrock:
                        if i == rk or ck == j:
                            r, c = i, j
                            funcRock(0, bking)
                    elif board[i][j] == wqueen:
                        if abs(i - rk) == abs(j - ck):
                            r, c = i, j
                            funcBishop(0, bking)
                        if i == rk or ck == j:
                            r, c = i, j
                            funcRock(0, bking)
            for row in range(1, 9):
                for col in range(1, 9):
                    val = board[row][col]
                    if val == bking:
                        rk, ck = row, col
                        num += 1
                        choice.append([[row, col]])
                        if not checkMate and not bKMoved:
                            if bKingSideCastle and danger[1][1][6] == 'o' and danger[1][1][7] == 'o' and board[1][
                                6] == ' ' and board[1][7] == ' ':
                                choice[num].append([1, 7])
                            if bQueenSideCastle and danger[1][1][4] == 'o' and danger[1][1][3] == 'o' and board[1][
                                4] == ' ' and board[1][3] == ' ':
                                choice[num].append([1, 3])
                        kingMove(row + 1, col + 1, 1)
                        kingMove(row + 1, col, 1)
                        kingMove(row + 1, col - 1, 1)
                        kingMove(row, col + 1, 1)
                        kingMove(row, col - 1, 1)
                        kingMove(row - 1, col + 1, 1)
                        kingMove(row - 1, col, 1)
                        kingMove(row - 1, col - 1, 1)
                        if checkMate and len(choice[num]) != 1:
                            checkMate = False
                            wC = True
                    elif val == bpawn:
                        num += 1
                        choice.append([[row, col]])
                        if board[row + 1][col] == ' ':
                            choice[num].append([row + 1, col])
                            if row == 2 and board[row + 2][col] == ' ':
                                choice[num].append([row + 2, col])
                        if col > 1:
                            pawnMove(row + 1, col - 1, 1)
                        if col < 8:
                            pawnMove(row + 1, col + 1, 1)
                        if row == 5 and enPassant and abs(enPassantCol - col) == 1:
                            choice[num].append([6, enPassantCol])
                    elif val == bknight:
                        num += 1
                        choice.append([[row, col]])
                        knightMove(row - 2, col - 1, 2, 1, 3, 2, 1, 1, 1)
                        knightMove(row - 2, col + 1, 2, -1, 3, 7, 1, -1, 1)
                        knightMove(row - 1, col - 2, 1, 2, 2, 3, 1, 1, 1)
                        knightMove(row - 1, col + 2, 1, -2, 2, 6, 1, -1, 1)
                        knightMove(row + 2, col - 1, -2, 1, 6, 2, -1, 1, 1)
                        knightMove(row + 1, col - 2, -1, 2, 7, 3, -1, 1, 1)
                        knightMove(row + 2, col + 1, -2, -1, 6, 7, -1, -1, 1)
                        knightMove(row + 1, col + 2, -1, -2, 7, 6, -1, -1, 1)
                    elif val == brock:
                        num += 1
                        choice.append([[row, col]])
                        queenRockMove(1, wking)
                    elif val == bbishop:
                        num += 1
                        choice.append([[row, col]])
                        queenBishopMove(1, wking)
                    elif val == bqueen:
                        num += 1
                        choice.append([[row, col]])
                        queenRockMove(1, wking)
                        queenBishopMove(1, wking)
                    if inSpecMove(row, col) and check(row, col, 0):
                        templist = []
                        for i in choice[num]:
                            if i in specMove[inSpecMove(row, col) - 1]:
                                templist.append([row, col])
                        choice[num] = templist.copy()
            enPassant = False
            canMove = []
            if wC or checkMate:
                for i in choice:
                    for j in i:
                        length = len(checkWay)
                        k = 0
                        while k < length:
                            if j in checkWay[k] and board[i[0][0]][i[0][1]] != bking:
                                canMove.append([i[0][0], i[0][1]])
                                break
                            elif board[i[0][0]][i[0][1]] == bking:
                                if len(i) != 1:
                                    canMove.append([i[0][0], i[0][1]])
                                break
                            k += 1
                if len(canMove) != 0 and not len(checkWay) >= 2:
                    checkMate = False
                    wC = True
            if len(checkWay) >= 2 and checkMate:
                for i in range(1, 9):
                    for j in range(1, 9):
                        if board[i][j] == wking:
                            if len(choice[findPos(i, j)]) == 1:
                                break
                            canMove = [i, j]
                            checkMate = False
                            wC = True
                            break
            if checkMate:
                print('{} WIN!'.format(name[0]))
                res[0] += 1
                input('Press ENTER to continue!')
                break
            elif canNotMove() or not countDown or draw():
                print('Draw')
                input('Press ENTER to continue!')
                break
                '''
              for j in danger:
                for i in j:
                  print(i)
                print()
              '''
            if not comPlayer:
                d = False
                go = input(
                    '{}\'s turn! Enter the coordinates(Ex: a3, h4...) or command(type \'help\' to see command list)! Be careful, you cannot undo! '.format(
                        name[1]))
                while not valid(go, 0):
                    if not command:
                        print('Invalid! Please try again! ', end='')
                    elif not aDraw:
                        print('Your change will be applied soon! Now enter a command or coordinates! ', end='')
                    elif not acDraw:
                        print('Now enter a command or coordinates! ')
                    else:
                        print('DRAW! ')
                        print('Press ENTER to continue!')
                        input()
                        acDraw = False
                        aDraw = False
                        command = False
                        d = True
                        break
                    acDraw = False
                    aDraw = False
                    command = False
                    go = input()
                if d:
                    break
                num = findPos(row, col)
                while len(choice[num]) == 1 or (wC and not inCanMove([row, col])):
                    go = input('Can\'t move! Please try again! ')
                    while not valid(go, 0):
                        if not command:
                            print('Invalid! Please try again! ', end='')
                        elif not aDraw:
                            print('Your change will be applied soon! Now enter a command or coordinates! ', end='')
                        elif not acDraw:
                            print('Now enter a command or coordinates! ')
                        else:
                            print('DRAW! ')
                            print('Press ENTER to continue!')
                            acDraw = False
                            aDraw = False
                            command = False
                            input()
                            break
                        acDraw = False
                        aDraw = False
                        command = False
                        go = input()
                    num = findPos(row, col)
                print('Your choice', board[row][col])
                go = input('Pick a place to move to. Enter the coordinates(Ex: e3, h4...) ')
                validGo(go, 1)
                num = findPos(row, col)
                while [rowt, colt] not in choice[num] or (rowt == row and colt == col) or (
                        wC and not inCheckWay([rowt, colt]) and board[row][col] != bking):
                    go = input('Invalid! Please try again! ')
                    while not validGo(go, 1):
                        go = input('Invalid! Please try again! ')
                        num = findPos(row, col)
                    num = findPos(row, col)
            else:
                for i in danger:
                    for j in i:
                        print(j)
                    print()
                input()
                max = -1
                canmove = []
                for i in choice:
                    for j in range(1, len(i)):
                        tRow, tCol, tRowt, tColt = i[0][0], i[0][1], i[j][0], i[j][1]
                        temp = (wC and not inCanMove([tRow, tCol]))
                        temp2 = ((tRowt == tRow and tColt == tCol) or (
                                    wC and not inCheckWay([tRowt, tColt]) and board[tRow][tCol] != bking))
                        if point(board[tRowt][tColt]) > max and not (temp or temp2):
                            max = point(board[i[j][0]][i[j][1]])
                            canmove = [[i[0][0], i[0][1], i[j][0], i[j][1]]]
                        elif point(board[i[j][0]][i[j][1]]) == max and not (temp or temp2):
                            canmove.append([i[0][0], i[0][1], i[j][0], i[j][1]])
                row, col, rowt, colt = canmove[random.randint(0, len(canmove) - 1)]
                print('I will move {} from {}{} to {}{}'.format(board[row][col], chr(col + 96), row, chr(colt + 96),
                                                                rowt))
                time.sleep(3)
            if board[row][col] == wpawn and rowt == 3 and colt == enPassantCol:
                board[5][enPassantCol] = ' '
            if board[row][col] == bking and abs(colt - col) == 2:
                board[1][1 + (colt > col) * 7] = ' '
                board[1][4 + (colt > col) * 2] = brock
            if board[row][col] == brock:
                if row == 1 and col == 8:
                    bKingSideCastle = False
                elif row == 1 and col == 1:
                    bQueenSideCastle = False
            elif board[row][col] == bking:
                bKMoved = True
            elif board[row][col] == bpawn and row == 2 and rowt == 4:
                enPassant = True
                enPassantCol = col
            if board[rowt][colt] == ' ' and board[row][col] != wpawn:
                countDown -= 1
            else:
                countDown = 50
            board[rowt][colt] = board[row][col]
            board[row][col] = ' '
            if rowt == 8 and board[rowt][colt] == bpawn:
                print('Promote your Pawn: ')
                print('1. Queen')
                print('2. Rock')
                print('3. Bishop')
                print('4. Knight')
                choice = '01'
                while len(choice) != 1 or choice < '1' or choice > '4':
                    choice = input('Enter your choice (1-4): ')
                if choice == '1':
                    board[rowt][colt] = bqueen
                if choice == '2':
                    board[rowt][colt] = brock
                if choice == '3':
                    board[rowt][colt] = bbishop
                if choice == '4':
                    board[rowt][colt] = bknight
            specMove = []
            for i in range(1, 9):
                for j in range(1, 9):
                    if board[i][j] == wbishop:
                        if abs(i - rk) == abs(j - ck):
                            r, c = i, j
                            funcBishop(0, bking)
                    elif board[i][j] == wrock:
                        if i == rk or ck == j:
                            r, c = i, j
                            funcRock(0, bking)
                    elif board[i][j] == wqueen:
                        if abs(i - rk) == abs(j - ck):
                            r, c = i, j
                            funcBishop(0, bking)
                        if i == rk or ck == j:
                            r, c = i, j
                            funcRock(0, bking)
            choice = []
            num, choice = -1, []
            for row in range(1, 9):
                for col in range(1, 9):
                    val = board[row][col]
                    if val == bpawn:
                        num += 1
                        choice.append([[row, col]])
                        if board[row + 1][col] == ' ':
                            choice[num].append([row + 1, col])
                            if row == 2 and board[row + 2][col] == ' ':
                                choice[num].append([row + 2, col])
                        if col > 1:
                            pawnMove(row + 1, col - 1, 1)
                        if col < 8:
                            pawnMove(row + 1, col + 1, 1)
                    elif val == bknight:
                        num += 1
                        choice.append([[row, col]])
                        knightMove(row - 2, col - 1, 2, 1, 3, 2, 1, 1, 1)
                        knightMove(row - 2, col + 1, 2, -1, 3, 7, 1, -1, 1)
                        knightMove(row - 1, col - 2, 1, 2, 2, 3, 1, 1, 1)
                        knightMove(row - 1, col + 2, 1, -2, 2, 6, 1, -1, 1)
                        knightMove(row + 2, col - 1, -2, 1, 6, 2, -1, 1, 1)
                        knightMove(row + 1, col - 2, -1, 2, 7, 3, -1, 1, 1)
                        knightMove(row + 2, col + 1, -2, -1, 6, 7, -1, -1, 1)
                        knightMove(row + 1, col + 2, -1, -2, 7, 6, -1, -1, 1)
                    elif val == brock:
                        num += 1
                        choice.append([[row, col]])
                        queenRockMove(1, wking)
                    elif val == bbishop:
                        num += 1
                        choice.append([[row, col]])
                        queenBishopMove(1, wking)
                    elif val == bqueen:
                        num += 1
                        choice.append([[row, col]])
                        queenRockMove(1, wking)
                        queenBishopMove(1, wking)
                    elif val == bking:
                        num += 1
                        choice.append([[row, col]])
                        kingMove(row + 1, col + 1, 1)
                        kingMove(row + 1, col, 1)
                        kingMove(row + 1, col - 1, 1)
                        kingMove(row, col + 1, 1)
                        kingMove(row, col - 1, 1)
                        kingMove(row - 1, col + 1, 1)
                        kingMove(row - 1, col, 1)
                        kingMove(row - 1, col - 1, 1)
                    if inSpecMove(row, col) and check(row, col, 1):
                        templist = []
                        for i in choice[num]:
                            if i in specMove[inSpecMove(row, col) - 1]:
                                templist.append([row, col])
                        choice[num] = templist.copy()
            for i in range(1, 9):
                for j in range(1, 9):
                    danger[0][i][j] = 'o'
            for row in range(1, 9):
                for col in range(1, 9):
                    val = board[row][col]
                    if val == bking:
                        kingDanger(row + 1, col + 1, 1)
                        kingDanger(row + 1, col, 1)
                        kingDanger(row + 1, col - 1, 1)
                        kingDanger(row, col + 1, 1)
                        kingDanger(row, col - 1, 1)
                        kingDanger(row - 1, col + 1, 1)
                        kingDanger(row - 1, col, 1)
                        kingDanger(row - 1, col - 1, 1)
                    elif val == bpawn:
                        if col > 1:
                            pawnDanger(row - 1, col - 1, 1)
                        if col < 8:
                            pawnDanger(row - 1, col + 1, 1)
                    elif val == bknight:
                        knightDanger(row - 2, col - 1, 2, 1, 3, 2, 1, 1, 1)
                        knightDanger(row - 2, col + 1, 2, -1, 3, 7, 1, -1, 1)
                        knightDanger(row - 1, col - 2, 1, 2, 2, 3, 1, 1, 1)
                        knightDanger(row - 1, col + 2, 1, -2, 2, 6, 1, -1, 1)
                        knightDanger(row + 2, col - 1, -2, 1, 6, 2, -1, 1, 1)
                        knightDanger(row + 1, col - 2, -1, 2, 7, 3, -1, 1, 1)
                        knightDanger(row + 2, col + 1, -2, -1, 6, 7, -1, -1, 1)
                        knightDanger(row + 1, col + 2, -1, -2, 7, 6, -1, -1, 1)
                    elif val == brock:
                        queenRockDanger(1, wking)
                    elif val == bbishop:
                        queenBishopDanger(1, wking)
                    elif val == bqueen:
                        queenRockDanger(1, wking)
                        queenBishopDanger(1, wking)
                    elif val == wking:
                        rk, ck = row, col
            checkWay = []
            for i in choice:
                for j in range(1, len(i)):
                    r, c = i[0][0], i[0][1]
                    val = board[r][c]
                    rc, cc = i[j][0], i[j][1]
                    if board[rc][cc] == wking:
                        checkMate = True
                        checkWay.append([[r, c]])
                        if val == brock:
                            checkMateRock()
                        elif val == bbishop:
                            checkMateBishop()
                        elif val == bqueen:
                            checkMateRock()
                            checkMateBishop()
            specMove = []
            for i in range(1, 9):
                for j in range(1, 9):
                    if board[i][j] == bbishop:
                        if abs(i - rk) == abs(j - ck):
                            r, c = i, j
                            funcBishop(1, wking)
                    elif board[i][j] == brock:
                        if i == rk or ck == j:
                            r, c = i, j
                            funcRock(1, wking)
                    elif board[i][j] == bqueen:
                        if abs(i - rk) == abs(j - ck):
                            r, c = i, j
                            funcBishop(1, wking)
                        if i == rk or ck == j:
                            r, c = i, j
                            funcRock(1, wking)
        os.system("clear")
        print('Result: {} {} - {} {} '.format(name[0], res[0], res[1], name[1]))
        Choice, fore, back = 0, 0, 0
        pr = ['NEW GAME    ', 'PLAY AGAIN  ', 'EXIT        ']
        l = 1
        while l:
            gotoxy(0, 2)
            for i in range(3):
                if Choice == i:
                    fore, back = 30, 47
                else:
                    fore, back = 37, 40
                print("\033[1;{};{}m{}".format(fore, back, pr[i]))
            while 1:
                c = getch()
                if c == 'w' or c == 'W' or ord(c) == 65:
                    Choice = (Choice + 2) % 3
                    break
                elif c == 's' or c == 'S' or ord(c) == 66:
                    Choice = (Choice + 4) % 3
                    break
                elif ord(c) == 10:
                    l = 0
                    break
        if Choice in [0, 1]:
            play, bigPlay, checkMate = True, True, False
            bQueenSideCastle, bKingSideCastle, wQueenSideCastle, wKingSideCastle = True, True, True, True
            enPassant, enPassantCol = False, 0
            wKMoved, bKMoved = False, False
            choice, canMove, cantMove, specMove = [], [], [], []
            countDown = 50
            num = -1
            go, rowt, colt, row, col, c, r, rc, cc, rk, ck = '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            for i in danger:
                for j in range(1, 9):
                    for k in range(1, 9):
                        i[j][k] = 'o'
            if Choice == 0:
                play = False
        else:
            play = False
            bigPlay = False
