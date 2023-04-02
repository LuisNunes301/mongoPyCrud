import uuid ## universally unique identifier
from typing import Optional
from pydantic import BaseModel, Field


class People(BaseModel):
    id: str = Field(default_factory=uuid, alis="_id")
    name: str = Field(...) 
    location: str = Field(...)
    founded: int = Field(ge=1440)

    class Config:
        schema_extra = {
            "example":{
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name" : "Luis Nunes",
                "location": "...",
                "founded": 2002
            }
        }

class PeopleUpdate(BaseModel):
    name: Optional[str]
    location: Optional[str]
    founded: Optional[int]

    class Config:
        schema_extra = {
            "example":{
                "name" : "Luis Nunes",
                "location": "BR",
                "founded": 2002
            } 
        }