import random
secret_number = random.randint(1,15)
guess = int(input("Enter your number: "))
try_again = True
match guess:
    case _ if guess == secret_number:
        print("Congratulations, you guessed it!")
    case _ if guess > secret_number:
        print("Oops, your guess is a bit high. Try again! ",try_again )
        if (try_again):
            guess = int(input("Enter your new number: "))
        else:
            print("Goodbye")
    case guess > secret_number:
        print("Nope, your guess is a bit low. Give it another shot!", try_again)
        if (try_again):
            guess = int(input("Enter your new number: "))
        else:
            print("Goodbye")
    case _:
        print('invalid value!')