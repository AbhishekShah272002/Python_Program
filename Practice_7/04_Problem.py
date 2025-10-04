def disply1(flight_number, seating_capacity):
  print("Flight Number:", flight_number)
  print("Seating Capacity:", seating_capacity)

print("code-1: positional arguments")
display1("AI789",200)

def display2(flight_number, seating_capacity):
  print("Flight Number:", flight_number)
  print("Seating Capacity:", seating_capacity)

print("----------------------------------------------")
print("code-2: keyword arguments")
display2(seating_capacity = 250, flight_number="AI789")

def display3(flight_number, flight_make = "Boeing", seating_capacity = 150):
  print("Flight Number:", flight_number)
  print("Flight Make:", flight_make)
  print("Seating Capacity:" seating_capacity)
