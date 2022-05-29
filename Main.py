import random
length = int(input("Enter lhe length of the game(points):"))
print(f"Rock Paper scissor of {length} points")

user = 0
computer = 0
while(True):
    if user == length or computer == length:
        if user == length:
            print("You won !!!")
            break
        elif computer == length:
            print("Sorry, You Lost !!!")
            break
    else:
        uc = input("Enter Your Choice (Rock, Paper, Scissor):")
        Computer = ["Rock", "Paper", "Scissor","Rock", "Paper", "Scissor","Rock", "Paper", "Scissor"]
        cc = random.choice(Computer)
        print(f"Computer selected:{cc} and you selected:{uc}")
        if uc == "Rock" and cc == "Paper":
            print("Computer's Point")
            computer = computer+1
            print(f"Computer:{computer} and User:{user}")

        elif uc == "Paper" and cc == "Scissor":
            print("Computer's Point")
            computer = computer+1
            print(f"Computer:{computer} and User:{user}")

        elif uc == "Scissor" and cc == "Rock":
            print("Computer's Point")
            computer = computer+1
            print(f"Computer:{computer} and User:{user}")

        elif uc == "Paper" and cc == "Rock":
            print("Your Point")
            user = user + 1
            print(f"Computer:{computer} and User:{user}")

        elif uc == "Scissor" and cc == "Paper":
            print("Your Point")
            user = user + 1
            print(f"Computer:{computer} and User:{user}")

        elif uc == "Rock" and cc == "Scissor":
            print("Your Point")
            user = user + 1
            print(f"Computer:{computer} and User:{user}")

        elif uc == cc:
            print("Tie")
