class Vehicle:
  def __init__(self, brand, model, year, rental_price_per_day):
    capacity = 0
    engine = ""
    days = 0
    self.brand = brand
    self.model = model
    self.year = year
    self.__rental_price_per_day = rental_price_per_day
    self.capacity = capacity
    self.engine = engine
    self.days = days

  def get_rental_price_per_day(self):
    return self.__rental_price_per_day

  def set_rental_price_per_day(self, new_price):
    self.__rental_price_per_day = new_price
    return self.__rental_price_per_day

  def display_info(self):
    if(self.capacity != 0):
      print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.capacity}, Rental Price: ${self.get_rental_price_per_day()}/day")     
    elif(self.engine != ""):
      print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine}, Rental Price: ${self.get_rental_price_per_day()}/day")
  
  def calculate_rental_cost(self, days):
    cost = self.get_rental_price_per_day() * days
    print(f"Rental cost for {self.brand} {self.model} for {days} days: ${cost}")

  def modify_rental_cost(self, new_price):
    modified_price = self.set_rental_price_per_day(new_price)
    print(f"Updated rental cost for {self.brand} {self.model}: ${modified_price}/day")
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

def show_vehicle_info(vehicle):
  vehicle.display_info()

def car_attributes():
  brand = input("Enter the brand: ")
  model = input("Enter the model: ")
  
  year = int(input("Enter the year (4-digit): "))
  while year < 1000 or year > 9999:
    print("Year must be a 4-digit positive number. Please try again.")
    year = int(input("Enter the year (4-digit): "))

  seats = -1
  while seats <= 0:
    seats = int(input("Enter the number of seats (Positive number): "))
    if seats < 0:
      print("Seats must be a positive number. Please try again.")

  rental_price_per_day = -1
  while rental_price_per_day <= 0:
    rental_price_per_day = float(input("Enter the rental price per day (Positive price): "))
    if rental_price_per_day < 0:
      print("Price must be a positive number. Please try again.")

  car = Car(brand, model, year, rental_price_per_day, seats)

  car.days = -1
  while car.days <= 0:
    car.days = int(input("Enter the number of days (Positive number): "))
    if car.days < 0:
      print("Number of days must be a positive number. Please try again.")

  vehicles_list.append(car)
  return car

def bike_attributes():
  brand = input("Enter the brand: ")
  model = input("Enter the model: ")

  year = int(input("Enter the year (4-digit): "))
  while year < 1000 or year > 9999:
    print("Year must be a 4-digit positive number. Please try again.")
    year = int(input("Enter the year (4-digit): "))

  capacity = input("Enter the engine capacity: ")
  
  rental_price_per_day = -1
  while rental_price_per_day <= 0:
    rental_price_per_day = float(input("Enter the rental price per day (Positive price): "))
    if rental_price_per_day < 0:
      print("Price must be a positive number. Please try again.")
  
  bike = Bike(brand, model, year, rental_price_per_day, capacity)
  
  bike.days = -1
  while bike.days <= 0:
    bike.days = int(input("Enter the number of days (Positive number): "))
    if bike.days < 0:
      print("Number of days must be a positive number. Please try again.")

  vehicles_list.append(bike)
  return bike

car_instance = Car("Toyota", "Corolla", 2020, 50.0, 5)
car_instance.days = 3

bike_instance = Bike("Yamaha", "R1", 2019, 30.0, "998cc")
bike_instance.days = 5

vehicles_list= []

option = 0

while option != 4:
  print("=" * 60)
  print("Select a vehicle: ")
  print("1 ==> Car")
  print("2 ==> Bike")
  print("3 ==> To list existing data")
  print("4 ==> To exit the system")
  option = int(input("Choice: "))

  if option == 1:
    car = car_attributes()
    answer = input(f"Do you want to modify you rental price[{car.get_rental_price_per_day()}]? (yes/no): ").lower()
    if answer == "yes":
      price = float(input("Enter the new rental price: "))
      car.modify_rental_cost(price)

  elif option == 2:
    bike = bike_attributes()
    answer = input(f"Do you want to modify you rental price[{bike.get_rental_price_per_day()}]? (yes/no): ").lower()
    if answer == "yes":
      price = float(input("Enter the new rental price: "))
      bike.modify_rental_cost(price)

  elif option == 3:
    for vehicle in vehicles_list:
      show_vehicle_info(vehicle)

    for vehicle in vehicles_list:
      vehicle.calculate_rental_cost(vehicle.days)

car_instance.display_info()
bike_instance.display_info()
print("")

car_instance.calculate_rental_cost(car_instance.days)
bike_instance.calculate_rental_cost(bike_instance.days)
print("")

car_instance.modify_rental_cost(55.0)
print("=" * 80)

for vehicle in vehicles_list:
  show_vehicle_info(vehicle)
  vehicle.calculate_rental_cost(vehicle.days)