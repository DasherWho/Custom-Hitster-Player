import spotipy
import spotipy.oauth2 as oauth2
import spotipy.util as util
#Uses a better login method with scopes
import os
import dotenv


def spotifyAuth(scope):
    redirect_uri = "https://github.com/DasherWho"
    dotenv.load_dotenv(".env")
    SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
    SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
    USERNAME = os.environ["USERNAME"]

    token = util.prompt_for_user_token(
        username=USERNAME,
        scope=scope,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=redirect_uri
    )
    spotify = spotipy.Spotify(auth=token)
    return spotify
