# multiplication_table.py
# input number

number = int(input("Enter a number to see its multiplication table: "))
# use for loop to print the multiplication table
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")
