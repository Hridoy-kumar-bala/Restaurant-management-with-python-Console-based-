
def Admin_manu():
    name = input("Enter Your Name: ")
    email = input("Enter the email: ")
    phone = input("Enter your phone:")
    address = input("Enter your address:")
    Admin =Admin(name=name,email=email,phone=phone,address=address)
    while True:
        print("WELLCOME TO {Admin.name}!!")
        print("1. ADD NEW ITEM")
        print("2. Add NEW EMPLOYEE")
        print("3. VIEW EMPLOYEE")
        print("4. VIEW ITEM")
        print("5. DELETE ITEM")
        print("6. EXIT")


        choice = int(input("Enter your option: "))
        
        if choice ==1:
            item_name = input("Enter your item Name : ")
            item_price = int(input('enter item PRICE: '))
            item_quantity = int(input('enter item quantity: '))
            item = Fooditem(item_name,item_price,item_quantity)
            Admin.add_new_item(mamar_restaurant,item)
        elif choice==2:
            name = input("Enter employee Name: ")
            phone = input("Enter employee phone:")
            email = input("Enter employee email: ")
            address = input("Enter employee address:")
            designation = input("Enter employee designation: ")
            age = input("Enter employee age:")
            salary  = input("Enter employee salary:")
            Admin.add_employee(name, phone, email, address,age,designation,salary)

        elif choice ==3:
            Admin.view_employee(mamar_restaurant)
        elif choice==4:
            Admin.view_manu(mamar_restaurant)
        elif choice == 5:
            item_name = input("Enter your item Name : ")
            Admin.remove_item(mamar_restaurant,item_name)
        elif choice==6:
            break
        else:
            print("your number is invalid. Please try again.\n Good luck")

