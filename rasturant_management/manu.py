class Manu:
    def __init__(self) -> None:
        self.items=[] #item ar database
    def add_manu(self,item):
        self.items.append(item)
    def find_item(self,item_name):
        for item in self.items:
            if item.name.lower() == item_name:
                return item
        return None
    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print('Item deleted')
        else:
            print('Item is not found')
    def show_manu(self):
        print("****MANU****")
        print("Name\t price\t Quentity")
        for item in self.items:
            print(f'{item.name}\t {item.price}\t {item.quantity}')