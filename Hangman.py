import random

HANGMAN_PICS = ['''
 +---+
     |
     |
     |
  ====''', '''
 +---+
 0   |
     |
     |
  ====''', '''
 +---+
 0   |
 |   |
     |
  ====''', '''
 +---+
 0   |
/|   |
     |
  ====''', '''
 +---+
 0   |
/|\  |
     |
  ====''', '''
 +---+
 0   |
/|\  |
/    |
  ====''', '''
 +---+
 0   | 
/|\  |
/ \  |
  ====''']

words = 'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея ' \
        'индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон ' \
        'попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'.split()


def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blank = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blank = blank[:i] + secretWord[i] + blank[i + 1:]

    for letter in blank:
        print(letter, end='')
    print()


def getGuess(alreadyGuessed):
    while True:
        print('Введите букву ')
        guess = input().lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву')
        elif guess in alreadyGuessed:
            print('Эта бувка уже использована')
        elif guess not in 'абвгдежзийклмнопрстуфхцчщшъыьэюя':
            print('Введите букву из русского алфавита!')
        else:
            return guess


def playAgain():
    print('Хотите сыграть еще раз? (да или нет)')
    return input().lower().startswith('д')


print('В И С Е Л И Ц А')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameOver = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters += guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Молодец! Секретное слово: ' + secretWord + '!')
            gameOver = True
    else:
        missedLetters += guess
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Сектретное слово: ' + secretWord)
            gameOver = True

    if gameOver:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameOver = False
            secretWord = getRandomWord(words)
        else:
            break
