from pymongo import MongoClient
from bson import ObjectId

client= MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.vnjrzrs.mongodb.net/"
                    , tlsAllowInvalidCertificates=True)

db= client["ytmanager"]
video_collection= db["videos"]

# print(video_collection)


# functions

def add_video(name,time):
    video_collection.insert_one({"name":name, "time":time})

def list_all():
   for video in video_collection.find():
       print(f"Id: {video["_id"]}, name: {video["name"]}, duration: {video["time"]}")

def update(video_id,new_name,new_time):
    video_collection.update_one(
        {"_id":ObjectId(video_id)},
        {"$set":{"name":new_name,"time":new_time}}
        )

def delete(video_id):
    video_collection.delete_one({"_id":ObjectId(video_id)})

def main():
  while True:
      print("\n ||Youtube Manager|| (choose an option)")
      print("1. List all Youtube videos")
      print("2. Add a Video")
      print("3. Update a Video")
      print("4. Delete a video")
      print("5. Exit")

      choice= int(input("Enter Choice: "))

      match choice:
          case 1:
              list_all()
          case 2:
              name=input("enter name : ")
              time=input("enter time : ")
              add_video(name,time)
          case 3:
              video_id= input("enter video ID : ")
              name=input("enter name : ")
              time=input("enter time : ")

              update(video_id,name,time)
          case 4:
              video_id= input("enter video ID : ")
              delete(video_id)
          case 5:
              print("Exited successfully!")
              break
          case _:
              print("Invalid Choice")




if __name__=="__main__":
  main()