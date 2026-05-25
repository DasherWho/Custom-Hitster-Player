from Spotify import spotifyAuth
from main import importantInformation
import json

importantInformation()
scope = "streaming user-read-playback-state playlist-read-collaborative"
sp = spotifyAuth(scope=scope)

data = sp.current_playback()

print(json.dumps(data, indent=4))
print("\n\n\n")

if data is not None:
    print(json.dumps(data, indent=4))
    print("What")
else:
    print("No active playback session found. Open Spotify and play a song!")


is_playing = data["is_playing"]

print("Is Spotify playing :")
print(is_playing)