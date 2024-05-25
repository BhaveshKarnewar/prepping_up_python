items=["apple","banana","orange","maushi","banana","maushi"]

# for val in items:
#   if items.count(val)>1:
#     print(val)
#     break
  
uni_item =set()

for item in items:
  if item in uni_item:
    print("duplo :", item)
    exit()
  uni_item.add(item)