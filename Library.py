#library- for songs
"""
Ex:
    Title,
    Artist,
    Album,
    File path,
    Play count
    (if you forget the commas i will smite you)
"""
from pathlib import Path
import json

SUPPORTED_EXTENSIONS = {
    ".mp3",
    ".wav",
    ".flac",
    ".mp4",
    ".mkv"
}

class Song:
    def __init__(self, title, artist, album, filepath):
        self.title = title
        self.artist = artist
        self.album = album
        self.filepath = filepath
        self.play_count = 0

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Artist: {self.artist}")
        print(f"Album: {self.album}")
        print(f"File Path: {self.filepath}")
        print(f"Play Count: {self.play_count}")

    def to_dict(self):
        return {
            "title": self.title,
            "artist": self.artist,
            "album": self.album,
            "filepath": self.filepath,
            "play_count": self.play_count
        }

class MusicLibrary:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def display_library(self):
        for song in self.songs:
            song.display_info()
    
    def save_to_file(self, filename):
        data = {
            "songs": []
        }
        for song in self.songs:
            data["songs"].append(song.to_dict())
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    

def create_song():
    title = input("Enter song title: ")
    artist = input("Enter song artist: ")
    album = input("Enter song album: ")
    
    filepath = input("Enter file path (e.g., C:/Music/Song.mp3): ").strip()
    filepath = Path(filepath)
    if not filepath.exists():
        print("File does not exist.")
        return None
    if not filepath.is_file():
        print("Path is not a file.")
        return None
    if filepath.suffix.lower() not in SUPPORTED_EXTENSIONS:
        print("Unsupported file type.")
    
    return Song(title, artist, album, filepath)
