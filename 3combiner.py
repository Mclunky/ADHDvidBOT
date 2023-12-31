from moviepy.editor import *
import csv
import time
import random
import os

def combine_videos(main_video_path, second_video_path, output_path):
    # Load the main video
    main_video = VideoFileClip(main_video_path)
    
    # Load the second video
    second_video = VideoFileClip(second_video_path)
    
    # Calculate new height for the second video to maintain aspect ratio
    new_height = int(main_video.w * second_video.h / second_video.w)
    
    # Resize the second video
    second_video = second_video.resize(newsize=(main_video.w, new_height))
    
    # Calculate a random start time for the second video
    max_start_time = second_video.duration - main_video.duration
    if max_start_time > 0:
        start_time = random.uniform(0, max_start_time)
        second_video = second_video.subclip(start_time, start_time + main_video.duration)
    
    # Calculate the position where the second video should be placed on the main video
    x_pos = 0  # x position is 0
    y_pos = main_video.h - new_height  # y position is the height of the main video minus the height of the second video
    
    # Overlay the second video on the main video
    final_video = CompositeVideoClip([main_video, second_video.set_position((x_pos, y_pos))])
    
    # Set the audio of the final video to be the audio of the main video
    final_video = final_video.set_audio(main_video.audio)
    
    # Write the result to a file
    final_video.write_videofile(output_path, audio_codec='aac')

def download_dataset(dataset, path, sleep=5, start=0, end=0):
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

        main_video_path = os.path.join(path, filename + ".mp4")
        
        if filename + ".mp4" not in dir_list:
            print(url, filename)
            time.sleep(sleep * random.random())
        else:
            missed_files.append((url, filename))
            # Example usage
            combine_videos(main_video_path,'test.mp4', os.path.join("Videos", "Combined", filename + '.mp4'))

# Example usage
download_dataset("my_file_vert.csv", "C:/Users/Ohio/Documents/Shorts Scraper/Videos/Main", 5, 0, 7)
