# def debug(func):
#   def wrapper(*args,**kwargs):
#     arg_value=", ".join(str(arg) for arg in args)
#     kwarg_value=", ".join(f"{k}={v}" for k,v in kwargs.items()) 
#     print(f"args : {arg_value}")
#     print(f"kwargs : {kwarg_value}")
#     print(f"caller : {func.__name__}")
#     return func(*args,**kwargs)
    
#   return wrapper



# @debug
# def greet(name,greeting="hello"):
#   print(f"{greeting}, {name}")

# greet("hitesh", greeting="maushi")


def my_decorator(func):
  def wrapper(*args,**kwargs):
    result=func(*args,**kwargs)
    print(f"func name : {func.__name__}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    return result
  return wrapper

@my_decorator
def full_name(*args,**kwargs):
  return 1

full_name("bhavesh", "santosh","karnewar",power="kvh",mausi="kalyan")


full_name("b", "s","k",power=" kalyan",mausi="kvh")

