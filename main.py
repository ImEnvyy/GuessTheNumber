import random

game_mode = input("Welcome to this little guessing Simulation.\n"
                  "Type 'me' -> mode you guess the number chosen by the computer\n"
                  "Type 'pc' -> mode where the computer guesses your number.\n")
try:
    max_bound = int(input("Please type in a number to set a max Value for the guessing game:"))
except:
    print("Not a number format. Running on default Value 10.")
    max_bound = 10


print(max_bound)


def guess(x):
    random_number = random.randint(0, x)
    my_guess = -1
    min_value = 0
    max_value = x

    while my_guess != random_number:
        my_guess = int(
            input(f"Guess a number between {min_value} and {max_value} (including {min_value} and {max_value}): "))
        if my_guess < random_number:
            min_value = my_guess + 1
            print("Sorry, guess again. Too low.")
        elif my_guess > random_number:
            max_value = my_guess - 1
            print("Sorry, guess again. Too high.")

    print(f"Nice Done! You guessed the number {random_number} correctly!!")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    counter = 0

    while feedback != 'c':
        counter += 1
        if low != high:
            pc_guess = random.randint(low, high)
            feedback = input(f"Is {pc_guess} too high (H), too low (L) or correct (C)??").lower()
            if feedback == 'h':
                high = pc_guess - 1
            elif feedback == 'l':
                low = pc_guess + 1
            elif feedback != 'l' and feedback != 'h' and feedback != 'c':
                while feedback != 'l' or feedback != 'h' or feedback != 'c':
                    feedback = input(f"Sorry, {feedback} can't be processed. "
                                     "Please type 'H' if too high, 'L' if too low or 'c' if guess matches your number!")
        else:
            pc_guess = low
            feedback = 'c'

    if counter == 1:
        print(f"Ohh okay wow..I became very lucky guessing the number {pc_guess} correctly first try.")
    else:
        print(f"Well after trying {counter} times I finally guessed your number ({pc_guess}) correct.")


if game_mode == "pc":
    computer_guess(max_bound)
elif game_mode == "me":
    guess(max_bound)
