class Vehicle:
  def __init__(self, brand, model, year, rental_price_per_day):
    capacity = 0
    engine = ""
    days = 0
    self.brand = brand
    self.model = model
    self.year = year
    self.rental_price_per_day = rental_price_per_day
    self.capacity = capacity
    self.engine = engine
    self.days = days

  def display_info(self):
    if(self.capacity != 0):
      print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.capacity}, Rental Price: ${self.rental_price_per_day}/day")     
    elif(self.engine != ""):
      print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine}, Rental Price: ${self.rental_price_per_day}/day")
  
  def calculate_rental_cost(self, days):
    cost = self.rental_price_per_day * days
    print(f"Rental cost for {self.brand} {self.model} for {days} days: ${cost}")
class Car(Vehicle):
  def __init__(self, brand, model, year, rental_price_per_day, seats):
    super().__init__(brand, model, year, rental_price_per_day)
    self.capacity = seats

  def display_info(self):
        super().display_info()

class Bike(Vehicle):
  def __init__(self, brand, model, year, rental_price_per_day, engine):
    super().__init__(brand, model, year, rental_price_per_day)
    self.engine = engine

  def display_info(self):
        super().display_info()

def car_attributes():
  brand = input("Enter the brand: ")
  model = input("Enter the model: ")
  year = int(input("Enter the year: "))
  seats = int(input("Enter the number of seats: "))
  rental_price_per_day = float(input("Enter the rental price per day: "))
  car = Car(brand, model, year, rental_price_per_day, seats)
  car.days = int(input("Enter the number of rental days: "))
  vehicles_list.append(car)
  return car

def bike_attributes():
  brand = input("Enter the brand: ")
  model = input("Enter the model: ")
  year = int(input("Enter the year: "))
  capacity = input("Enter the engine capacity: ")
  rental_price_per_day = float(input("Enter the rental price per day: "))
  bike = Bike(brand, model, year, rental_price_per_day, capacity)
  bike.days = int(input("Enter the number of rental days: "))
  vehicles_list.append(bike)
  return bike

vehicles_list= []
option = 0

while option != 3:
  print("=" * 60)
  print("Select a vehicle: ")
  print("1 ==> Car")
  print("2 ==> Bike")
  print("3 ==> To exit the system")
  option = int(input("Choice: "))

  if option == 1:
    car = car_attributes()

  elif option == 2:
    bike = bike_attributes()

for vehicle in vehicles_list:
  vehicle.display_info()

for vehicle in vehicles_list:
  vehicle.calculate_rental_cost(vehicle.days)