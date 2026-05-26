from scraper.aldi_scraper import scrape_aldi
from scraper.lidl_scraper import scrape_lidl

from database import SessionLocal
from models import Offer

def get_all_offers():

    db = SessionLocal()

    print("🚀 SCRAPER STARTED")

    aldi = scrape_aldi()
    lidl = scrape_lidl()

    print("ALDI:", aldi)
    print("LIDL:", lidl)

    all_products = aldi + lidl

    # Clear old data (important)
    db.query(Offer).delete()
    db.commit()

    # Insert new data
    for item in all_products:

        offer = Offer(
            product=item["product"],
            store=item["store"],
            price=float(item["price"])
        )

        db.add(offer)

    db.commit()
    db.close()

    return all_products
