def change_number(num):
  num+=10

def change_list(num_list):
  num_list.append(20)

num_val=10

print("num_val before function call:", num_val)
change_number(num_val)
print("num_val after function call:" num_val)
