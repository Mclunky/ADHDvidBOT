from moviepy.editor import *
from moviepy.editor import TextClip, CompositeVideoClip
import csv
import time
import random
import os

def combine_videos(output_path):
    family_guy_video_path=scan_dataset("my_file.csv", "C:/Users/Ohio/Documents/Shorts Scraper/Videos/Main", 5, 0, 8)
        
    YTshorts_video_path=scan_dataset2("my_file_vert.csv", "C:/Users/Ohio/Documents/Shorts Scraper/Videos/Main", 5, 0, 8)
    # Load the family_guy video
    family_guy_video = VideoFileClip(family_guy_video_path)
                                     
    # Load the YTshorts video
    YTshorts_video = VideoFileClip(YTshorts_video_path)

    scaler=YTshorts_video.w/family_guy_video.w
    newfamily_guyH=family_guy_video.h*scaler
    family_guy_video= family_guy_video.resize(newsize=(YTshorts_video.w,newfamily_guyH))
    YTshorts_video_height_adjuster=int(family_guy_video.h)
    print(YTshorts_video_height_adjuster)

    
    # Overlay the YTshorts video on the family_guy video
    final_video = CompositeVideoClip([YTshorts_video.set_position((0, YTshorts_video_height_adjuster)), family_guy_video ])


    # Set the audio of the final video to be the audio of the family_guy video
    final_video = final_video.set_audio(family_guy_video.audio)
  
    title=YTshorts_video_path.removeprefix('C:/Users/Ohio/Documents/Shorts Scraper/Videos/Main')    
    final_video.write_videofile("C:/Users/Ohio/Documents/Shorts Scraper/Videos/Combined/" + title, audio_codec='aac')


def scan_dataset(dataset, path, sleep=5, start=0, end=10):
    dir_list = os.listdir(path)
    rows = []
    missed_files = []

    # Specifying utf-8 encoding while opening the file
    with open(dataset, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    if end == 0:
        end = len(rows)

    for i in range(start, end):
        print(50 * "*")
        print("Pulling video", i)
        row = rows[i]
        url = row[0]
        filename = row[1]

        family_guy_video_path = os.path.join(path, filename + ".mp4")
        
        if filename + ".mp4" not in dir_list:
            print(url, filename)
        else:
            missed_files.append((url, filename))
            # Example usage
            family_guy_video_path=str(family_guy_video_path)
            return (family_guy_video_path)

def scan_dataset2(dataset, path, sleep=5, start=0, end=10):
    dir_list = os.listdir(path)
    rows = []
    missed_files = []

    # Specifying utf-8 encoding while opening the file
    with open(dataset, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    if end == 0:
        end = len(rows)

    for i in range(start, end):
        print(50 * "*")
        print("Pulling video", i)
        row = rows[i]
        url = row[0]
        filename = row[1]

        YTshorts_video_path = os.path.join(path, filename + ".mp4")
        
        if filename + ".mp4" not in dir_list:
            print(url, filename)
            time.sleep(sleep * random.random())
        else:
            missed_files.append((url, filename))
            # Example usage
            YTshorts_video_path=str(YTshorts_video_path)
            return YTshorts_video_path

# Example usage



combine_videos(str(os.path.join("Videos", "Combined")))