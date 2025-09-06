items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binarysearch(item, itemlist):

  listsize = len(itemlist) -1
  lowerIdx = 0
  upperIdx = listsize

while lowerIdx <= upperIdx:
  midPt = (lowerIdx + upperIdx) // 2

if itemlist[midPt] == item:
  return midPt

if item > itemlist[midPt]:
  lowerIdx = midPt + 1
else:
  upperIdx = midPt - 1

if lowerIdx > upperIdx:
  return None

print(binarysearch(23, items))
print(binarysearch(87, items))
print(binarysearch(21, items)
