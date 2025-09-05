def power(num, pwr):
if pwr == 0:
return 1
else:
return (num * power(num, pwr-1))

def factorial(num):
if num == 0:
  return 1
  else 
  return num * factorial(num - 1) 
 
print("5 to the power of 3 is {power(5, 3)}")
print("2 to the power of 4 is {power(2,4)}")
print("4! is {factorial (4)}") 
print("0! is {factorial (0)}") 
