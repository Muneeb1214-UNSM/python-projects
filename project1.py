#inputs need from the user
#rent from the user
#food from the user
#electricity bill from the user
#charge per unit
#number of persons

#OUTPUTS
#total amount

rent = int(input("enter the total rent of the hostel =  "))
food = int(input("total amount of food =  "))
electricity_bill = int(input("enter the electricity bill =  "))
charge_per_unit = int(input("enter the charge per unit =  "))
persons = int(input("number of persons =  "))

total = electricity_bill * charge_per_unit

output = (rent + food + total) // persons
print("total amount of the hostel rent are =  ",output)