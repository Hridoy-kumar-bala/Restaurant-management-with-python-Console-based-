from Fooditem import Fooditem
from manu import Manu
from order import order
from restaurant import Restaurent
from user_panel import Customer,admin,Employee

            employee =Employee(name, email, phone, address,age, designation, salary)
= Restaurent("Mamar Restaurant")
def coustomar_manu():
    name = input("Enter Your Name: ")
    email = input("Enter the email: ")
    phone = input("Enter your phone:")
    address = input("Enter your address:")
    coustomer =Customer(name=name,email=email,phone=phone,address=address)
    while True:
        print(f"WELLCOME TO {coustomer.name}!!")
        print("1. View Manu")
        print("2. Add item to Card")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. EXIT")

        choice = int(input("Enter your option: "))
        
        if choice ==1:
            coustomer.view_to_manu(mamar_restaurant)
        elif choice==2:
            item_name = input("Enter your item Name : ")
            item_quantity = int(input('enter item quantity: '))
            coustomer.add_to_cart(mamar_restaurant,item_name,item_quantity)

        elif choice ==3:
            coustomer.view_cart()
        elif choice==4:
            coustomer.pay_bill()
        elif choice==5:
            break
        else:
            print("your number is invalid. Please try again.\n Good luck")


    
def Admin_manu():
    name = input("Enter Your Name: ")
    email = input("Enter the email: ")
    phone = input("Enter your phone:")
    address = input("Enter your address:")
    Admin = admin(name=name,email=email,phone=phone,address=address)
    while True:
        print(f"WELLCOME TO {Admin.name}!!")
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
            employee =Employee(name, email, phone, address,age, designation, salary)
            Admin.add_employee(mamar_restaurant,employee)
        elif choice ==3:
            Admin.view_employee(mamar_restaurant)
        elif choice==4:
            Admin.view_manu(mamar_restaurant)
        elif choice == 5:
            item_name = input("Enter your item Name : ")
            Admin.delete_item(mamar_restaurant,item_name)
        elif choice==6:
            break
        else:
            print("your number is invalid. Please try again.\n Good luck")

while True:
    print("WELLCOME !!")
    print("1. customer")
    print("2. ADMIN")
    print("3. EXIT")
    choice = int(input("ENTER YOUR NUMBER: "))
    if choice==1:
        coustomar_manu()
    elif choice==2:
        Admin_manu()
    elif choice ==3:
        break
    else:
        print(f"your number is invalid")
