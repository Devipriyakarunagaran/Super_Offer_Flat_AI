from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from scraper.run_scraper import get_all_offers
from database import engine
from models import Base

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# HEALTH CHECK
@app.get("/")
def home():
    return {"message": "Backend Running 🚀"}

# SCRAPE + STORE INTO DB
@app.get("/scrape")
def scrape():
    data = get_all_offers()
    return {
        "message": "Scraping completed",
        "count": len(data)
    }

# GET ALL OFFERS FROM DB
@app.get("/offers")
def offers():
    from database import SessionLocal
    from models import Offer

    db = SessionLocal()
    results = db.query(Offer).all()
    db.close()

    return results

# COMPARE PRODUCTS
@app.get("/compare/{product}")
def compare(product: str):

    from database import SessionLocal
    from models import Offer

    db = SessionLocal()

    results = db.query(Offer).filter(
        Offer.product.ilike(f"%{product}%")
    ).all()

    db.close()

    return results
