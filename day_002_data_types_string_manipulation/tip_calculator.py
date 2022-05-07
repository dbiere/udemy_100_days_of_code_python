print("Welcome to the tip calculator!")
bill_amount = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
people_count = int(input("How many people to split the bill? "))

final_bill = bill_amount + (tip_percent/100) * bill_amount
amount_per_person = final_bill / people_count

print (f"Each person should pay: ${round(amount_per_person, 2)}")
