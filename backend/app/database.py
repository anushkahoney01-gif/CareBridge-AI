from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# If using PostgreSQL on Render/Railway, force the use of correct async/sync drivers if needed
db_url = settings.DATABASE_URL
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

# Create the persistent database engine
engine = create_engine(db_url)

# Create a sessionmaker factory to generate isolated sessions for requests
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for database models to inherit from
Base = declarative_base()

# Dependency injection middleware utility to safely handle DB sessions per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
