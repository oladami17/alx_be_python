# put the size of the square

size = int(input("Enter the size of the pattern: "))
# initialize a row
row = 0
# use while loop to go trough rows
while row < size:
    for col in range(size):
        print("*", end="")
        print()
        row += 1