import os
os.chdir('D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\texttomp4') 


from gtts import gTTS
import os
import cv2
from moviepy.editor import *

def text_to_speech(text, filename):
    # Convert the text to speech
    tts = gTTS(text=text, lang='en')
    # Save the speech to an audio file
    tts.save(filename)

def text_to_video(text, audio_filename, video_filename):
    # Initialize the video file with a size and fps
    video = cv2.VideoWriter(video_filename, cv2.VideoWriter_fourcc(*'mp4v'), 20, (1920, 1080))

    # Split the text into lines
    lines = text.split("\n")
    # Calculate the number of lines
    n_lines = len(lines)

    # Load the audio file
    audio = AudioFileClip(audio_filename)

    # Get the duration of the audio
    duration = audio.duration

    # For each line of text
    for i, line in enumerate(lines):
        # Create an image with the line of text
        img = np.zeros((1080, 1920, 3), np.uint8)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, line, (50, int(1080/2)), font, 4, (255, 255, 255), 8, cv2.LINE_AA)

        # Write the image to the video file
        video.write(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # Release the video file
    video.release()

    # Create a video clip from the audio and the video
    video_clip = VideoFileClip(video_filename)
    audio_clip = AudioFileClip(audio_filename)
    final_clip = video_clip.set_audio(audio_clip)

    # Write the final video to file
    final_clip.write_videofile(video_filename)

# Read the text file
with open("input.txt", "r") as file:
    text = file.read()

# Convert the text to speech and save it as an audio file
text_to_speech(text, "speech.mp3")

# Create a video file that displays the text being read, synchronized with the audio
text_to_video(text, "speech.mp3", "video.mp4")
