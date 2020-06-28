import random

NUM_DIGITS = 3
MAX_GUESS = 10


def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return 'Congrats!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Hot!')
        elif guess[i] in secretNum:
            clues.append('Warmly!')

    if len(clues) == 0:
        return 'Cold!'

    clues.sort()
    return ' '.join(clues)

def isOnlyDigits(num):
    if num == '':
        return False
    for i in num:
        if i not in '1 2 3 4 5 6 7 8 9'.split():
            return False
    return True

print('I will guess the %s digit number that you might guess.' % (NUM_DIGITS))
print('I will give some tips ...')
print('When I say:            This means:')
print('           Cold                   No digits guessed.')
print('           Heat                   One digit is guessed, but its position is not guessed.')
print('           Hot                    One digit and its position guessed.')

while True:
    secretNum = getSecretNum()
    print('So I made a number. You have %s attempts to guess it.' % (NUM_DIGITS))
    guessTaken = 1
    while guessTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print('Attempt %s: ' % guessTaken)
            guess = input()
        print(getClues(guess,secretNum))
        guessTaken += 1
        if guess == secretNum:
            break
        if guessTaken > MAX_GUESS:
            print('No more attempts were left. I made a number %s.' % (secretNum))
    print('Want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break