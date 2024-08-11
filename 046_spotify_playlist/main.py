import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.exceptions import SpotifyException
from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI
from typing import List, Optional

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_SCOPE = "playlist-modify-public"

def scrape_top_songs(date: str) -> List[dict]:
    """
    Scrapes the top songs from the Billboard Hot 100 chart for a given date.

    Args:
        date (str): The date in the format 'YYYY-MM-DD'.

    Returns:
        List[dict]: A list of dictionaries containing song titles and artist names.
    """
    response = requests.get(f"{BILLBOARD_URL}{date}")
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    song_elements = soup.select("li > h3#title-of-a-story")
    artist_elements = soup.select("li > span.c-label.a-no-trucate")
    
    songs = []
    for song, artist in zip(song_elements, artist_elements):
        songs.append({
            "title": song.get_text(strip=True),
            "artist": artist.get_text(strip=True)
        })
    
    return songs

def get_spotify_client(client_id: str, client_secret: str, redirect_uri: str) -> Optional[spotipy.Spotify]:
    """
    Authenticates with the Spotify API using OAuth and returns a Spotify client.

    Args:
        client_id (str): The Spotify client ID.
        client_secret (str): The Spotify client secret.
        redirect_uri (str): The redirect URI for OAuth.

    Returns:
        Optional[spotipy.Spotify]: An authenticated Spotify client, or None if authentication fails.
    """
    try:
        auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=SPOTIFY_SCOPE)
        return spotipy.Spotify(auth_manager=auth_manager)
    except SpotifyException as e:
        print(f"Error authenticating with Spotify: {e}")
        return None

def search_spotify_song(spotify_client: spotipy.Spotify, song_title: str, artist_name: str) -> Optional[str]:
    """
    Searches for a song on Spotify using both the song title and artist name, and returns its URI.

    Args:
        spotify_client (spotipy.Spotify): The Spotify client.
        song_title (str): The title of the song to search for.
        artist_name (str): The name of the artist.

    Returns:
        Optional[str]: The Spotify URI of the song, or None if not found.
    """
    query = f"track:{song_title} artist:{artist_name}"
    try:
        results = spotify_client.search(q=query, type='track', limit=1)
        tracks = results.get('tracks', {}).get('items', [])
        return tracks[0]['uri'] if tracks else None
    except SpotifyException as e:
        print(f"Error searching for song '{song_title}' by '{artist_name}': {e}")
        return None

def create_spotify_playlist(spotify_client: spotipy.Spotify, playlist_name: str) -> Optional[str]:
    """
    Creates a new playlist on Spotify.

    Args:
        spotify_client (spotipy.Spotify): The Spotify client.
        playlist_name (str): The name of the playlist to create.

    Returns:
        Optional[str]: The Spotify ID of the created playlist, or None if creation fails.
    """
    try:
        user_id = spotify_client.me()['id']
        playlist = spotify_client.user_playlist_create(user_id, playlist_name)
        return playlist['id']
    except SpotifyException as e:
        print(f"Error creating playlist '{playlist_name}': {e}")
        return None

def add_songs_to_playlist(spotify_client: spotipy.Spotify, playlist_id: str, song_uris: List[str]) -> bool:
    """
    Adds songs to a Spotify playlist.

    Args:
        spotify_client (spotipy.Spotify): The Spotify client.
        playlist_id (str): The ID of the playlist to add songs to.
        song_uris (List[str]): A list of Spotify URIs for the songs to add.

    Returns:
        bool: True if songs were added successfully, False otherwise.
    """
    try:
        spotify_client.playlist_add_items(playlist_id, song_uris)
        return True
    except SpotifyException as e:
        print(f"Error adding songs to playlist: {e}")
        return False

def main():
    """
    Main function to scrape top songs from Billboard and search for their Spotify URIs.
    """
    date = input("Enter the date (YYYY-MM-DD) for the Billboard Hot 100 chart: ")
    top_songs = scrape_top_songs(date)
    spotify_client = get_spotify_client(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)
    
    if not spotify_client:
        print("Failed to authenticate with Spotify. Exiting.")
        return

    playlist_name = f"Billboard Hot 100 - {date}"
    playlist_id = create_spotify_playlist(spotify_client, playlist_name)
    if not playlist_id:
        print(f"Failed to create playlist '{playlist_name}'")
        return

    print(f"Playlist '{playlist_name}' created successfully with ID: {playlist_id}")

    song_uris = [
        search_spotify_song(spotify_client, song["title"], song["artist"]) 
        for song in top_songs
    ]
    song_uris = [uri for uri in song_uris if uri]

    if not song_uris:
        print("No songs to add to playlist")
        return

    if add_songs_to_playlist(spotify_client, playlist_id, song_uris):
        print("Songs added to playlist successfully")
    else:
        print("Failed to add songs to playlist")

if __name__ == "__main__":
    main()