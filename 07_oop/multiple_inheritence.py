from oops import Car

punch= Car("tata","Punch")
print(punch.model)

class Battery:
  pass

class Engine:
  pass


class electric_car(Battery,Engine,Car):
  pass