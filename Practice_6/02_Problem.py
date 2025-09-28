lunch_menu=("Welcome Drink", "Veg Starter", "Non-Veg Stater","Veg Main Course","Non-Veg Main Course","Dessert")

sample_tuple="A", "B", "C"
sample_tuple1=("D",)

print("Number of elements in the tuple, lunch_menu:",len(lunch_menu))

print("Element of 2nd index position in lunch_menu:", lunch_menu[2])

print("Concatenating tuples:")

sample_tuple = sample_tuple+sample_tuple1 
print(sample_tuple)

sample_tuple = sample_tuple+("E",)
print(sample_tuple)

sample_tuple = sample_tuple+("F", "G")
print(Sample_tuple)

print("Iterating the tuple using range()")
for index in range(0, len(lunch_menu)): 
  print(lunch_menu[index])

print("Iterating the tuple using keyword in")
for food_type in lunch_menu:
  print(food_type)
