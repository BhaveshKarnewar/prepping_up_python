file= open("youtube.txt","w")

try:
  file.write("bhai bhiha jhaska")
finally:
  file.close()

# OR

with open("youtube.txt","w") as file:
  file.write("I will learn german \n")
  file.write("I will visit germany")
