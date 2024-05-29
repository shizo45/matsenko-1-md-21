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
    def __init__(self, restaurant_name, cuisine_type, flavors, location, time):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.time = time

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def remove_flavor(self, flavor):
        self.flavors.remove(flavor)

    def contains_flavor(self, flavor):
        return flavor in self.flavors

    def list_flavors(self):
        print(self.flavors)

BaskinRobbins = IceCreamStand("Baskin Robbins", "icecream", ["strawberry", "orange","vanilla"], "Nevsky 30", "10:00-21:00")