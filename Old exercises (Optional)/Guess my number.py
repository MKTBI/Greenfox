import random


min_range = int(input("Enter the minimum value for the range: "))
max_range = int(input("Enter the maximum value for the range: "))

# Generate a random number in the specified range
secret_num = random.randint(min_range, max_range)

lives = 5

# Keep asking for guesses until the player gets it right or runs out of lives
while lives > 0:
    
    guess = int(input("Enter your guess: "))
    
    
    if guess == secret_num:
        print("You guessed the correct number!")
        break
    else:
        print("Incorrect guess, try again")
        lives -= 1


if lives == 0:
    print("Game over, you ran out of lives")
    print("the number in my mind was: ",secret_num)
