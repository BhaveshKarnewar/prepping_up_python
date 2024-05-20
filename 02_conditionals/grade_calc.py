marks= int(input("\nenter marks :"))

if marks>=90 and marks<=100 :
  print("A")
elif marks>=80 and marks<=89 :
  print("B")
elif marks>=70 and marks<=79 :
  print("C")
elif marks>=60 and marks<=69 :
  print("D")
elif marks>=0 and marks<=59 :
  print("Fail")
else:
  print("saale bhot marunga")
  exit() #to exit py program