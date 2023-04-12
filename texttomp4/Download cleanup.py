import os
import re
from tqdm import tqdm


folder_name = (
    "D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\texttomp4\\OG Files\\"
)
output_folder = (
    "D:\\Users\\Henry\\Downloads\\github\\Learning-Python\\texttomp4\\Files\\"
)
for file_name in tqdm(os.listdir(folder_name)):
    if file_name.endswith(".txt"):
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, "r", encoding="utf8") as file:
            file_content = file.read()

        chapters = re.split(r"\*Chapter \d+\*", file_content)

        for i, chapter in enumerate(chapters):
            chapter_name = os.path.join(
                output_folder, f"{os.path.splitext(file_name)[0]}_Chapter_{i}.txt"
            )
            with open(chapter_name, "w", encoding="utf8") as file:
                a = file.write(chapter)
                file.close()
