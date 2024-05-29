class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f'{self.restaurant_name} - {self.cuisine_type}')
    def open_restaurant(self):
        print('Ресторан открыт!')
firstRestaurant = Restaurant('Macsrak', 'american')
secondRestaurant = Restaurant('JKkdk', 'japan')
lastRestaurant = Restaurant('Kroshka-kartoshka', 'russian')
firstRestaurant.describe_restaurant()
secondRestaurant.describe_restaurant()
lastRestaurant.describe_restaurant()