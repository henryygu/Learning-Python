import os
os.chdir('D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\texttomp4') 

import re
from gtts import gTTS
from pydub import AudioSegment
from moviepy.editor import *

# Load the text file
with open("text.txt", "r") as file:
    text = file.read()

# Split the text into sentences based on new line or full stops
sentences = re.split(r'[.\n]', text)

# Create a list to store the audio and video files
audio_files = []
video_files = []

# Convert each sentence into a text to speech mp3 file and video file
for i, sentence in enumerate(sentences):
    # Convert the sentence into an mp3 file using gTTS
    tts = gTTS(text=sentence, lang='en')
    tts.save(f"sentence_{i}.mp3")
    
    # Load the mp3 file into a pydub AudioSegment object
    audio = AudioSegment.from_file(f"sentence_{i}.mp3", format="mp3")
    
    # Create a video file with the sentence text
    video = TextClip(sentence, font="Arial", fontsize=24, color='white')
    video = video.set_duration(audio.duration_seconds)
    video.write_videofile(f"sentence_{i}.mp4",fps=24)
    
    # Append the audio and video files to the list
    audio_files.append(AudioFileClip(f"sentence_{i}.mp3"))
    video_files.append(VideoFileClip(f"sentence_{i}.mp4"))

# Concatenate all the audio and video files into one final video file
final_video = concatenate_videoclips(video_files, method="compose")
final_audio = concatenate_audioclips(audio_files)

# Overlay the audio on top of the video
final_video = final_video.set_audio(final_audio)

# Write the final video file
final_video.write_videofile("final_video.mp4")