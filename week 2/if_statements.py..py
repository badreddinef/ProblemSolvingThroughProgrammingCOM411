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
    print("\nPerforming calculation...")
elif activity!="calculate":
    print("\nPerforming activity...")
print("\nActivity compled!")
#IF...ELSE Statement 2
print("Towards which direction should i go (up, down, left or right) ")
direction=input()
if direction=="up":
    print("\nI am moving upward direction!")
else:
    if direction=="down":
        print("\nI am moving downward direction!")
    else:
        if direction=="left":
            print("\nI am moving left direction!")
        elif direction=="right":
            print("\nI am moving right direction!")
#Using Operators
print("\nPlease enter a whole number")
number=input()
if number=="%2":
    print(f"\nThe number {number} is even!")
elif number!="%2":
    print(f"\nThe number {number} is odd!")
