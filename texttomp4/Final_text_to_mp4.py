import os
import re
from tqdm import tqdm
from gtts import gTTS
from pydub import AudioSegment
from moviepy.editor import *
import cv2
import numpy as np
from io import BytesIO


def remove_spaces(sentence):
    return sentence.strip() != ""

folder_name = 'D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\texttomp4\\OG Files\\'
output_folder = 'D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\texttomp4\\Files\\'
for file_name in tqdm(os.listdir(folder_name)):
    if file_name.endswith(".txt"):
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'r', encoding="utf8") as file:
            file_content = file.read()
            
        chapters = re.split(r'\*Chapter \d+\*', file_content)
        
    
        for i, chapter in enumerate(chapters):
            chapter_name = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}_Chapter_{i}.txt")
            with open(chapter_name, 'w', encoding="utf8") as file:
                a = file.write(chapter)
                file.close()
    
    


os.chdir('D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\texttomp4') 
folder = "Files"


screensize = (1920,1080)
existingfiles = os.listdir()
mp3_or_mp4_files = [f for f in existingfiles if f.endswith(".mp3") or f.endswith(".mp4")]
i_values = [int(re.search(r"sentence_(\d+)", f).group(1)) for f in mp3_or_mp4_files]
# find the highest value of i
if len(i_values) == 0:
    highest_i=-1
else:
    highest_i = max(i_values)


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
        sentences = list(filter(remove_spaces, sentences))
        # Create a list to store the audio and video files
        audio_files = []
        video_files = []
        
        # Convert each sentence into a text to speech mp3 file and video file
        for i, sentence in enumerate(sentences):
            print(f'{i} out of {len(sentences)}]' )
            if i < highest_i: #sometimes script fails, this will allow you to not have to redo if files already exists
                continue
            else:
                if len(sentence)!=0:
                    print("y")
                    # Convert the sentence into an mp3 file using gTTS
                    tts = gTTS(text=sentence, lang='en')
                    tts.save(f"sentence_{i}.mp3")

                    # Load the mp3 file into a pydub AudioSegment object
                    audio = AudioSegment.from_file(f"sentence_{i}.mp3", format="mp3")
                    
                    # Create a video file with the sentence text
                    video = TextClip(sentence, font="Arial", fontsize=48, color='white', method='caption',align='center',size=screensize)
                    video = video.set_duration(audio.duration_seconds)
                    video.write_videofile(f"sentence_{i}.mp4",fps=24)
                    video.close()

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

