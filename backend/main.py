from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

MOCK_DATA = {
    "milk": [
        {
            "store": "Aldi",
            "product": "Milk",
            "price": 1.20
        },
        {
            "store": "Lidl",
            "product": "Milk",
            "price": 1.10
        }
    ],
    "bread": [
        {
            "store": "Aldi",
            "product": "Bread",
            "price": 2.50
        },
        {
            "store": "Lidl",
            "product": "Bread",
            "price": 2.10
        }
    ]
}

@app.get("/")
def home():
    return {"message": "Backend Running"}

@app.get("/compare/{product}")
def compare(product: str):
    return MOCK_DATA.get(product, [])
