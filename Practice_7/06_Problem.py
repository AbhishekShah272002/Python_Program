wt_limit = 30

def baggage_check(baggage_wt):
  extra_baggage_charge=0
  if not(baggage_wt>=0 and baggage_wt<=wt_limit):
    extra_baggage=baggage_wt-wt_limit
    extra_baggage_charge=extra_baggage*100
  return extra_baggage_charge 
  
def update_baggage_limit(new_wt_limit):  
  global wt_limit 
  wt_limit=new_limit  
  print("This airline now allows baggage limit till",wt_limit,"kgs")

def useless_function_to_prove_a_point():
  print("Extra bggage:",extra_baggage)
  print("Extra airline now allows baggage limit till",wt_limit,"kgs")

print("This airline allow baggage limit till",wt_limit,"kgs")
print("Pay the extra baggage charge of",baggage_check(35),"rupees")
print("Extra baggage:",extra_baggage)
print("Extra baggage charge:",extra_baggage_charge)
update_baggage_limit(45)
print("Pay the extra baggage charge of",baggage_check(35),"rupees")
usless_function_to_prove_a_point()
