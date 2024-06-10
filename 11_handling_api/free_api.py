import requests

def fetch_random_user():


    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    data = response.json()
  
    if data["success"] and "data" in data:
      user_data=data["data"]

    
      print(f"Name : {user_data["login"]["username"]}")
      print(f"Password : {user_data["login"]["password"]}")
      print(f"DOB : {(user_data["dob"]["date"])[:10]}")
      print(f"Age : {user_data["dob"]["age"]}")
      print(f"Phone number : {user_data["phone"]}")
      print("\n")

    else:
      raise Exception("fail hai Api")




def main():
  try:
   fetch_random_user()
    
  except Exception as e:
    print(str(e))

if __name__=="__main__":
  main()