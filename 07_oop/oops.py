class Car:
  total_car=0

  def __init__(self,brand,model):
    self.__brand= brand
    self.__model= model
    Car.total_car+=1
 
  def get_brand(self):
    return self.__brand + " !"

  def full_name(self):
    return f"the brand is {self.__brand} and model is {self.model}"
  
  def hello(self):
    return ("hello user")
  
  @staticmethod
  def gen_des():
    return ("means of transport")
  
  @property
  def model(self):
    return self.__model

  def fuel_type(self):
    return "Petrol or diesel"

class electric_car(Car):
  def __init__(self, brand, model,battery):
    super().__init__(brand, model)
    self.battery= battery

# tesla= electric_car("tesla","s2","100kW")
# print(tesla.get_brand())
# print(tesla.model)
# print(tesla.battery)

# a=isinstance(electric_car,Car)
# print(a)