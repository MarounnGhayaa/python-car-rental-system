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

vehicle1 = Vehicle("Car", "Toyota Corolla", 2020, 50)
vehicle2 = Vehicle("Bike", "Yamaha R1", 2019, 30)
vehicle1.capacity = 5
vehicle2.engine = "998cc"
vehicle1.display_info()
vehicle2.display_info()
vehicle1.calculate_rental_cost(3)
vehicle2.calculate_rental_cost(5)

vehicles_list= [vehicle1, vehicle2]

action = input("Create a new vehicle (yes/no): ").lower()

while action != "no":
  brand = input("Enter the brand: ")
  model = input("Enter the model: ")
  year = int(input("Enter the year: "))
  rental_price_per_day = float(input("Enter the rental price per day: "))
  vehicle = Vehicle(brand, model, year, rental_price_per_day)
  vehicles_list.append(vehicle)
  action = input("Create a new vehicle (yes/no): ").lower()

for vehicle in vehicles_list:
  vehicle.display_info()