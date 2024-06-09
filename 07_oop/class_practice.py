class Car:

  count=0

  def __init__(self,brand,model):
    self.__brand=brand
    self.model=model
    Car.count+=1

  def getter(self):
    return self.__brand

  def greet(self, name):
    return f"Hello {name}, -{self.__brand} {self.model}"
  
  def fuel_type(self):
    return "Tel Mitti ka"
  
  @staticmethod
  def gen_info():
   return "cars are amazing"
  

class Ev(Car):
  def __init__(self, brand, model,battery):
    super().__init__(brand, model)
    self.battery=battery

  def fuel_type(self):
    return "Electrifying current"


Punch= Car("tata","punch")
print(Car.gen_info())

# Comet= Ev("Mg","Comet","120W")
# print(Comet.fuel_type())

