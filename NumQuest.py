import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = None

    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input! Please enter an integer.")

    print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")

# Run the game
number_guessing_game()
