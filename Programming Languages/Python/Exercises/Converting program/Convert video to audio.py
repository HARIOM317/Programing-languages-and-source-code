import moviepy.editor
from tkinter.filedialog import *

vid = askopenfilename()

video = moviepy.editor.VideoFileClip(vid)
aud = video.audio
aud.write_audiofile("Video_to_Audio.mp3")

print(">>>>> -> Audio Created Successfully ! <-")
