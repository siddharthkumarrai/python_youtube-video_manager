import sqlite3
connection = sqlite3.connect("youtube_manager.db")

cursor = connection.cursor()

    # Create a table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS videos (
                        video_id INTEGER PRIMARY KEY,
                        video_name TEXT NOT NULL,
                        video_duration TEXT NOT NULL
                    )
               '''
)


def list_all_videos():
    response = cursor.execute("SELECT * FROM videos")
    all_data = response.fetchall()
    return all_data

def add_video(name,duration):
    try:
        cursor.execute("INSERT INTO videos (video_name, video_duration) VALUES (?, ?)", (name, duration))
        connection.commit()
        print("Data inserted successfully.")
    except sqlite3.IntegrityError:
        print("Error: Cannot insert NULL values.")

def update_video(name,duration,video_id):
    try:
        query = "UPDATE videos SET video_name = ?, video_duration = ? WHERE video_id = ?"
        cursor.execute(query,(name,duration,video_id))
        connection.commit()
        print("update succesfully")
    except sqlite3.Error as e:
        print(f"ERROR in Updation: {e}")

# DELETE FROM employees WHERE employee_id = 123;
def delete_video(id):
    try:
        query = "DELETE FROM videos WHERE video_id = ?"
        cursor.execute(query,(id,))
        connection.commit()
        print("video successfull deleted")
    except sqlite3.Error as e:
        print(f"Error in delete video : {e}")

        


def main():
    while True:
        print("YOUTUBE MANAGER WITH Sqlite3 ")
        print("1. List all videos ")
        print("2. Add new videos ")
        print("3. Update videos ")
        print("4. Delete videos ")
        print("5. exit ")

        choice = input("enter your choice: ")
        if choice == "1":
            print("*"*50)
            print("\t \t videos list")
            print("")
            for all_list in list_all_videos():
                print(f"{all_list[0]}\t{all_list[1]}\t Duration:{all_list[2]}") 
            print("")
            print("*"*50) 

        elif choice == "2":
            name = input("enter video name: ")
            time = input("enter video duration: ")
            add_video(name,time)
        elif choice == "3":
            video_id = int(input("enter video_id which you want to update: "))
            new_name = input("enter new name: ")
            new_duration = input("enter the video duration: ")
            update_video(new_name,new_duration,video_id)
        elif choice == "4":
            video_id = int(input('enter video_id which you want to be deleted: '))
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()
