print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_percent = 1 + tip / 100
payment_per_person = (bill / people) * tip_percent
print (f"Each person should pay: ${payment_per_person:.2f}")

