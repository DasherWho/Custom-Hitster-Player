from Spotify import spotifyAuth
import json
import main
import texts
import time, sys, random, pathlib
try:
    import spotipy, dotenv
except:
    print(texts.error["003"])
    time.sleep(3)
    sys.exit()

jsonFile = pathlib.Path("playlist_tracks.json")
main.importantInformation()
scope = "streaming user-read-playback-state playlist-read-collaborative"
sp = spotifyAuth(scope=scope)
playlist_ID = "5YdHUSd8VKnNZgdEzEgjpm"
print("Collecting Playlist Tracks...")

print("[1]Load JSON file | [2]Download Playlist Tracks")
result = int(input())
if result == 1:
    if jsonFile.exists():
        with open(jsonFile) as f:
            data = json.load(f)
    else:
        print("There is no loaded Plalist.")
        print("Loading Playlist from Spotify... This can take a while...")
        tracks = main.extractTracks(playlistID=playlist_ID, sp=sp)

        t = {
        "1":tracks
        }

        with open(jsonFile, "w") as f:
            json.dump(t, f, indent=4)

elif result == 2:
    print("Loading Playlist from Spotify... This can take a while...")
    tracks = main.extractTracks(playlistID=playlist_ID, sp=sp)

    t = {
    "1":tracks
    }

    with open(jsonFile, "w") as f:
        json.dump(t, f, indent=4)

    sys.exit()

list = data["1"]

while True:
    track = random.choice(list)
    playing_tracks = f"https://open.spotify.com/track/{track}"
    
    print("Playing random Song from Playlist with Playlist ID:" + playing_tracks)
    print("\n\n")
    playing_track = [playing_tracks]
    sp.start_playback(uris=playing_track)

    input("To stop the Music press Enter\n\n")
    sp.pause_playback()
    input("If you want to play the next Song press Enter\n\n")
    time.sleep(2)