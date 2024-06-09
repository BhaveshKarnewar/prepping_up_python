# import time

# def cache(func):
#   cache_val={}
#   def wrapper(*args):
#     if args in cache_val:
#       return cache_val[args]
#     result= func(*args)
#     cache_val[args]=result
#     return result
#   return wrapper

# @cache
# def long_running_func(a,b):
#   time.sleep(3)
#   return a+b

# print(long_running_func(1,2))
# print(long_running_func(1,2))
# print(long_running_func(2,5))

import time

def cache(func):
    memory={}
    def wrapper(*args):
        if args in memory:
            return memory[args]
        else:
            result=func(*args)
            memory[args]= result
            return result
    return wrapper
             


@cache
def long_run_func(a,b):
    time.sleep(2)
    print(a+b)


long_run_func(2,3)

long_run_func(2,3)
long_run_func(4,5)