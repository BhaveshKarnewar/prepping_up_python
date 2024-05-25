from oops import Car



class Battery:
  def battery(self):
    return "Battery is present"

class Engine:
 def Engine(self):
    return "Engine is present"


class electric_car2(Battery,Engine,Car):
  pass

punch= electric_car2("tata","Punch")
print(punch.model)
print(punch.battery())
print(punch.Engine())