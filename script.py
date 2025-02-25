class Vehicle:
 def __init__(self, brand, model, year, rental_price_per_day):
    self.brand = brand
    self.model = model
    self.year = year
    self.rental_price_per_day = rental_price_per_day

 def display_info(self):
   print(f"{self.brand}: {self.model}, Year: {self.year}, Rental Price: ${self.rental_price_per_day}/day")

 def calculate_rental_cost(self, days):
   cost = self.rental_price_per_day * days
   print(f"Rental cost for {self.brand} {self.model} for {days} days: ${cost}")

vehicle1 = Vehicle("Car", "Toyota Corolla", 2020, 50)
vehicle2 = Vehicle("Bike", "Yamaha R1", 2019, 30)
vehicle1.display_info()
vehicle2.display_info()
vehicle1.calculate_rental_cost(3)
vehicle2.calculate_rental_cost(5)