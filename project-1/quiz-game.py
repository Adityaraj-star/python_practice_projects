print("Welcome to my computer quiz!")

want_to_play = input("Do you want to play the game? ")

if want_to_play.lower() != 'yes':
    quit()

print("Let Play!")

score = 0

answer = input("What does CPU stands for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does GPU stands for? ")

if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does RAM stands for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does PSU stands for? ")

if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} questions correct.")
print(f"Your score {(score / 4) * 100} %.")