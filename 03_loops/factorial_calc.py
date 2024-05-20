# user_num=int(input("enter :"))


# i=user_num-1
# factorial=user_num*i
# while i>1:
#   i=i-1
#   print(i)
#   factorial*=i

# print(factorial)


user_num=int(input("enter :"))

factorial=1

while user_num > 1:
  factorial=factorial*user_num
  
  user_num-=1


print("factorial is", factorial)