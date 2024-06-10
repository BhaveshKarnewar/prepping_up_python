import requests

def get_jokes_by_id(id):
  url=f"https://api.freeapi.app/api/v1/public/randomjokes/{id}"

  response= requests.get(url)
  data= response.json()

  if data["success"] and "data" in data:
    print(f"Joke: {data["data"]["content"]}")

  else:
    raise Exception("Fail hai Api")
  

def main():
  try:
    user_input=input("Enter joke Id :")
    get_jokes_by_id(user_input)
    get_jokes_by_id(user_input+"1")
    get_jokes_by_id(user_input-"1")
  except Exception as e:
    print(e)

if __name__=="__main__":
  main()

