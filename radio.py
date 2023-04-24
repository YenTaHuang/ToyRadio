import os
import tkinter as tk
import pygame
from tkinter import filedialog
from modules.gui.song_selection import SongSelectionLabel

MUSIC_FOLDER = "data/songs"


class RadioApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(background='black')
        self.attributes('-fullscreen', True)

        self.title("Toy Radio")
        self.geometry("640x480")

        self.song_selection_label = SongSelectionLabel(self, MUSIC_FOLDER)

        # test_label = tk.Label(self, text='test')
        # test_label.pack()

        self.bind("a", lambda event: self.PlaySong())
        self.bind("b", lambda event: self.StopSong())
        self.bind("x", lambda event: self.PlaySong())
        self.bind("y", lambda event: self.StopSong())
        self.bind("<Left>", lambda event: self.song_selection_label.ChangeSelectedSong(ind_change=1))
        self.bind("<Right>", lambda event: self.song_selection_label.ChangeSelectedSong(ind_change=-1))

        # # create a button to play the selected song
        # self.play_button = tk.Button(self, text="Play", command=self.PlaySong)
        # self.play_button.pack()

    def PlaySong(self):
        pygame.init()

        # get the selected item from the listbox
        selection = self.song_selection_label.GetSelectedSong()

        # load the selected song using pygame
        pygame.mixer.music.load(selection)

        # play the selected song
        pygame.mixer.music.play()

    def StopSong(self):
        pygame.mixer.music.stop()


if __name__ == '__main__':
    radio_app = RadioApp()

    # start the GUI
    radio_app.mainloop()
