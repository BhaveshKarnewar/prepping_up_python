
import time

def timer(func):
  def wrapper(*args,**kwargs):
    start =time.time()
    result=func(*args,**kwargs)
    end =time.time()
    print(f"{func.__name__} is run in {end -start} time")
    return result
  return wrapper

@timer
def test_fx(n):
  time.sleep(n)

test_fx(2)