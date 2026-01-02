import random
print('''welcome to roll a dice game
- if your score is greater than computer
- you will win
- other vise you will lose''')

number=int(input("enter a number from 1 to 6: "))
user_choice=number

if number>=1 and number<=6:
    print("your choice ",user_choice)
else:
    print("invalid input")
    exit()


def dice():
    b=[1,2,3,4,5,6]
    return (random.choice(b))

computer_choice=dice()
print("computer choice is",computer_choice)

if user_choice==computer_choice:
    print("it is a draw")
elif user_choice>=computer_choice:
    print("you won")
else:
    print("you lose")

