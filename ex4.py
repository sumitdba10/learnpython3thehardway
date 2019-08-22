cars = 100
space_in_each_car = 4.0
drivers = 30
passengers = 90
car_not_driven = cars - drivers
car_driven = drivers
carpool_capacity = car_driven * space_in_each_car
average_passanger_per_car = passengers/car_driven


print("There are",cars,"cars available to be driven.")
print("There are",drivers,"drivers available.")
print("There will be",car_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have",passengers,"passengers to carpool today.")
print("We need to put about",average_passanger_per_car,"people in each car.")
print("\n")

td_kannu=49768.67
cibc = 3897.29
td_Sumit= 5034.00
scotia= 3311.08
blue_rewards=1250.00
debt=200.00
deepika_total_savings=td_kannu+cibc+scotia
sumit_total_savings=td_Sumit+blue_rewards-debt
total_household_savings= deepika_total_savings+sumit_total_savings

print("There are two contributers in our financials:")
print("Sumit")
print("Deepika")
print("\n")
print("Savings till month of July 2019")
print("\n")
print("Deepika has savings of $",td_kannu,"in TD bank")
print("Deepika has savings of $",cibc,"in CIBC bank")
print("Deepika has savings of $",scotia,"in Scotia bank")
print("Total savings of Deepika is $",deepika_total_savings)
print("\n")
print("Sumit has total savings of $",td_Sumit,"in TD bank")
print("Sumit has total savings of $",blue_rewards," as Blue Rewards")
print("Sumit has debt of $",debt)
print("Total savings of Sumit is $",td_Sumit+blue_rewards-debt)
print("\n")
print("Total household saving is $",total_household_savings)
print("\n")
