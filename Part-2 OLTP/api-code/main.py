# imports
from fastapi import FastAPI
from pymongo import MongoClient
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from routes import router as spotify_router
import csv

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient('mongodb+srv://<username>:<password>@cluster0.m6hscve.mongodb.net/?retryWrites=true&w=majority')
    app.database = app.mongodb_client['spotify']
    print("Connected to the MongoDB database!")
    
    #only needed when to insert the data
    with open('train-data.csv', 'r', encoding="utf8") as csvfile:
        header = ['track_id', 'artists', 'album_name', 'track_name', 'popularity', 'duration_ms', 'explicit', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature', 'track_genre']
        reader = csv.reader(csvfile)
        next(reader, None) # skip the headers

        for row in reader:
            doc={}
            for n in range(0,len(header)):
                doc[header[n]] = row[n]
            app.database['spotify'].insert_one(doc)
            print('record inserted')

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

# registering the API endpoints
app.include_router(spotify_router, tags=["Spotify"], prefix="/spotify")
