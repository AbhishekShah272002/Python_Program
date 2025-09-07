items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_max(items):
  if len(items) == 1:
    return items[0]

val1 = items[0]
val2 = find_max(items[1:])

if val1>val2:
  return val1

else:
  return val2

print(find_max(items))
