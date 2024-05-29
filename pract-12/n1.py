class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating=0

    def change_rating(self,value):
        self.rating=value
    def describe_restaurant(self):
        print(f'{self.restaurant_name} - {self.cuisine_type}')
    def open_restaurant(self):
        print('Ресторан открыт!')

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    def list_flavors(self):
        print(self.flavors)

BaskinRobbins = IceCreamStand("Baskin Robbins", "icecream", ["strawberry", "orange","vanilla"])
BaskinRobbins.list_flavors()