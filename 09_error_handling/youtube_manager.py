import json

fname="youtube.txt"

def load_data():
  try:
    with open(fname,"r") as file:
     return json.load(file) 
  except FileNotFoundError:
    return []
  
def save_data_helper(videos):
  with open(fname,"w") as file:
    json.dump(videos, file)

def list_all_videos(videos):
    print("*"*70)
    for index,video in enumerate(videos,start=1):
      print(f"{index}: {video["name"]}, {video["time"]}")
    print("*"*70)

def add_videos(videos):
  name=input("Enter video Name:")
  time=input("Enter video Time:")
  videos.append({"name":name, "time":time})
  save_data_helper(videos)


def update_video(videos):
  list_all_videos(videos)
  index=int(input("Which one to be updated: "))
  if 1<= index <= len(videos):
    name=input("enter name: ")
    time=input("enter time: ")

    videos[index-1]={"name":name,"time":time}
    save_data_helper(videos)
  else: 
    print("invalid index")
    update_video(videos)



def delete_video(videos):
   index=int(input("Which one to be deleted: "))
   if 1<= index <= len(videos):
      videos.pop(index-1)
      save_data_helper(videos)
      print("deleted successfully")
   else:
      print("invalid index")

     


def main():
  videos=load_data()

  while True:
    print("\n ||Youtube Manager|| (choose an option)")
    print("1. List all Youtube videos")
    print("2. Add a Youtube Video")
    print("3. Update a Youtube Video details")
    print("4. Delete a youtube video")
    print("5. Exit the App")

    choice= input("Enter Choice :")

    match choice:
      case "1":
        list_all_videos(videos)
      case "2":
        add_videos(videos)
      case "3":
        update_video(videos)
      case "4":
        delete_video(videos)
      case "5":
        print("successfully exited!")
        break
      case _:
        print("invalid Choice") 


# industrial practice
if __name__=="__main__":
  main()

