print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?\n $"))
people = int(input("How many people to split the bill?\n"))
tip = float(input("What percentage of tip would you like to give?\n"))

bill_with_tip = total_bill + total_bill*tip/100
bill_per_person = "{:.2f}".format(bill_with_tip/people)
print(f"Each person should pay ${bill_per_person}")
