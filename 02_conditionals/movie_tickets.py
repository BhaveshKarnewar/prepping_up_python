# age = int(input("enter age:"))
# day = str(input("Select day (S M T W T F S) :"))

# if age >=0 and age<=17:
#   print("\nticket price is $8")
# elif age >=18 and age<=100:
#   print("\nticket price is $12")
# else:
#   print("\nenter apppropriate age")

# if 0<=age<=100 and day=="W":
#   print("with sp. discount of $2.")



age=int(input("age :"))
day=str(input("day :"))

price= 12 if age>=18 else 8

if day=="wed":
  price-=2

print("price is ",price, "$")


# print(price)