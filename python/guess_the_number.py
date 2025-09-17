import random
import os

def clrsc():
    if os.name == 'nt':  
        _ = os.system('cls')
    else:  
        _ = os.system('clear')

random_int = random.randint(0, 1000)

rounds = 1

while rounds <= 10:

    print("Guess the number")
    a = int(input("Enter your number : "))

    if random_int==a:
        print("You won")
        break;
    elif random_int < a:
        print("Go Low\n")
        input("Press any key")
        clrsc()
    elif random_int > a:
        print("Go High\n")
        input("Press any key")
        clrsc()
    else:
        print("Error")

    rounds += 1

print(f"You took {rounds} rounds.")