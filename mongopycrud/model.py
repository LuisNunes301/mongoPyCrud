from typing import Optional
from pydantic import BaseModel, Field


class People(BaseModel):
    name: str
    location: Optional[str] =None
    founded: int = Field(ge=1440)

    class Config:
        schema_extra = {
            "example":{
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name" : "Luis Nunes",
                "location": "BR",
                "founded": 2002
            }
        }
