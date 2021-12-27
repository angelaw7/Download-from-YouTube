from tkinter import *
from tkinter import filedialog

from yt import download_video

root = Tk()
root.title("YouTube to mp4")
# root.iconbitmap("")
root.geometry("600x400")
root.directory = "C:/Users/Downloads"


def change_save_path():
    root.directory = filedialog.askdirectory()
    download_location.config(text=root.directory)


def reset_messages():
    success_text.config(text="")
    error_text.config(text="")


def download_video_button():
    change_save_path()
    reset_messages()

    current = e.get()
    e.delete(0, END)
    is_downloading_text.grid(row=6)
    res = download_video(current)
    is_downloading_text.grid_remove()

    if res == "Invalid link" or res == "Download error":
        print("failed")
        error_type = res
        error_text.config(text="Error: " + error_type)

    else:
        print(res)
        video_title = res
        success_text.config(text="Successfully downloaded " + video_title + "!", wraplength=500)


title = Label(root, text="YouTube Download", width=40, height=4, font=("Arial", 16))
title.grid(row=0, column=0, columnspan=4)

download_location = Label(root, text=root.directory)
download_location.grid(row=3, column=0, columnspan=3)

e = Entry(root, width=60, borderwidth=1)
e.grid(row=4, column=0, columnspan=3, padx=20, pady=4)
download_button = Button(root, text="Download", padx=20, pady=10, bg="#ADD8E6", command=download_video_button)

download_button.grid(row=4, column=3)

is_downloading_text = Label(root, text="Downloading...", width=20, height=10)
success_text = Label(root, text="")
error_text = Label(root, text="")
error_text.grid(row=6, column=0, columnspan=4)
success_text.grid(row=6, column=0, columnspan=4)


root.mainloop()
