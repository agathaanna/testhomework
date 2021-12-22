import os
import uvicorn
import psycopg2
from dotenv import load_dotenv
from datetime import date
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.shipments.shipments import Shipments

origins = [
    "http://localhost:8080"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
load_dotenv()

conn = psycopg2.connect(dbname=os.getenv('DB_NAME'), user=os.getenv('DB_USERNAME'), password=os.getenv('DB_PASSWORD'),
                        port=os.getenv('DB_PORT'), host=os.getenv('DB_HOST'))


@app.get("/shipment")
def get_shipments(start_date,
                  end_date):
    return Shipments(conn).get_shipments(start_date, end_date)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3000, log_level="info")
