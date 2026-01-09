NAME = "ABHISHEK"
def greet():
    print("Hello, " + NAME + "!")
greet()

print (len(NAME))
print(NAME.lower())
print(NAME.upper())

number_of_characters = len(NAME)
print("The name " + NAME + " has " + str(number_of_characters) + " characters.")
print("The name {} has {} characters.".format(NAME, number_of_characters))
print(f"The name {NAME} has {number_of_characters} characters.")
print("The name %s has %d characters." % (NAME, number_of_characters))