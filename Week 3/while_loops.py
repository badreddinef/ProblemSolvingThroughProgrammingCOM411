#Task 1
# Program to simulate a robot removing apples from box task 1
from unicodedata import numeric

print("How many apples you want to remove?")
apples_remove=int(input())

#Declare a control variable
apples_removed = 0

#remove apple
print()

#While loop
while apples_removed < apples_remove:
    print("removed apple")
    apples_removed = apples_removed + 1

# Task 2
#Program that allows the robot to avoid obstacles
print("How many obstacles should I avoid?")
obstacles_to_avoid=int(input())

#declare a control variable
obstacles = 0

#avoid obstacles
print()

#while loop
while obstacles< obstacles_to_avoid:
    print("Avoiding...done!",end="")
    print(f"{obstacles +1 } obstacles_to_avoided")
    obstacles = obstacles + 1

# final message
print("\nAll obstacles have benn avoided.")

