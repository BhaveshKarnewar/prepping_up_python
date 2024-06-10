import requests

def get_stocks(code):
  url= f"https://api.freeapi.app/api/v1/public/stocks/{code}"
  response= requests.get(url)
  data = response.json()

  if data["success"] and "data" in data:
    MarketCap= data["data"]["MarketCap"]
    CurrentPrice= data["data"]["CurrentPrice"]
    BookValue= data["data"]["BookValue"]

    print(f"MarketCap : {MarketCap}")
    print(f"CurrentPrice : {CurrentPrice}")
    print(f"BookValue : {BookValue}")
  
  else:
    raise Exception("Fail hai Api")




def main():
    try:
      get_stocks("SBC")
     
    except Exception as e:
      print(e)

if __name__=="__main__":
  main()