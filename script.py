class Vehicle:
  def __init__(self, brand, model, year, rental_price_per_day):
    capacity = 0
    engine = ""
    self.brand = brand
    self.model = model
    self.year = year
    self.rental_price_per_day = rental_price_per_day
    self.capacity = capacity
    self.engine = engine

  def display_info(self):
    if self.capacity == 0 and self.engine == "":
      print(f"{self.brand}: {self.model}, Year: {self.year}, Rental Price: ${self.rental_price_per_day}/day")
    elif(self.capacity != 0 and self.engine == ""):
      print(f"{self.brand}: {self.model}, Year: {self.year}, Seats: {self.capacity}, Rental Price: ${self.rental_price_per_day}/day")     
    elif(self.capacity == 0 and self.engine != ""):
      print(f"{self.brand}: {self.model}, Year: {self.year}, Engine: {self.engine}, Rental Price: ${self.rental_price_per_day}/day")
    elif(self.capacity != 0 and self.engine != ""):
      print(f"{self.brand}: {self.model}, Year: {self.year}, Engine: {self.engine}, Seats: {self.capacity}, Rental Price: ${self.rental_price_per_day}/day")          
  
  def calculate_rental_cost(self, days):
    cost = self.rental_price_per_day * days
    print(f"Rental cost for {self.model} for {days} days: ${cost}")

vehicles_list= []
option = 0

while option != 5:
  print("=" * 60)
  print("Select an option: ")
  print("1 ==> Vehicle without additional attributes")
  print("2 ==> Vehicle with seats capacity")
  print("3 ==> Vehicle with engine power")
  print("4 ==> Vehicle with seats capacity and engine power")
  print("5 ==> To exit the system")

  option = int(input("Choice: "))

  if option == 1:
    brand = input("Enter the brand: ")
    model = input("Enter the model: ")
    year = int(input("Enter the year: "))
    rental_price_per_day = float(input("Enter the rental price per day: "))
    vehicle = Vehicle(brand, model, year, rental_price_per_day)
    vehicles_list.append(vehicle)


  elif option == 2:
    brand = input("Enter the brand: ")
    model = input("Enter the model: ")
    year = int(input("Enter the year: "))
    capacity = int(input("Enter the number of seats: "))
    rental_price_per_day = float(input("Enter the rental price per day: "))
    vehicle = Vehicle(brand, model, year, rental_price_per_day)
    vehicle.capacity = capacity
    vehicles_list.append(vehicle)


  elif option == 3:
    brand = input("Enter the brand: ")
    model = input("Enter the model: ")
    year = int(input("Enter the year: "))
    engine = input("Enter the engine's power: ")
    rental_price_per_day = float(input("Enter the rental price per day: "))
    vehicle = Vehicle(brand, model, year, rental_price_per_day)
    vehicle.engine = engine
    vehicles_list.append(vehicle)


  elif option == 4:
    brand = input("Enter the brand: ")
    model = input("Enter the model: ")
    year = int(input("Enter the year: "))
    capacity = int(input("Enter the number of seats: "))
    engine = input("Enter the engine's power: ")
    rental_price_per_day = float(input("Enter the rental price per day: "))
    vehicle = Vehicle(brand, model, year, rental_price_per_day)
    vehicle.capacity = capacity
    vehicle.engine = engine
    vehicles_list.append(vehicle)


for vehicle in vehicles_list:
  vehicle.display_info()