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


def download_video(link, mp):
    try:
        yt = YouTube(link)
        if mp == "mp4":
            filtered_yt = yt.streams.filter(file_extension="mp4").first()
        else:
            filtered_yt = yt.streams.filter(only_audio=True).first()
    except:
        return "Invalid link"

    video_title = clean_title(filtered_yt.title)

    try:
        output = filtered_yt.download(save_path)
        if mp == "mp3":
            base, ext = os.path.splitext(output)
            os.rename(output, base + ".mp3")

        print("Success!")
    except:
        return "Download error"

    return video_title


def download_playlist(link, mp):
    video_list = []

    try:
        playlist = Playlist(link)
    except:
        return "Invalid link"

    playlist_title = clean_title(playlist.title)
    new_directory = save_path + "/" + playlist_title
    try:
        os.mkdir(new_directory)
    except FileExistsError:
        return "Directory exists"

    try:
        for video in playlist.video_urls:
            video_list.append(video)
        print(video_list)

        if mp == "mp4":
            for video in playlist.videos:
                video.streams.filter(file_extension="mp4").first().download(new_directory)
        else:
            for video in playlist.videos:
                output = video.streams.first().download(new_directory)
                base, ext = os.path.splitext(output)
                os.rename(output, base + ".mp3")
    except:
        return "Download error"

    return playlist_title


if __name__ == '__main__':
    print(save_path)

    link = input("Link: ")
    download_playlist(link, "mp3")
