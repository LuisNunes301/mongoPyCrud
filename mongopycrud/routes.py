from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import People,PeopleUpdate

router = APIRouter()

#post people
@router.post("/", response_description="Create people",status_code=status.HTTP_201_CREATED,response_model=People)
def create_people(request: Request, people: People = Body(...)):
    people = jsonable_encoder(people)
    new_people = request.app.database["people"].insert_one(people)
    create_people = request.app.database["people"].ficnd_one(
        {"_id": new_people.inserted_id}
    )
    return create_people

#get /people
@router.get("/", response_description="List all people",response_model=List[(People)])
def list_people(request: Request):
    people = list(request.app.database["people"].find(limit=100))
    return people

#get /people/{id}
@router.get("/{id}",response_description="Get people by Id",response_model=People)
def find_people(id: str,request: Request):
    if(people := request.app.database["people"].find_one({"_id": id})) is not None:
        return people
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"People with ID {id} not found")

#put book/{id}
@router.put("/{id}", response_description="Update people", response_model=People)
def update_people(id: str,request: Request, people: PeopleUpdate = Body(...)):
    people = {k: v for k, v in people.dict().items() if v is not None}
    if len(people) >= 1:
        update_result = request.app.database["people"].update_one(
            {"_id": id},{"$set": people}
        )
        if update_result.modifed_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"People with Id {id} not found")
    if(
        existing_people := request.app.database["people"].find_one({"_id": id})
    ) is not None:
        return existing_people
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"People with Id {id} not found")

#delete book/{id}
@router.delete("/{id}", response_description="Delete a people")
def delete_people(id: str, request: Request, response: Response):
    delete_result = request.app.database["people"].delete_one({"_id": id})

    if delete_result.delete_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"People with Id {id} not found")