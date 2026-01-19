from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url='postgresql://neondb_owner:npg_aZTJ1RGjM2my@ep-silent-fog-ahg7dwdb-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
engine=create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 