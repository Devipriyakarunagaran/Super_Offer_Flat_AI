from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ✅ SWITCH TO POSTGRES (NOT SQLITE)
DATABASE_URL = "postgresql://admin:password@localhost:5432/offersdb"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
