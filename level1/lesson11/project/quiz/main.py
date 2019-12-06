import random
import time

YES = ['y', 'Y', 'yes', 'Yes', 'YES']
NO = ['n', 'N', 'no', 'No', 'NO']
CLEAR = ['c', 'C', 'clear', 'Clear', 'CLEAR']
QUIT = ['q', 'Q', 'quit', 'Quit', 'QUIT']
MULTIPLECHOICE = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']


class QuizGame:
    '''  repository of methods to do with QuizGame
         -  get_username
         -  play_loop
         -  ask_play_again
         -  escape_quiz
         -  play_quiz
         -  read_highscores
         -  write_highscores
         -  clear_highscores
         -  display_highscores
    '''
    questions = \
        {1: ('Bánh chưng hình chữ nhật, hình vuông hay hình tam giác?',
             'a)  Hình chữ nhật\nb)  Hình vuông \nc)  Hình tam giác \nd)  Tùy người làm bánh',
             'd'),

         2: ('Theo truyền thuyết dân gian, Nhà Táo có 2 ông 1 bà hay 2 bà 1 ông hay 2 ông 2 bà?',
             'a)   3 ông 1 bà\nb)   2 ông 1 bà  \n'
             'c)   1 ông 1 bà  \nd)   1 ông 2 bà',
             'b'),

         3: ('Nước nào trên thế giới không có giao thừa: Việt Nam, Hàn Quốc hay Ấn Độ?',
             'a)  Nước nào cũng có giao thừa\nb)  Hàn Quốc\nc)  Ấn Độ\nd) Việt Nam ',
             'a'),

         4: ('Đố bạn chuột nào đi bằng 2 chân?',
             'a) Chuột Mickey \nb)  Chuột máy tính\nc)  Chuột trũi\n'
             'd)  Chuột đồng',
             'a'),

         5: ('Cà gì dễ bị ghét nhất',
             'a)  Cà khịa\nb)  Cà chớn\n'
             'c)  Đáp án a và b\nd)  Cà pháo',
             'c'),

         6: ('Người xông đất là người xông vô nhà mình, nhảy vô nhà mình hay là lẻn vô nhà mình sau thời khắc giao thừa?',
             'a)  Bước vô nhà mình đầu tiên\nb)  xông vô nhà mình\n'
             'c)  nhảy vô nhà mình\nd)  lẻn vô nhà mình',
             'a'),

         7: ('Tay nào làm nhiều chuyện không phải?',
             'a)  Tay trái\nb)  Tay súng 3\nc)  Tay cầm\nd)  Tay chân',
             'a'),

         8: ('Khi một trái cam đã lột vỏ và một trái cam chưa lột vỏ mà rơi xuống nước theo con trái nào chìm?',
             'a)  Trái táo\nb)  Trái cam đã lột vỏ\nc)  Trái cam chưa lột vỏ\nd)  Không biết',
             'b'),

         9: ('Người Việt Nam có tết Tây vậy người Tây có tết Ta hay không?',
             'a)  Có\nb)  Không có thông tin\nc)  Không\n'
             'd)  Không có câu trả lời',
             'c'),

         10: ('Ở đâu không có Tết: Vũng Tàu, Đắk Lắk hay Đà Lạt?',
              'a)  Ở đâu cũng có tết\nb)  Vũng Tàu, 1995\n'
              'c)  Đắk Lắk\nd)  Đà Lạt',
              'a'), }

    welcometext =\
        '\nHello {}, welcome to The Videogame Quiz'\
        '\nIn this quiz, you will be asked 10 questions about videogames.'\
        '\nTry your best to answer all 10 correctly. Enter a, b, c or d '\
        '\ndepending on which answer you think is right\n'

    users = {}
    score = 0
    highscore_file = 'highscore.log'

    @classmethod
    def get_username(cls):
        '''  method to ask user for user_name, if user name is Quit then leave.
             Dictionary of cls.users is checked on existing users. If user
             does not exist he/ she is added.
        '''
        user_name = ''
        quit = False
        while len(user_name) < 4 and not quit:
            user_name = input('Hello! What is your name [enter Q(uit) '
                              'to leave]?: ').strip().capitalize()
            if user_name in QUIT:
                quit = True

        if not quit:
            if user_name not in cls.users:
                cls.users.update({user_name: 0})
                cls.highscore = 0

            print(cls.welcometext.format(user_name))

        return user_name, quit

    @classmethod
    def play_loop(cls, user_name):
        '''  method to control loop of the quiz, update highscore, and ask
             to play again or not
        '''
        playagain = True
        while playagain:
            print(f'\n{user_name}, your current highscore is '
                  f'{cls.users[user_name]}.\n')

            if cls.escape_quiz():
                break

            score = cls.play_quiz()

            if score > cls.users[user_name]:
                cls.users.update({user_name: score})

            playagain = cls.play_again()

    @staticmethod
    def play_again():
        '''   ask player if he/ she wants to play quiz again
        '''
        answered = False
        while not answered:
            answer = input('Do you want to take the quiz again? Y or N: ')
            answered = True

            if answer in YES:
                playagain = True

            elif answer in NO:
                playagain = False

            else:
                answered = False

        return playagain

    @staticmethod
    def escape_quiz():
        '''  ask player twice if he/ she is ready to continue
        '''
        answered = 0
        question = '\nAre you ready to continue? Y or N? '
        while answered < 2:
            answer = input(question)
            print('---------------------------------------')
            answered += 1

            if answer in YES:
                escape_the_quiz = False
                break

            elif answer in NO:
                escape_the_quiz = True
                for i in range(3):
                    print('Oh... ok')
                    time.sleep(0.5)
                question = '\nNow are you ready to continue? Y or N '

            else:
                print('Yes or no only please!')

        return escape_the_quiz

    @classmethod
    def play_quiz(cls):
        '''  core of quiz asking multiple choice questions. Player can leave
             by entering quit
        '''
        questions = cls.questions.copy()
        question_choice = {i for i in range(1, len(questions)+1)}
        score = 0
        question_nr = 1

        while questions:
            question = random.sample(question_choice, 1)[0]
            answered = False

            print(f'Question: {question_nr} of {len(cls.questions)}')
            print(questions[question][0])
            print(questions[question][1])
            question_nr += 1

            answered = False
            while not answered:
                answer = input('What is your answer?: ').lower()

                if answer in (MULTIPLECHOICE + QUIT):
                    answered = True

                else:
                    print('ERROR, please input a, b, c or d only please!')

            if answer in QUIT:
                break

            elif answer == questions[question][2]:
                print('Good job! You are correct.\n')
                score += 1

            else:
                print('Unfortunately that is not correct! '
                      'Better luck next time.\n')

            questions.pop(question)
            question_choice.remove(question)

        print(f'Your score is >>> {score}\n')

        return score

    @classmethod
    def read_highscores(cls):
        '''  read highscores from cls.highscore_file
        '''
        try:
            with open(cls.highscore_file, 'r') as highscores:
                for line in highscores:
                    user_name, score = line.split(':')
                    cls.users[user_name.strip()] = int(score)

        except Exception as e:
            print('Error in log file, must be format <name: score>')

    @classmethod
    def write_highscores(cls):
        '''  write highscores to cls.highscore_file
        '''
        try:
            with open(cls.highscore_file, 'w') as highscores:
                for name in cls.users:
                    highscores.write('{}: {}\n'.
                                     format(name, str(cls.users[name])))

        except Exception as e:
            print('Error in log file, must be format <name: score>')

    @classmethod
    def clear_highscores(cls):
        '''  clears the highscore file if confirmed by typing 'CLEAR'
        '''
        answer = input('\nDo you want to clear the scores log, '
                       'type \'CLEAR\' ')

        if answer == 'CLEAR':
            with open(cls.highscore_file, 'w') as highscores:
                highscores.write('')

    @classmethod
    def display_highscores(cls):
        '''  displays highscores in order from high to low
        '''
        print('\nHighscores')
        print('-'*40)
        print('{:20}{}'.format('Name', 'Score'))
        print('-'*40)

        sorted_output = sorted(QuizGame.users.items(), key=lambda v: v[1],
                               reverse=True)
        for line in sorted_output:
            print(f'{line[0]:20}{line[1]}')


def main():
    '''  starts the program
    '''
    QuizGame.read_highscores()
    QuizGame.display_highscores()
    quit = False

    while not quit:
        user_name, quit = QuizGame.get_username()
        if not quit:
            QuizGame.play_loop(user_name)

    QuizGame.display_highscores()
    QuizGame.write_highscores()
    QuizGame.clear_highscores()


if __name__ == '__main__':
    main()