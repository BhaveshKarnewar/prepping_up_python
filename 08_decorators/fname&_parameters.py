def debug(func):
  def wrapper(*args,**kwargs):
    arg_value=", ".join(str(arg) for arg in args)
    kwarg_value=", ".join(f"{k}={v}" for k,v in kwargs.items()) 
    print(f"args : {arg_value}")
    print(f"kwargs : {kwarg_value}")
    print(f"caller : {func.__name__}")
    return func(*args,**kwargs)
    
  return wrapper



@debug
def greet(name,greeting="hello"):
  print(f"{greeting}, {name}")

greet("hitesh", greeting="maushi")