#CONTACT BOOK APP USING PYTHON.
contacts = {}

while True:
    print("\n contact book app ")
    print("1 : Create contact")
    print("2 : view contact")
    print("3 : update contact")
    print("4 : delete contact")
    print("5 : search contact")
    print("6 : count contact")
    print("7 : Exit")

    choice = input("choose your choice : ")

    if choice == '1':
        name = input("enter your name ")
        if name in contacts:
            print(f"contact name {name} already exists.")
        else:
            age = int(input("enter age = "))
            email = input("enter your email = ")
            mobile = input("enter your mobile number =  ")
            contacts[name] = {'age':int(age),'email':email,'mobile':mobile}
            print(f"contact name {name} has already created successfully!")

    elif choice == '2':
        name = input("enter contact name to view =  ")
        if name in contacts:
            contact = contacts[name]
            print(f'Name:{name}, Age:{age}, Mobile Number:{mobile}')
        else:
            print("contact not found ")

    elif choice == '3':
        name = input("enter the name of updated contact  = ")
        if name in contacts:
            age = int(input("enter updated age = "))
            email = input("enter updated email = ")
            mobile = input("enter updated mobile number = ")
            contacts[name] = {'age':int(age),'email':email, 'mobile':mobile}
        else:
            print("contact not found.")

    elif choice == '4':
        name = input("enter contact name to delete : ")
        if name in contacts:
            del contacts[name]
            print(f'contact name {name} has been deleted successfully!')
        else:
            print("contact not found.")

    elif choice == '5':
        search_name = input("enter contact name to search = ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found - name {name}, age:{age},mobile number:{mobile},Email:{email}')
                found = True
        if not found:
            print("not contact found with that name ")

    
    elif choice == '6':
        print(f'totol contacts in your book : {len(contacts)}')

    elif choice == '7':
        print("closing the.....program")
        break

    else:
        print("invalid input .")