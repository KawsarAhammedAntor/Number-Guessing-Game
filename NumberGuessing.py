import random

secret_number= random.randint(1, 101)
attempts = 0
guessed_correctly= False
print("Wellcome to the Guess The Number Game")
print("Thinking a number, you have to guess")

while not guessed_correctly:
    try:
        guess = int(input("Enger your guessed number"))
        attempts+=1
        
        if guess< secret_number:
            print("Too Low")
        elif guess> secret_number:
            print("Too Hight")
        else:
            guessed_correctly= True
            print(f"Congratulations! You have guessed the number correctly")
    except ValueError:
        print("Please enter a valid integer number")
        
