from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router



app = FastAPI()





@app.on_event("startup")
def statup_db_client():
    app.mongodb_client = MongoClient("mongodb+srv://Luis:h0TtsxwuhRMXVSmo@clustertest.ilqkbh5.mongodb.net/?retryWrites=true&w=majority")
    app.database = app.mongodb_client["test_mongo"]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(router, tags=["people"],prefix="/people")