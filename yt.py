from pytube import YouTube, Playlist
import os
from dotenv import load_dotenv

load_dotenv()
save_path = os.getenv("SAVE_PATH")


def clean_title(title):
    clean = ""
    remove_list = ["/", "\\", "|", ":", "*", "\"", "<", ">"]

    for letter in title:
        if letter not in remove_list:
            clean += letter

    return clean


def get_path():
    return save_path


def change_path(path):
    global save_path
    save_path = path
    print(save_path)


def download_video(link):
    try:
        yt = YouTube(link)
        filtered_yt = yt.streams.filter(file_extension="mp4").first()
    except:
        return "Invalid link"

    try:
        filtered_yt.download(save_path)
        print("Success!")
    except:
        return "Download error"

    return clean_title(filtered_yt.title)


def download_playlist(link):
    playlist = Playlist(link)

    for video in playlist.video_urls:
        print(video)

    for video in playlist.videos:
        video.streams.first().download(save_path)


if __name__ == '__main__':
    print(save_path)

    # link = input("Link: ")
    # download_playlist(link)
