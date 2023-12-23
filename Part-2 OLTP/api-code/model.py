# Model class for Spotify dataset
 
from typing import Optional
from pydantic import BaseModel, Field

class Spotify(BaseModel):
    track_id: str
    artists: str
    album_name: str
    track_name: str
    popularity: float
    duration_ms: int
    explicit: str
    danceability: float
    energy: float
    key: int
    loudness: float
    mode: int
    speechiness: float
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float
    time_signature: int
    track_genre: str


    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "track_id": "track_id",
                "artists": "artists",
                "album_name": "album_name",
                "track_name":"track_name",
                "popularity": 1.2,
                "duration_ms": 1,
                "explicit": "explicit",
                "danceability": 2.3,
                "energy": 1,
                "key": 2,
                "loudness": 3,
                "mode": 2,
                "speechiness": 1,
                "acousticness": 1,
                "instrumentalness": 1,
                "liveness": 1,
                "valence": 1,
                "tempo": 1,
                "time_signature": 1,
                "track_genre": "track_genre"
            }
        }

class SpotifyUpdate(BaseModel):
    track_id: Optional[str]
    artists: Optional[str]
    album_name: Optional[str]
    track_name: Optional[str]
    popularity: Optional[float]
    duration_ms: Optional[int]
    explicit: Optional[str]
    danceability: Optional[float]
    energy: Optional[float]
    key: Optional[int]
    loudness: Optional[float]
    mode: Optional[int]
    speechiness: Optional[float]
    acousticness: Optional[float]
    instrumentalness: Optional[float]
    liveness: Optional[float]
    valence: Optional[float]
    tempo: Optional[float]
    time_signature: Optional[int]
    track_genre: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "track_id": "track_id",
                "artists": "artists",
                "album_name": "album_name",
                "track_name":"track_name",
                "popularity": 1.2,
                "duration_ms": 1,
                "explicit": "explicit",
                "danceability": 2.3,
                "energy": 1,
                "key": 2,
                "loudness": 3,
                "mode": 2,
                "speechiness": 1,
                "acousticness": 1,
                "instrumentalness": 1,
                "liveness": 1,
                "valence": 1,
                "tempo": 1,
                "time_signature": 1,
                "track_genre": "track_genre"
            }
        }
