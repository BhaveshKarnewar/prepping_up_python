fruit_color=input("fruit color :")

if fruit_color=="Green" :
  fruit="unripe"
elif fruit_color=="Yellow" :
  fruit="ripe"
elif fruit_color=="Brown" :
  fruit="Overripe"
else:
  print("galat ghanta")
  exit()


print("Fruit is",fruit)