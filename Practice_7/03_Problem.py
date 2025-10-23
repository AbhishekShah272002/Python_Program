def check_in(baggage,bording_pass):
  if(baggage>=1 and baggage<=30):
    boarding_pass = "Issued"

def update_seat(seat_list): 
  seat_list[1]=25  
 
boarding_pass = "Not Issued"
print("boarding_pass before function call:", boarding_pass) 
check_in(25,boarding_pass)
print("boarding_pass after after function call:", boarding_pass)
print("boarding_pass, a string is immutable")
print("-------------------------------------------")

passenger_seat = ["Jack","NA"]
print("passenger_seat before function call:", passenger_seat)
upadte_seat(passenger_seat)
print("Passenger_seat after function call:", passenger_seat)
print("passenger_seat, a list is mutable")
