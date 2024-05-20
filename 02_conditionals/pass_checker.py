password=input("enter pass:")
p_len=len(password)

if p_len<6:
  p_str="weak"
if 6<=p_len<=10:
  p_str="medium"
if p_len>10:
  p_str="strong"

print("pass strength :",p_str)