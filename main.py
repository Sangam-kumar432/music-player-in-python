 
from pygame import mixer
from tkinter import *
import os

# functions for playing song

def play_song():
    current_song=playlist.get(ACTIVE)
    print("now playing  :  " + current_song)
    mixer.music.load(current_song)
    song_status.set("Playing Music")
    mixer.music.play()

# functions to pause the currently playing song

def pause_song():
    if (song_status.get() != "Music Paused"):
        song_status.set("Music Paused")
        print(song_status.get())
    mixer.music.pause()

def stop_song():
    if (song_status.get() != "Music Stopped"):
        song_status.set("Music stopped")
        print(song_status.get())
    mixer.music.stop()

# functions for resuming the paused song    

def resume_song():
    if (song_status.get() != "Resuming Music"):
        song_status.set("Resuming Music")
        print(song_status.get())
    mixer.music.unpause()

    
# window for music playing

root=Tk()
root.geometry('800x400')
root.config(bg='SlateGray3')
root.title('sangam Music player project')

mixer.init()
song_status=StringVar()
song_status.set("choosing")

# playlist to keep songs accessed from local storage

playlist=Listbox(root,selectmode=SINGLE,bg="white", fg="black",font=('arial',15),height=10,width=100)
playlist.grid(columnspan=4)

os.chdir(r'F:\music from my phone\SnapTube Audio\SnapTube Audio from phone')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

    
# Buttons for palying , pausing and resuming the song 

play_button=Button(root, text="play", command=play_song)
play_button.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
play_button.grid(row=1, column=0)

pause_button=Button(root, text="Pause", command=pause_song)
pause_button.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
pause_button.grid(row=1, column=1)

stop_button=Button(root, text="Stop", command=stop_song)
stop_button.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
stop_button.grid(row=2, column=0)

Resume_button=Button(root, text="Resume", command=resume_song)
Resume_button.config(font=('arial', 20), bg="DodgerBlue2", fg="white", padx=7, pady=7)
Resume_button.grid(row=2, column=1)

mainloop()
print("music interface Ended.")
