pancard_number = "AABGT6715H"

print("Length of the PAN card number: ", len(pancard_number))

name1 = "PAN "
name2 = "card"
name = name1 + name2
print(name)

print("Iterating the string using range()")
for index in range (0,len(pancrd_number)):
  print(pancrd_number[index])

print("Iterating the string using keyword in")
for value in pancrd_number:
  print(value)

print("Searching for a character in string")
if "Z" in pancard_number:
  print("Charcter is not present")

print("The numbers isn the PAN card number:", pancard_Number[5:9])
