from tkinter import *
from yt import download_video

root = Tk()
root.title("YouTube to mp4")
# root.iconbitmap("")
root.geometry("600x400")


success_text = Label(root, text="")
error_text = Label(root, text="")


def reset_messages():
    global success_text, error_text
    success_text.grid_remove()
    error_text.grid_remove()


def download_video_button():
    global success_text, error_text
    reset_messages()

    current = e.get()
    e.delete(0, END)
    is_downloading_text.grid(row=6)
    res = download_video(current)
    is_downloading_text.grid_remove()

    if res == "Invalid link" or res == "Download error":
        print("failed")
        error_type = res
        error_text = Label(root, text="Error: " + error_type)
        error_text.grid(row=6, column=0, columnspan=4)
    else:
        print(res)
        video_title = res
        success_text = Label(root, text="Successfully downloaded " + video_title + "!", wraplength=500)
        success_text.grid(row=6, column=0, columnspan=4)


title = Label(root, text="YouTube Download", width=40, height=4, font=("Arial", 16))
title.grid(row=0, column=0, columnspan=4)

e = Entry(root, width=60, borderwidth=1)
e.grid(row=4, column=0, columnspan=3, padx=20, pady=4)
download_button = Button(root, text="Download", padx=20, pady=10, bg="#ADD8E6", command=download_video_button)

download_button.grid(row=4, column=3)

is_downloading_text = Label(root, text="Downloading...", width=20, height=10)

root.mainloop()
