# Number Guessing Game 

A simple CLI-based number guessing game written in Python. The user has to guess a randomly generated number within limited attempts, based on the selected difficulty level.

# Features
- Difficulty levels: Easy, Medium, Hard
- Helpful hints after each guess
- Timer to track how long the user took
- High score tracking per difficulty level
- Option to replay multiple rounds

# How to Run the game
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/number-guessing-game.git
   cd number-guessing-game

# Run the script
python number_guessing_game.py

## Sample Output

Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Rules:
- You'll get a limited number of attempts based on difficulty
- I'll tell you if your guess is higher or lower than my number
- Try to guess the number in as few attempts as possible!

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
Enter your choice (1-3): 2

Great! You have selected the Medium difficulty level.

Let's start the game!

Attempts remaining: 5
Enter your guess (1-100): 22
Incorrect! The number is greater than 22.

Attempts remaining: 4
Enter your guess (1-100): 25
Incorrect! The number is greater than 25.

Attempts remaining: 3
Enter your guess (1-100): 30
Incorrect! The number is greater than 30.

Attempts remaining: 2
Enter your guess (1-100): 50
Incorrect! The number is greater than 50.
Hint: You're getting close!

Attempts remaining: 1
Enter your guess (1-100): 52

Game over! You've run out of attempts. The number was 59.

High Scores:
Easy: No score yet
Medium: No score yet
Hard: No score yet

Would you like to play again? (yes/no): no

Thanks for playing! Goodbye!

=== Code Execution Successful ===
