pet=input("pet species :")
age=int(input("pet age :"))


if pet=="Dog" or pet=="Cat":
  if 0<=age<=2:
    food="Puppy food"
  elif 5<=age:
    food="senior food"
else:
  print("invalid pet")

print("Reccn :",food,"for",pet)
