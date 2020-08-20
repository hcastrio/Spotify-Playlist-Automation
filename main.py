import json
import requests
from secrets import spotify_user_id, discover_weekly_id
from datetime import date
from refresh import Refresh

class SaveSongs:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = ""
        self.discover_weekly_id = discover_weekly_id
        self.tracks = ""
        self.new_playlist_id = ""

    def call_refresh(self):

        print("Refreshing token...")

        refreshCaller = Refresh()

        self.spotify_token = refreshCaller.refresh()

        self.find_songs()

    def find_songs(self):

        print("Finding songs in discover weekly...")
            
        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            discover_weekly_id)

        response = requests.get(query,
            headers = {"content-type":"application/json",
                        "Authorization": "Bearer {}".format(self.spotify_token)})

        response_json = response.json()

        for i in response_json["items"]:
            self.tracks += (i["track"]["uri"] + ",")
        self.tracks = self.tracks[:-1]

        self.add_to_playlist()

    def add_to_playlist(self):

        print("Adding songs...")

        self.new_playlist_id = self.create_playlist()

        query = "https://api.spotify.com/v1/playlists/{}/tracks?uris={}".format(
            self.new_playlist_id, self.tracks)

        response = requests.post(query, headers={
            "content-type":"application/json",
            "Authorization": "Bearer {}".format(self.spotify_token)
        })

    def create_playlist(self):

        print("Trying to create playlist...")

        today = date.today()

        todayFormatted = today.strftime("%d/%m/%Y")

        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            spotify_user_id)   

        request_body = json.dumps({
            "name": todayFormatted + " Discover Weekly", "description": "Discover weekly rescued from the brick of destruction using Python", "public": True
        })

        response = requests.post(query, data=request_body, headers={
            "content-type":"application/json",
            "Authorization": "Bearer {}".format(self.spotify_token)
        })

        response_json = response.json()

        return response_json["id"]       

a = SaveSongs()
a.call_refresh()