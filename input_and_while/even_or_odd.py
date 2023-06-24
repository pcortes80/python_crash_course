# How to use the Module Operator (%)
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
reminder = number % 2

if number % 2 == 0:
    print(f"\nThe reminder is {reminder}, so the number {number} is even.")
else:
    print(f"\nThe reminder is {reminder}, so the number {number} is odd.")
