from tkinter import *
from yt import download_video

root = Tk()
root.title("YouTube to mp4")
# root.iconbitmap("")
root.geometry("600x400")


def download_video_button():
    current = e.get()
    e.delete(0, END)
    download_video(current)


title = Label(root, text="YouTube Download", width=40, height=10)
title.grid(row=0)

e = Entry(root, width=35, borderwidth=1)
e.grid(row=4, column=0, columnspan=3, padx=20, pady=10)
download_button = Button(root, text="Download", padx=20, pady=10, bg="#ADD8E6", command=download_video_button)

download_button.grid(row=4, column=3)

root.mainloop()
