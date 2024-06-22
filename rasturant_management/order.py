class order:
    def __init__(self) -> None:
        self.items = {}

    def add_item(self,item):
        if item in self.items:
            #jodi item ta cart a already takye
            self.items[item] += item.quantity
        else:
            #cart e item jodi na takye
            self.items[item] = item.quantity 
    
    def remove(self,item):
        if item in self.items:
            del self.items[item]
    #property jodi dai taila aita akta variable ar moto kaj korbe 
    #se khatre ake next time variable diye call korle hobe function ar jaygay
    @property 
    def total_price(self):
        return sum(item.price * quantity for item,quantity in self.items.items())
    
    def clear(self):
        self.items ={}