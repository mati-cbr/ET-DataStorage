from contextlib import asynccontextmanager
from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from logging import info

from shared.schemas import BitscopeCollectionSchema, BitscopeRecordSchema
from shared.mongo import client


@asynccontextmanager
async def db_lifespan(app: FastAPI):
    app.mongodb_client = client
    app.database = app.mongodb_client.get_database("data_storage")
    app.bitscope = app.database.get_collection("bitscope")
    ping_response = await app.database.command("ping")
    if int(ping_response["ok"]) != 1:
        raise Exception("Problem z połączeniem do bazy")
    else:
        info("Połączono z bazą")
    
    yield
    await app.mongodb_client.close()


app: FastAPI = FastAPI(title="DataStorage API Gateway", lifespan=db_lifespan, docs_url="/api/docs")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


api = APIRouter(prefix="/api")


@api.get("/records", response_model=BitscopeCollectionSchema)
async def list_records():
    results = await app.bitscope.find().to_list(100)
    if results is not None:
        return (BitscopeCollectionSchema(data=results))
    else:
        raise HTTPException(
            status_code=404, detail="Nie znaleziono rekordów"
        )


@api.post("/records", response_model=BitscopeRecordSchema, status_code=201)
async def create_record(record: BitscopeRecordSchema):
    new_record = record.model_dump(by_alias=True, exclude=["id"])
    result = await app.bitscope.insert_one(new_record)
    new_record["_id"] = result.inserted_id

    return new_record


app.include_router(api)
