from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router

config= dotenv_values(".env")

app = FastAPI()
app.include_router(router, tags=["people"],prefix="/people")




@app.on_event("startup")
def statup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

