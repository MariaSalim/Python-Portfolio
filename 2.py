print("Welcome to the tip calculator!")
bill = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
bill = float(bill)
tip = int(tip) / 100
people = int(people)
total_bill = float(bill + (bill * tip))
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")