# customar
# employee
# admin
from order import order
from abc import ABC
class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart =order()
    
    def view_to_manu(self,restaurent):
        restaurent.manu.show_manu()

    def add_to_cart(self,restaurent,item_name,quantity):
        item = restaurent.manu.find_item(item_name)
        print(item.quantity)
        if item:
            if quantity > item.quantity:
                print('Item quantity exceeded!!')
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print('your item is added')
        else:
            print('item is not found')
    def view_cart(self):
        print("***VIEW***")
        print("Name\t Price\t Quantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t {item.price}\t {quantity}")
        print(f"Total Price : {self.cart.total_price}")
        # jodi property use na kotam
        #print(f"Total Price : {self.cart.total_price()}")
    def pay_bill(self):
        print(f"TOtal {self.cart.total_price} paid successfully")
        self.cart.clear()
class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address)
        self.age=age
        self.designation=designation
        self.salary=salary
class admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)


    def add_employee(self,restaurant,employee):
        restaurant.add_employee(employee)


    def view_employee_list(self,restaurant):
        restaurant.view_employee_list()
    
    def add_new_item(self,restaurent,item):
        restaurent.manu.add_manu(item)
    def delete_item(self,restaurent,item):
        restaurent.manu.remove_item(item)

    def view_manu(self,restaurant):
        restaurant.manu.show_manu()



# mn =Manu()
# item =Fooditem("pizza",120,3)
# mamar_res = Restaurent("Mamar restaurent")
# item2 =Fooditem("burger",10,3)
# item3 =Fooditem("fish",120,3)
# ad = admin('rahim',12345,'rahim@gmail.com','khulna')
# ad.add_new_item(mamar_res,item)
# ad.add_new_item(mamar_res,item2)
# ad.add_new_item(mamar_res,item3)

# # mn.add_manu(item)
# # mn.add_manu(item2) # ai gulo admin add korte parbe only
# # mn.add_manu(item3)
# # mn.show_manu()
# # ad.view_employee_list()

# cousomer1=Customer("Rakib",12345678,"Rahim@gmail.com",'khulna.')
# cousomer1.view_to_manu(mamar_res)
# item_name = input("Enter your item Name : ")
# item_quantity = int(input('enter item quantity: '))
# cousomer1.add_to_cart(mamar_res,item_name,item_quantity)
# cousomer1.view_cart()
