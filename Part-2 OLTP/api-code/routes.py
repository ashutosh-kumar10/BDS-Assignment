from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from model import Spotify, SpotifyUpdate

router = APIRouter()

# fetch all records from MongoDB
@router.get("/", response_description="List all music", response_model=List[Spotify])
def list_music(request: Request):
    music = list(request.app.database["spotify"].find(limit=100))
    return music

# create a new record in MongoDB
@router.post("/", response_description="Create a new music", status_code=status.HTTP_201_CREATED, response_model=Spotify)
def create_music(request: Request, spotify: Spotify = Body(...)):
    spotify = jsonable_encoder(spotify)
    new_music = request.app.database["spotify"].insert_one(spotify)
    created_music = request.app.database["spotify"].find_one(
        {"_id": new_music.inserted_id}
    )

    return created_music

# fetch a single record from MongoDB
@router.get("/{id}", response_description="Get a single music by id", response_model=Spotify)
def find_music(id: str, request: Request):
    spotify = request.app.database["spotify"].find_one({"track_id": id})
    if spotify is not None:
        return spotify
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Music with ID {id} not found")

# Update a single record in MongoDB
@router.put("/{id}", response_description="Update a music", response_model=Spotify)
def update_music(id: str, request: Request, spotify: SpotifyUpdate = Body(...)):
    book = {k: v for k, v in book.dict().items() if v is not None}
    if len(spotify) >= 1:
        update_result = request.app.database["spotify"].update_one(
            {"_id": id}, {"$set": book}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Music with ID {id} not found")
  
        existing_book = request.app.database["spotify"].find_one({"track_id": id})
        if (existing_book) is not None:
            return existing_book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")

# Delete a single record from MongoDB
@router.delete("/{id}", response_description="Delete a music")
def delete_music(id: str, request: Request, response: Response):
    delete_result = request.app.database["spotify"].delete_one({"track_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Music with ID {id} not found")
