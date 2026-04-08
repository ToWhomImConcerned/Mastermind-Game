import time
import random

def display_intro(code_length, max_attempts, time_limit):
    print("Welcome, are YOU a mastermind?")
    print(f"Try to guess my secret {code_length} digit code!")
    print(f"You have {max_attempts} attempts and {time_limit} seconds to crack it!")

def set_difficulty(difficulty):
    if difficulty == "easy":
        code_length = 3
        max_attempts = 20
        time_limit = 240
    elif difficulty == "medium":
        code_length = 4
        max_attempts = 16
        time_limit = 180
    elif difficulty == "hard":
        code_length = 5
        max_attempts = 12
        time_limit = 120
    else:
        print("Invalid choice, defaulting to easy.")
        code_length = 3
        max_attempts = 20
        time_limit = 240

    return code_length, max_attempts, time_limit

game_running = True

while game_running:

    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

    code_length, max_attempts, time_limit = set_difficulty(difficulty)

    code = [random.randint(0, 9) for _ in range(code_length)]

    display_intro(code_length, max_attempts, time_limit)

    print(code)

    timed_out = False
    first_guess = True
    correct_position = 0
    attempts = 0

    while correct_position != code_length and attempts < max_attempts:

        guess = input("Enter code: ")

        if guess == "quit":
            print("WE DON'T LIKE QUITTERS!")
            game_running = False
            break

        if guess == "iwannawin":
            print(f"{code} is the answer ya dirty cheater! Enjoy the loss! 💀  ")
            game_running = False
            break

        if first_guess:
            start_time = time.time()
            first_guess = False

        if len(guess) != code_length or not guess.isdigit(): #validates input length and type
            print("Invalid code, try again.")
            continue

        elapsed = time.time() - start_time

        if elapsed >= time_limit:
            timed_out = True
            break

        guess_list = [int(digit) for digit in guess] #converts guess to a list

        correct_position = 0

        for i in range(code_length):
            if guess_list[i] == code[i]:
                correct_position += 1

        code_copy = code[:]
        #removes already correctly placed digits from code_copy
        for i in range(code_length):
            if guess_list[i] == code[i]:
                code_copy.remove(int(guess_list[i]))

        correct_digit = 0
        #checks remaining digits against what's left in code_copy
        for i in range(code_length):
            if guess_list[i] in code_copy and guess_list[i] != code[i]:
                correct_digit += 1
                code_copy.remove(guess_list[i]) #matches removed as to not be counted twice

        if correct_position != code_length:
            print("Correct positions:", correct_position)
            print("Correct digit, wrong position:", correct_digit)
            attempts += 1
            print(f"You have {max_attempts - attempts} attempts remaining!")

    if timed_out:
        print("Time's up!")

    elif attempts >= max_attempts:
        print("You ran out of tries, game over!")

    elif correct_position == code_length:
        print("YOU CRACKED THE CODE! 🎉")

    play_again = input("Play again? (yes/no): ")

    if play_again == "no":
        print("Thanks for playing!")
        break

    if play_again != "yes" and play_again != "no":
        print("I'll take that as a no, thanks for playing!")
        break