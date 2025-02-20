import json

def load_data():
    try:
        with open("youtube.txt", 'r') as file:
            return json.load(file)
    except:
        return []


def add_data(videos):
    with open("youtube.txt", "w") as file:
        return json.dump(videos, file)


def list_all_videos(videos):
    for index,video in enumerate(videos, start=1):
        print(f"{index} \t {video["name"]} \t Duration: {video["duration"]}")


def add_video(videos):
    name = input("enter video name ")
    time = input("enter video duration ")
    videos.append({"name": name, "duration": time})
    add_data(videos)


def update_video(videos):
    list_all_videos(videos)
    while True:            
        index = int(input("enter the index which you want to update "))
        if 1 <= index <= len(videos):
            name = input("enter new video name ")
            time = input("enter new video duration ")
            videos[index-1] = {"name": name, "duration": time}
            add_data(videos)
            break
        else:
            print("enter valid index")

def main():
    def delete_video(videos):
        list_all_videos(videos)
        while True:
            index = int(input("enter index which you want deleted "))
            if 1 <= index <= len(videos):
                del videos[index-1]
                add_data(videos)
                break
            else:
                print("enter valid index")
        

    while True:
        print("YOUTUBE MANAGER")
        print("1. list all youtube videos ")
        print("2. add youtube video ")
        print("3. update video ")
        print("4. delete video ")
        print("5. exit ")
        choice = input("enter your choice ")

        videos = load_data()

        match choice:
            case '1':
                print("")
                print("*"*50)
                print("YOUTUBE VIDEOs LISTS")
                print("")
                list_all_videos(videos)
                print("")
                print("*"*50)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("enter valid choice ")

if __name__ == "__main__":
    main()
