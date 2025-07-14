# Program to check if a number is even or odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is an even number.")
elif(number % 2 !=0):
    print(f"{number} is an odd number.")
else:
    print("Invalid input")