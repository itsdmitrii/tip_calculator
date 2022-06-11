print("Welcome to the tip calculator!\n")

total_bill = input("What was the total bill? $\n")

tip_percentage = input("What petcentage tip would you like to give? 10, 12, or 15?\n")

total_people_split = input ("How many people to split the bill? \n")

total_bill_as_float = float(total_bill)
tip_percentage_as_int = int(tip_percentage)
total_people_split_int = int(total_people_split)

# Calculations:
percentage_with_tip = 100 + tip_percentage_as_int

total_with_tip = total_bill_as_float * percentage_with_tip / 100

each_person_pay = total_with_tip / total_people_split_int

final_amaount = "{:.2f}".format(each_person_pay)


print(f"Each person shoud pay: ${final_amaount} ")