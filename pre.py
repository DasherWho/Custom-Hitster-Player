import texts
import json
import random
import time
import sys
import main

try:
    import spotipy, dotenv
except:
    print(texts.error["003"])
    time.sleep(3)
    sys.exit()

from Spotify import spotifyAuth

main.importantInformation()
scope = "streaming user-read-playback-state playlist-read-collaborative"
sp = spotifyAuth(scope=scope)
playlist_ID = "5YdHUSd8VKnNZgdEzEgjpm"
print("\n\n It may take some time to compile the whole Playlist if it is very big\n\n")
tracks = main.extractTracks(playlistID=playlist_ID, sp=sp)
while True:
    print("Playing random Song from Playlist with Playlist ID:" + playlist_ID)
    print("\n\n")
    main.playRandomTrack(trackList=tracks, sp=sp)
    input("To stop the Music press Enter\n\n")
    sp.pause_playback()
    input("If you want to play the next Song press Enter\n\n")
    time.sleep(2)