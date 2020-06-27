import random
import time

def displayIntro():
    print('''\tВы находитесь в землях, заселенных драконами.
    Перед собой вы видите две пещеры. В одной из них — дружелюбный дракон,
    который готов поделиться с вами своими сокровищами. Во второй —
    жадный и голодный дракон, который мигом вас съест.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('В какую пещеру вы войдете? (нажмите клавишу 1 или 2)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Ее темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
    print()
    time.sleep(2)

    friendlyDragon = random.randint(1,2)

    if chosenCave == str(friendlyDragon):
        print('...делится с вами своими сокровищами!')
    else:
        print('...моментально вас съедает!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    # caveNumber = chooseCave()
    checkCave(chooseCave())
    print('Попытаете удачу еще раз? (yes или no)')
    playAgain = input()