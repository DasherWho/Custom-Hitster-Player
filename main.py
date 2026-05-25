from Spotify import spotifyAuth
import json
import random
import time

def importantInformation():
    print("When Spotipy tries to get the access Token to your account there is a Test wehere a Browser Window is going to open and you have to paste the URL in the Terminal (remenber to use CTR + Shift + V)")

def extractTracks(playlistID, sp):
    results = sp.playlist_tracks(playlist_id=playlistID)
    tracks = results['items']

    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    track_ids = [track['track']['id'] for track in tracks if track['track'] is not None]

    return track_ids

def isPlaying(sp):
    data = sp.current_playback()
    if data is not None:
        pass
    else:
        print("No active playback session found. Restart Spotify and play a song!")
        print("Restarting the Program to reconnect to the Spotify Session.")
        print("Sleeping 20 Sec...")
        time.sleep(10)
        main()
    try:
        is_playing = data["is_playing"]
    except:
        print("WARNING: data has Type none and can't be assigned a var")
        return False
    if is_playing == type(None):
        return False
    else:
        return is_playing

    

def playRandomTrack(trackList, sp):
    is_playing = isPlaying(sp=sp)
    if is_playing == True:
        sp.pause_playback()
    else:
        pass
    
    del is_playing
    sp.add_to_queue(random.choice(trackList))
    sp.next_track()

def main():
    importantInformation()
    scope = "streaming user-read-playback-state playlist-read-collaborative"
    sp = spotifyAuth(scope=scope)
    playlist_ID = "1tYfH1SdNCqlgC7sH1MHJ2"
    tracks = extractTracks(playlistID=playlist_ID, sp=sp)
    playRandomTrack(trackList=tracks, sp=sp)

if __name__ == "__main__":
    main()