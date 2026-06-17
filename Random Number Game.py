import random
level = input("Choose a level (Easy, Medium, Hard): ")
if level == "Easy":
    max = 10
elif level == "Medium":
    max = 100
else:
    max = 1000

x = random.randint(1, max)
running = True
attempts = 0

print("Guess the number between 1 and", max)
while running == True:
    user = int(input("Enter your guess: "))
    attempts = attempts + 1
    if user < x:
        print("Bigger then your guess", user)
    elif user > x:
        print("Smaller then your guess", user)
    else:
        print("Well Done!")
        print("It took you", attempts, "attempts")
        running = False
