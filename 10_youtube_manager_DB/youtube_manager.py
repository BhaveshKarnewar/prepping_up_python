import sqlite3
conn =sqlite3.connect("youtubeDB.db")
cursor=conn.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
            )
''')


def list_all():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(f"{row[0]}. {row[1]} Duration: {row[2]}")

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?, ?)",(name,time))
    conn.commit()

def update(video_id,name,time):
    cursor.execute("UPDATE videos SET name=?,time=? WHERE id=?",(name,time,video_id))
    conn.commit()

def delete(video_id):
     cursor.execute("DELETE FROM videos where id = ?", (video_id,))
     conn.commit()

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
              name=input("video name: ")
              time=input("video time: ")
              add_video(name,time)
          case 3:
              video_id=input("enter video id: ")
              name=input("video name: ")
              time=input("video time: ")
              update(video_id,name,time)
          case 4:
              video_id=input("enter video id: ")
         
              delete(video_id)
          case 5:
              print("Exited successfully!")
              break
          case _:
              print("Invalid Choice")

  conn.close()
      

if __name__=="__main__":
    main()