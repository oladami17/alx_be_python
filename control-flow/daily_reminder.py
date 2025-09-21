# ask user for input
task = input("Enter your task: ")
priority = input("Priority(high/medium/low): ")
time_bound = input("Is it time-bound?(yes/no): ")

# match case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unspecified priority"
        # modify message if task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    if priority == "low":
        reminder = f"Note: {reminder}.Consider completing it when you have free time."
    else:
        reminder += " but it is not time-sensitive."
print("\nReminder:", reminder)
repeat = 0
while repeat < 1:
    print("Don't forget:", reminder)
    repeat += 1
