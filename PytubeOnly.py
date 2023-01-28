import csv
import os
from pytube import Playlist
from pytube import YouTube

# Base output location
base_path = './YTfolder'
#JK
# Read CSV file
with open('./csv/input.csv', 'r') as file:
    reader = csv.reader(file)
    links_and_paths = [row for row in reader]

# Download audio
for link, path in links_and_paths:
    try:
        # check if it's a playlist
        if 'list' in link:
            # create a Playlist object
            pl = Playlist(link)
            # Use title of playlist as the directory name
            playlist_title = pl.title.replace(" ", "_")
            full_path = os.path.join(base_path, path)
            full_path = os.path.join(full_path, playlist_title)
            if not os.path.exists(full_path):
                os.makedirs(full_path)
        
            for video in pl.videos:
                try:
                    audio = video.streams.filter(only_audio=True).first()
                    filename = video.title + ".mp3"
                    if os.path.isfile(os.path.join(full_path, filename)):
                        print(f"{filename} already exists in {full_path}, please check.")
                        continue
                    audio.download(output_path=full_path, filename=filename)
                    print(f"{filename} has been downloaded in {full_path}")
                except Exception as e:
                    print(f"Playlist Error occured : {e}")
        else:
            yt = YouTube(link)
            audio = yt.streams.filter(only_audio=True).first()
            full_path = os.path.join(base_path, path)
            if not os.path.exists(full_path):
                os.makedirs(full_path)
        
            filename = yt.title + ".mp3"
            if os.path.isfile(os.path.join(full_path, filename)):
                print(f"{filename} already exists in {full_path}, please check.")
                continue
            audio.download(output_path=full_path, filename=filename)
            print(f"{filename} has been downloaded in {full_path}")
    except Exception as e:
            print(f"Error occured : {e}")