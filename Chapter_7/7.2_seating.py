#Ask the user how many people are in their dinner group
#>8 means telling them to wait for a table

group = input("How many people are in your dinner group? ")
group = int(group)

if (group > 8):
    print("Sorry you have to wait for a table")
else:
    print("Your table is ready!")
