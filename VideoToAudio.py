#EXTRTACT MP3 FROM MP4

import moviepy

import moviepy.editor



video = moviepy.editor.VideoFileClip("D:/Videos/golf.mp4") # <-- Input Video File path goes here

audio = video.audio

audio.write_audiofile('D:/Videos/audio_only.mp3') # <--Output Audio File path (And Name) goes here