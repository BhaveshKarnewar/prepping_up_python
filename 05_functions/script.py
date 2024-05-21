# # calculate and return square of a num

# user_num1=int(input("no1: "))
# user_num2=int(input("no2: "))

# def sum(num1,num2):
#   return num1+num2

# result=sum(user_num1,user_num2)
# print("result is",result)



# polymorphism in funcs

# def multiply(p1,p2):
#   return p1*p2

# print(multiply(2,3))
# print(multiply("L",3))
# print(multiply(2,"g"))



# circle area and circumference

# import math
# def circle(radius):
#   area= math.pi * (radius**2)
#   circumference= 2*math.pi*radius
#   return area,circumference

# area, circum=circle(10)
# print(round(area,2))
# print(round(circum,2))


# Default Parameter value

# def greet(name="bunny"):
#   print("Guten tag",name)

# greet()



# lambda func

# cube= lambda x,y: x*y
# print(cube(4,2))



# *args for accepting multiple arguments

# def sum_all(*args):
#   return sum(args)

# print(sum_all(1,2,3))




# **kwargs, named parameters

def print_kwargs(name,power):
  print("NAME", name)
  print("POWER", power)

print_kwargs(power="lazer")