import os
import emotion_detection as de
from pygame import mixer
# Starting the mixer
mixer.init()

# Loading the single song
#mixer.music.load("D:\Music\Waalian - Harnoor 320 Kbps(pagalworldu.com).mp3")
# To load list of songs in directory

mood = de.detect_my_emotion()
print(mood)
listPath =""
if  mood == 'happy'and mood == 'neutral':
    listPath = "D:\Music\happy\\"
elif mood == 'sad':
    listPath = "D:\Music\sad\\"
elif mood == 'fear':
    listPath = "D:\Music\devotional\\"

print(listPath)
song_list = os.listdir(listPath)

# load file according to mood of user

for song in song_list:
    if song.endswith(".mp3"):
        file_path=listPath+song
        print(file_path)
        mixer.music.load(file_path)
        mixer.music.set_volume(0.7)
        mixer.music.play()

        print("Press 'n' to next")
        print("Press 'e' to exit the program")
        query = input("  ")

        if query == 'n':
             # Go next the music
             mixer.music.pause()
        elif query == 'e'  :
             # Stop the mixer
             mixer.music.stop()
             break




