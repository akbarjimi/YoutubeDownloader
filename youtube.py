from random import shuffle
from turtle import done
from pytube import YouTube
from pytube.cli import on_progress
from os.path import exists

if not exists("links.txt"):
    links = open("links.txt", "w")
    links.close()

if not exists("done.txt"):
    links = open("done.txt", "w")
    links.close()

links = list(set(open("links.txt", "r").readlines()))
shuffle(links)
done = list(set(open("done.txt").readlines()))

downloaded = len(done)
total = len(links)

if links:
    while links:
        link = links.pop()
        if link in done:
            print(f"Skipped... \n")
            continue

        youtube = YouTube(link, on_progress_callback=on_progress)
        print("Title: ", youtube.title)
        ys = youtube.streams.get_highest_resolution()
        print(f"Downloading {youtube.title} ...")
        ys.download()
        downloaded += 1
        print(f"Downloaded {youtube.title}")
        print(f"Downloaded {downloaded} links of all {total} \n")
        file_object = open(f"done.txt", 'a')
        file_object.write(link)
        file_object.close()
else:
    print("there is no links to download".title())