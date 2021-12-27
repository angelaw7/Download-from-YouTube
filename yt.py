from pytube import YouTube, Playlist
import os
from dotenv import load_dotenv

load_dotenv()
SAVE_PATH = os.getenv("SAVE_PATH")


def clean_title(title):
    clean = ""
    remove_list = ["/", "\\", "|", ":", "*", "\"", "<", ">"]

    for letter in title:
        if letter not in remove_list:
            clean += letter

    return clean


def download_video(link):
    try:
        yt = YouTube(link)
    except:
        print("Connection error")

    try:
        filtered_yt = yt.streams.filter(file_extension="mp4").first()
    except:
        print("Filter error")

    try:
        filtered_yt.download(SAVE_PATH)
        print("Success!")
    except:
        print("Download error")

    return clean_title(filtered_yt.title)


def download_playlist(link):
    playlist = Playlist(link)

    for video in playlist.video_urls:
        print(video)

    for video in playlist.videos:
        video.streams.first().download(SAVE_PATH)


if __name__ == '__main__':
    print(SAVE_PATH)

    # link = input("Link: ")
    # download_playlist(link)
