"""
    the main area of the music library

"""
from Library import Song, MusicLibrary, create_song

library = MusicLibrary()

#test enviornment
song1 = Song("two trucks", "lemon demon", "nature tapes", "C:/Music/two_trucks.mp3")
library.add_song(song1)
library.save_to_file("library.json")



def choice_handler():
    choice = input("Choose an option: ")
    print("======================")
    print("")

    if choice == "1":
        # View Library
        print("Viewing library...")
        library.display_library()
        choice_handler()
        
    elif choice == "2":
        # Import music
        print("Importing music...")
        print("Songs in library:")
        song = create_song()
        library.add_song(song)
        
        if song is not None:
            print("Song created!")
        choice_handler()

    elif choice == "3":
        # Play music
        print("Playing music...")
        pass
    elif choice == "4":
        # Play Playlist
        print("Playing playlist...")
        pass
    elif choice == "5":
        # Most Played
        print("Showing most played...")
        pass
    elif choice == "6":
        # Exit
        print("Exiting...")
        pass
    else:
        print("Invalid option. Please try again.")
        choice_handler()

#menu
print("+====================+")
print("|     Music Library    |")
print("+====================+")

print("1. View Library")
print("2. Import music")
print("3. Play music")
print("4. Play Playlist")
print("5. Most Played")
print("6. Exit")
  
choice_handler()