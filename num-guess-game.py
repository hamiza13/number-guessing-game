import random
num=random.randint(1,50)
num1=0
name=input("Enter Your Name:")
print("Hello",name,"Welcome To The Number Guessing Game!")
while num1!=num:
    num1=int(input("Guess a Number Between 1 to 50:"))
    if num1>num:
        print("Your Guess Is Too High!, Try Again:\n")
    elif num1<num:
        print("Your Guess Is Too Low!, Try Again:\n")
    else:
        print("Congratulations, You Guessed The Correct Number!\n")