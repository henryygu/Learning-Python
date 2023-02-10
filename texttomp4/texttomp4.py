import re
import os
from gtts import gTTS
from pydub import AudioSegment
from moviepy.editor import *
import cv2
import numpy as np
import soundfile as sf

os.chdir('D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\texttomp4') 
folder = "Files"
# Loop through all the text files in the folder
for filename in os.listdir(folder):
    print(filename)
    if filename.endswith(".txt"):
    # Load the text file
        with open(os.path.join(folder,filename), "r") as file:
            text = file.read()

        # Split the text into sentences based on new line or full stops
        sentences = re.split(r'[.\n]', text)
        sentences = list(filter(None, sentences))
        # Create a list to store the audio and video files
        audio_files = []
        video_files = []
        
        # Convert each sentence into a text to speech mp3 file and video file
        for i, sentence in enumerate(sentences):
            print(i)
            if len(sentence)!=0:
                print("y")
                # Convert the sentence into an mp3 file using gTTS
                tts = gTTS(text=sentence, lang='en')
                tts.save(f"sentence_{i}.mp3")

                # Load the mp3 file into a pydub AudioSegment object
                audio = AudioSegment.from_file(f"sentence_{i}.mp3", format="mp3")
                
                # Create a video file with the sentence text using OpenCV
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 4
                thickness = 2
                text_size = cv2.getTextSize(sentence, font, font_scale, thickness)[0]
                text_width, text_height = text_size[0], text_size[1]
                height = text_height + 50
                if text_width>1200:
                    width = 1280
                else:
                    width = text_width + 50
                image = np.zeros((height, width, 3), np.uint8)
                cv2.putText(image, sentence, (25, height//2), font, font_scale, (255, 255, 255), thickness)
                video_path = f"sentence_{i}.mp4"
                video_fps = 24
                fourcc = cv2.VideoWriter_fourcc(*"mp4v")
                out = cv2.VideoWriter(video_path, fourcc, video_fps, (width, height))
                for j in range(int(audio.duration_seconds*video_fps)):
                    out.write(image)
                out.release()

                # Append the audio and video files to the list
                audio_files.append(AudioFileClip(f"sentence_{i}.mp3"))
                video_files.append(VideoFileClip(f"sentence_{i}.mp4"))
        
        # Concatenate all the audio and video files into one final video file
        final_video = concatenate_videoclips(video_files, method="compose")
        final_audio = concatenate_audioclips(audio_files)
        
        # Overlay the audio on top of the video
        final_video = final_video.set_audio(final_audio)
        
        # Write the final video file with the same name as the input text file
        #final_video.write_videofile(f"{os.path.splitext(filename)[0]}_final_video.mp4")
        final_video.write_videofile(os.path.join("Output",f"{os.path.splitext(filename)[0]}_final_video.mp4"))
        final_video.close() # close the final video file after saving it
        

        # Delete the intermediate files
        for i in range(len(sentences)):
            try:
                os.remove(f"sentence_{i}.mp3")
                os.remove(f"sentence_{i}.mp4")
            except:
                print(i)