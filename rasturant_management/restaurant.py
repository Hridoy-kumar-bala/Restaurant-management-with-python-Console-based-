from manu import Manu
class Restaurent:
    def __init__(self,name) -> None:
        self.name=name
        self.employees =[] #now it is your database
        self.manu= Manu()
    def add_employee(self,employee):
        self.employees.append(employee)
        # print(f'{employee.name} is added.') 
        # # sudu name o use korte partam karon Employee(self,name,phone,address,age,designation,sakary) diye e akta emplpyee object toiri korchi
        # # print(f'{name} is added.') 

    def view_employee_list(self):
        print(f'Employee list!!')
        for emp in self.employees:
            print(emp.name,emp.email,emp.phone,emp.address)
