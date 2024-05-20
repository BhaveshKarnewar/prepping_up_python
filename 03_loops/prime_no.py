# number=int(input("enter no:"))

# if number%2==0 or number%3==0 or number%5==0 or number%7==0:
#   print("not a prime no")
# else:
#   print("Prime number")


number=int(input("enter no:"))

is_prime=True

if number>1:
  for i in range(2,number):
    if (number%i)==0:
      is_prime= False
      break

print(is_prime)