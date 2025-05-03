import random

while True:
    number = random.randint(1, 100)
    print("Guess a number between 1 and 100")
    guess = int(input())

    if guess == number:
        print("You win!")
    else:
        print(f"Wrong! The number was {number}")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != 'y':
        break
