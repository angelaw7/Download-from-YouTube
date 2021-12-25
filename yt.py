from pytube import YouTube, Playlist
import os

SAVE_PATH = os.environ.get("SAVE_PATH")


def download_video(link):
    try:
        yt = YouTube(link)
    except:
        print("Connection error")

    try:
        filtered_yt = yt.streams.filter(file_extension="mp4").first()
    except:
        print("Error")

    try:
        filtered_yt.download(SAVE_PATH)
        print("Success!")
    except:
        print("Download error")


def download_playlist(link):
    playlist = Playlist(link)

    for video in playlist.video_urls:
        print(video)

    for video in playlist.videos:
        video.streams.first().download(SAVE_PATH)


def testing(a):
    print("yay " + a)


if __name__ == '__main__':
    link = input("Link: ")
    download_playlist(link)
