import random

def guess_the_number():
    """
    Main function to play Guess the Number.
    """
    number_to_guess = random.randint(1, 10)  # Random number between 1 and 10
    attempts = 3  # Number of attempts allowed
    
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 10.")
    
    while attempts > 0:
        try:
            guess = int(input(f"You have {attempts} attempts left. Enter your guess: "))
            if guess < 1 or guess > 10:
                print("Please guess a number between 1 and 10.")
                continue
            
            if guess == number_to_guess:
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly.")
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print("Incorrect guess. Try again.")
                else:
                    print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
if __name__ == "__main__":
    guess_the_number()
