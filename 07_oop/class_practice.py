class Car:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model

  def greet(self):
    return f"Hello user, -{self.brand} {self.model} "
  

class Ev(Car):
  def __init__(self, brand, model, battery):
    super().__init__(brand, model)
    self.battery=battery

  def evGreet(self):
    return "Hello user, you are Gay!"

punch= Ev("Tata", "Punch", "120 W")

print(punch)
print(punch.brand)
print(punch.model)
print(punch.battery)
p=punch.greet()
q=punch.evGreet()
print(p)
print(q)