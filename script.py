class Car:
 def __init__(self, brand, model, year, rental_price_per_day):
    self.brand = brand
    self.model = model
    self.year = year
    self.rental_price_per_day = rental_price_per_day

 def display_info(self):
   print(self.brand, self.model, self.year, self.rental_price_per_day)

 def calculate_rental_cost(self, days):
   cost = self.rental_price_per_day * 24 * days
   print(cost)

car1 = Car("mercedes", "e320", 2003, 25)
car2 = Car("bmw", "x5", 2013, 50)
car1.display_info()
car2.display_info()
car2.calculate_rental_cost(5)