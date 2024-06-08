user_num=int(input("enter :"))

for i in range(1,11):
  if i==5:
    continue
  else:
    print(user_num ,"*",i,"=",user_num*i)