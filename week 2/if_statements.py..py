#IF statement
print("What type of book is this?")
book=input()
if book=="adventure":
    print("\nI like adventure books!")
print("\n Finished reading book.")
#IF...ELSE Statement
print("Please enter the activity to be performed.")
activity=input()
if activity=="calculate":
    print("Performing calculation...")
elif activity!="calculate":
    print("Performing activity...")
print("Activity compled!")
#task 3
print("Towards which direction should i go (up, down, left or right) ")
direction=input()
if direction=="up":
    print("I am moving upward direction!")
else:
    if direction=="down":
        print("I am moving downward direction!")
    else:
        if direction=="left":
            print("I am moving left direction!")
        elif direction=="right":
            print("I am moving right direction!")

