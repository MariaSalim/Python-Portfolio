height = int(input("Enter your height in cm: "))
bill = 0
if height >= 120:
    age = input("Enter your age: ")
    age = int(age)
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Your ticket is free!")
    else:
        bill = 12
    print(f"Your ticket is ${bill}")
    if input("Do you want a photo taken? Y or N: ") == 'Y':
        bill += 3
        print(f"Your final bill is: ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
