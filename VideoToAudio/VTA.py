# pip install moviepy

# ********** this is for files present in folder *********

# import moviepy.editor
# from tkinter.filedialog import *

# vid = askopenfilename()
# video = moviepy.editor.VideoFileClip(vid)

# aud = video.audio

# aud.write_audiofile("a1.mp3")

# print("file converted to mp3")

# ********* for online video links *********

# pip install pytubefix
# pip install os_sys

from pytubefix import YouTube
import os

# url input from user
yt = YouTube(
    str(input("Enter the URL of the video you want to download: \n>> ")))

# extract only audio
video = yt.streams.filter(only_audio=True).first()

# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'

# download the file
out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# result of success
print(yt.title + " has been successfully downloaded.")
