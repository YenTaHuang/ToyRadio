import os
import tkinter as tk

from mutagen.mp3 import MP3
from mutagen.id3 import APIC
from PIL import ImageTk, Image

IMAGE_DEFAULT = 'image_default.png'


class SongSelectionLabel(tk.Label):
    def __init__(self, master, music_folder):
        super().__init__(master, text='test')
        self.configure(background='black')
        self.pack()

        self.song_list = []

        self._add_songs_in_directory(music_folder)

        self.current_ind = 0
        self.current_image = None
        self.current_name = None
        self.ChangeSelectedSong(ind=self.current_ind)

    def _add_songs_in_directory(self, directory):
        for name in os.listdir(directory):
            if name.split('.')[-1] != 'mp3':
                continue
            path = os.path.join(directory, name)
            if os.path.isdir(path):
                self._add_songs_in_directory(path)
                continue

            self.song_list.append({
                'name': name,
                'path': path,
                'image': os.path.join(directory, IMAGE_DEFAULT)
            })
            mp3_file = MP3(path)
            for tag in mp3_file.tags.values():
                if isinstance(tag, APIC):
                    path_image = os.path.join(directory, f'{name}.jpg')
                    with open(path_image, "wb") as f:
                        f.write(tag.data)
                    self.song_list[-1]['image'] = path_image

    def ChangeSelectedSong(self, ind=None, ind_change=0):
        if ind is not None:
            self.current_ind = ind
        else:
            self.current_ind = (self.current_ind + ind_change) % len(self.song_list)
        # create another PhotoImage object using the path of a second image file
        self.current_name = self.song_list[self.current_ind]['name']
        path_image = self.song_list[self.current_ind]['image']

        self.current_image = ImageTk.PhotoImage(Image.open(path_image))
        # self.current_image = tk.PhotoImage(file=path_image)
        # update the image option of the Label widget with the new PhotoImage object
        self.configure(image=self.current_image, text=self.current_name, compound='bottom')

    def GetSelectedSong(self):
        # Get the selected song from the listbox
        # selection = self.music_listbox.get(self.music_listbox.curselection())

        # return self.song_dict.get(selection, None)

        return self.song_list[self.current_ind]['path']
