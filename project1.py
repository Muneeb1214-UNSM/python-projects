#inputs need from the user
#rent form the user
#food from the user
#electricity bill
#charge per unit
#number of persons

#OUTPUT
#total amount

rent = int(input("enter the rent of your hostel = "))
food = int(input("enter the total amount of food = "))
electricity_bill = int(input("enter the total amount of electricity bill =  "))
charge_per_unit = int(input("enter charge per unit =  "))
persons = int(input("number of persons =  "))

total = electricity_bill * charge_per_unit

output = (rent + food + total) // persons
print("total amount of the hostel rent is =  ", output)