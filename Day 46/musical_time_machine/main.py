import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime as dt

endpoint = "https://www.billboard.com/charts/hot-100/"
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(url=f"{endpoint}/{date}").text

soup = BeautifulSoup(response, "html.parser")
all_songs = soup.select(selector="div.o-chart-results-list-row-container ul li h3")
tracks = [tag.getText().strip() for tag in all_songs]

# spotify api authentication
auth = SpotifyOAuth(client_id=os.environ.get("spotifyID"),
                    client_secret=os.environ.get("spotifySecret"),
                    redirect_uri=os.environ.get("spotifyRedictURI"),
                    scope="playlist-modify-public")
sp = spotipy.Spotify(auth_manager=auth)

# search tracks on spotify and store their ids in a list
track_ids = []
year = dt.datetime.strptime(date, '%Y-%m-%d').year

for track in tracks:
    # # search song
    track_id = sp.search(q=f"track: {track} year: {year}", type="track", limit=1, market="CA")["tracks"]["items"][0]["id"]
    track_ids.append(track_id)

# get user playlist
playlists_content = sp.current_user_playlists()["items"]
playlist_names = [playlist["name"] for playlist in playlists_content]

playlist_id = None
user_id = sp.current_user()['id']

spotify_playlist = f"Billboard 100 for {date}"  # playlist name to save tracks on
if spotify_playlist not in playlist_names:
    new_playlist = sp.user_playlist_create(user=user_id, name=spotify_playlist,
                                           public=True, collaborative=False,
                                           description="Generated using Python")
    playlist_id = new_playlist["id"]

else:
    for playlist in playlists_content:
        if spotify_playlist in playlist.values():
            playlist_id = playlist["id"]

# add songs to playlist
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=track_ids)
