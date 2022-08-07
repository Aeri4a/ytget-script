from pytube import YouTube
import os, time

print("What would you like to do?")
print("\n")
print("--Video----------------------------")
print("1) Download video from link")
print("2) Download videos from file")
print("\n")
print("--Music----------------------------")
print("3) Download music from link")
print("4) Download music from file")
print("\n")
print("5) Exit")
print("--------")


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
        time.sleep(2)
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
                yt = YouTube(l)
                print("Title: ", yt.title)
                print("Downloading... ", idx + 1)
                yd = yt.streams.get_highest_resolution()
                yd.download('./downloaded')

        print("Done")
        time.sleep(2)
        active = False

    elif choice == "3":
        link = input("Paste your link: ")
        yt = YouTube(link)

        print("\n")
        print("Title: ", yt.title)

        print("Downloading...")
        yd = yt.streams.get_audio_only()
        out_file = yd.download('./downloaded')

        name, ext = os.path.splitext(out_file)
        new_file = name + ".mp3"
        os.rename(out_file, new_file)

        print("Done")
        time.sleep(2)
        active = False

    elif choice == "4":
        file = open("list_music.txt", "r")
        list = file.readlines()
        list = [i.strip() for i in list]

        if list == []:
            print("File is empty!")
            continue
        else:
            for idx, l in enumerate(list):
                yt = YouTube(l)
                print("Title: ", yt.title)
                print("Downloading... ", idx + 1)
                yd = yt.streams.get_audio_only()
                out_file = yd.download('./downloaded')

                name, ext = os.path.splitext(out_file)
                new_file = name + ".mp3"
                os.rename(out_file, new_file)


        print("Done")
        time.sleep(2)
        active = False

    elif choice == "5":
        active = False

    else:
        print("Wrong option, try again")