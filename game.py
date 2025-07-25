import random
import time
from datetime import timedelta

class NumberGuessingGame:
    def __init__(self):
        self.high_scores = {
            'easy': float('inf'),
            'medium': float('inf'),
            'hard': float('inf')
        }
    
    def display_welcome(self):
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        print("\nRules:")
        print("- You'll get a limited number of attempts based on difficulty")
        print("- I'll tell you if your guess is higher or lower than my number")
        print("- Try to guess the number in as few attempts as possible!")
    
    def get_difficulty(self):
        print("\nPlease select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        
        while True:
            choice = input("Enter your choice (1-3): ")
            if choice in ['1', '2', '3']:
                difficulties = {
                    '1': ('easy', 10),
                    '2': ('medium', 5),
                    '3': ('hard', 3)
                }
                name, attempts = difficulties[choice]
                print(f"\nGreat! You have selected the {name.capitalize()} difficulty level.")
                return name, attempts
            print("Invalid input. Please enter 1, 2, or 3.")
    
    def get_hint(self, number, guess):
        difference = abs(number - guess)
        if difference > 30:
            return "You're very far from the number!"
        elif difference > 15:
            return "You're getting warmer but still quite far."
        elif difference > 5:
            return "You're getting close!"
        else:
            return "You're very close now!"
    
    def play_round(self):
        self.display_welcome()
        difficulty, max_attempts = self.get_difficulty()
        number = random.randint(1, 100)
        attempts = 0
        start_time = time.time()
        
        print("\nLet's start the game!")
        
        while attempts < max_attempts:
            remaining = max_attempts - attempts
            print(f"\nAttempts remaining: {remaining}")
            
            try:
                guess = int(input("Enter your guess (1-100): "))
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            attempts += 1
            
            if guess == number:
                end_time = time.time()
                time_taken = timedelta(seconds=int(end_time - start_time))
                print(f"\nCongratulations! You guessed the correct number in {attempts} attempts.")
                print(f"Time taken: {time_taken}")
                
                if attempts < self.high_scores[difficulty]:
                    self.high_scores[difficulty] = attempts
                    print("🎉 New high score for this difficulty level! 🎉")
                return True
            
            if attempts < max_attempts:
                if guess < number:
                    print(f"Incorrect! The number is greater than {guess}.")
                else:
                    print(f"Incorrect! The number is less than {guess}.")
                
                if attempts % 2 == 0 and remaining <= 3:
                    print(f"💡 Hint: {self.get_hint(number, guess)}")
        
        print(f"\nGame over! You've run out of attempts. The number was {number}.")
        return False
    
    def show_high_scores(self):
        print("\nHigh Scores:")
        for difficulty, score in self.high_scores.items():
            if score != float('inf'):
                print(f"{difficulty.capitalize()}: {score} attempts")
            else:
                print(f"{difficulty.capitalize()}: No score yet")
    
    def run(self):
        while True:
            self.play_round()
            self.show_high_scores()
            
            play_again = input("\nWould you like to play again? (yes/no): ").lower()
            if play_again not in ['yes', 'y']:
                print("\nThanks for playing! Goodbye!")
                break

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.run()
