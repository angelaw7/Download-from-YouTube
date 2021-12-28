from tkinter import *
from tkinter import filedialog

from yt import download_video, download_playlist, change_path, get_path

root = Tk()
root.title("YouTube to mp4")
# root.iconbitmap("")
root.geometry("600x400")
root.directory = get_path()


def change_save_path():
    root.directory = filedialog.askdirectory()
    if root.directory != "":
        print("not none")
        download_location.config(text="Save directory: \"" + root.directory + "\"")
        change_path(root.directory)


def reset_messages():
    success_text.config(text="")
    error_text.config(text="")


def download_video_button():
    reset_messages()

    current = input_field.get()
    input_field.delete(0, END)
    is_downloading_text.grid(row=6)
    if select_video_playlist.get() == "video":
        if select_mp3_mp4 == "mp3":
            res = download_video(current, "mp3")
        else:
            res = download_video(current, "mp4")
    else:
        if select_mp3_mp4 == "mp3":
            res = download_playlist(current, "mp3")
        else:
            res = download_playlist(current, "mp4")
    is_downloading_text.config(text="")

    if res == "Invalid link" or res == "Download error":
        print("failed")
        error_type = res
        error_text.config(text="Error: " + error_type)
    elif res == "Directory exists":
        error_text.config(text="Error: Directory with the playlist name already exists -- "
                               "Playlist might be downloaded already\nIf not, please rename that directory")
    else:
        print(res)
        success_text.config(text="Successfully downloaded " + res + "!", wraplength=500)


# Title
title = Label(root, text="Download from YouTube", width=40, height=4, font=("Arial", 16))
title.grid(row=0, column=0, columnspan=4)

# Radio buttons to select video/playlist
select_video_playlist = StringVar(root, "video")
video_option = Radiobutton(root, text="Single video", variable=select_video_playlist, value="video")
video_option.grid(row=1, column=1)
playlist_option = Radiobutton(root, text="Playlist", variable=select_video_playlist, value="playlist")
playlist_option.grid(row=2, column=1)

# Radio buttons to select mp3/mp4
select_mp3_mp4 = StringVar(root, "mp4")
mp3_option = Radiobutton(root, text="mp3 (audio)", variable=select_mp3_mp4, value="mp3")
mp3_option.grid(row=1, column=2)
mp4_option = Radiobutton(root, text="mp4 (video)", variable=select_mp3_mp4, value="mp4")
mp4_option.grid(row=2, column=2)

# Save directory
download_location = Label(root, text="Save directory: \"" + root.directory + "\"")
download_location.grid(row=3, column=0, columnspan=3)

# Change directly button
change_path_button = Button(root, text="Change directory", padx=20, pady=10, bg="#A9A9A9", command=change_save_path)
change_path_button.grid(row=3, column=3)

# Input field
input_field = Entry(root, width=60, borderwidth=1)
input_field.grid(row=4, column=0, columnspan=3, padx=20, pady=4)

# Download button
download_button = Button(root, text="Download", padx=20, pady=10, bg="#ADD8E6", command=download_video_button)
download_button.grid(row=4, column=3)

# Text while/after downloading
is_downloading_text = Label(root, text="Downloading...", width=20, height=10)
success_text = Label(root, text="")
success_text.grid(row=6, column=0, columnspan=4)
error_text = Label(root, text="")
error_text.grid(row=6, column=0, columnspan=4)

# Main
root.mainloop()
