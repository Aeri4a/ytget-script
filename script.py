from pytube import YouTube

print("What would you like to do?")
print("--------------------------------")
print("1) Download video from link")
print("2) Download videos from links listed in the file")
print("3) Exit")

active = True

while(active):
    choice = input("Option: ")

    if choice == "1":
        link = input("Paste your link: ")
        yt = YouTube(link)

        print("\n")
        print("Title: ", yt.title)

        print("Downloading...")
        yd = yt.streams.get_highest_resolution()
        yd.download('./downloaded')

        print("Done")
        active = False

    elif choice == "2":
        file = open("list_videos.txt", "r")
        list = file.readlines()
        list = [i.strip() for i in list]

        if list == []:
            print("File is empty!")
            continue
        else:
            for idx, l in enumerate(list):
                print("Downloading... ", idx+1)
                yt = YouTube(l)
                yd = yt.streams.get_highest_resolution()
                yd.download('./downloaded')

        print("Done")
        active = False

    elif choice == "3":
        active = False

    else:
        print("Wrong option, try again")