import os
import requests
from django.shortcuts import render

PICTURES_URL = os.environ.get("PICTURES_URL", "http://pictures:3000/picture")
SONGS_URL = os.environ.get("SONGS_URL", "http://songs:3030/song")

MOCK_PICTURES = [
    {"id": index, "pic_url": f"https://picsum.photos/id/{1000 + index}/800/500",
     "event_city": city, "event_country": "Demo", "event_state": "N/A",
     "event_date": f"2024-0{index}-01"}
    for index, city in enumerate(["Paris", "Tokyo", "New York", "London", "Rome"], 1)
]
MOCK_SONGS = [
    {"id": 1, "title": "Imagine", "artist": "John Lennon", "album": "Imagine", "lyrics": "You may say I'm a dreamer"},
    {"id": 2, "title": "Africa", "artist": "Toto", "album": "Toto IV", "lyrics": "I bless the rains down in Africa"},
]


def _get_json(url, fallback):
    try:
        response = requests.get(url, timeout=2)
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError):
        return fallback


def home(request):
    pictures = _get_json(PICTURES_URL, MOCK_PICTURES)
    if isinstance(pictures, dict):
        pictures = pictures.get("pictures", pictures.get("data", []))
    return render(request, "portal/home.html", {"pictures": pictures[:6]})


def photos(request):
    pictures = _get_json(PICTURES_URL, MOCK_PICTURES)
    if isinstance(pictures, dict):
        pictures = pictures.get("pictures", pictures.get("data", []))
    return render(request, "portal/photos.html", {"pictures": pictures})


def songs(request):
    songs_data = _get_json(SONGS_URL, {"songs": MOCK_SONGS})
    if isinstance(songs_data, dict):
        songs_data = songs_data.get("songs", [])
    return render(request, "portal/songs.html", {"songs": songs_data})
