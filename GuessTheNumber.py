import random

guessTaken = 0;

print("Hello! What is your name?")
playerName = input()

number = random.randint(1, 20)
print("Well, " + playerName + ", I make a number from 1 to 20.")

for guessTaken in range(6):
    print("Try to guess ")
    guess = int(input())
    if guess == number:
        guessTaken = str(guessTaken + 1)
        print("Very good, " + playerName + "! You did it for " + guessTaken + " trying!")
        break
    if guess > number:
        print("Your number too large!")
    if guess < number:
        print("Your number too small!")

# if guess == number:
#     guessTaken = str(guessTaken + 1)
#     print("Very good, " + playerName + "! You did it for " + guessTaken + " trying!")

if guess != number:
    number = str(number)
    print("Alas, I guessed the number " + number)
