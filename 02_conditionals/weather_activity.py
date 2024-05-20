weather=(input("weather :")).lower()
# weather2 = weather.lowwer

if weather=="sunny" :
  activity="Go for a walk"
elif weather=="rainy" :
  activity="read a Book"
elif  weather=="snowy" :
  activity="build a snowman"
else:
  activity="invalid weather"

print("sugg act :",activity)