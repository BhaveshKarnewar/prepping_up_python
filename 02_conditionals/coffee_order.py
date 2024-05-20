order_size = input("size :").lower()
extra_shot= input("extra shot (True/False) :")

if extra_shot :
  print(order_size,"Coffee with Extra Shot")
else:
  print(order_size,"Coffee only")