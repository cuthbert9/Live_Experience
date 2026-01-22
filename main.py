from fastapi import FastAPI,Depends
from database import SessionLocal, engine  
from fastapi.middleware.cors import CORSMiddleware
import database_model
import models
from sqlalchemy.orm import session




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# database_model.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()     




@app.get("/")
def test():
    return {"message": "API is working"}

@app.get("/events")
def get_events(db:session=Depends(get_db)):
    events=db.query(database_model.Event).all()
    return events

@app.post("/events")
def create_event(event:models.EventCreate,db:session=Depends(get_db)):
    db_event=database_model.Event(
       title=event.title,
       description=event.description,
       genre=event.genre,
       venue_id=event.venue_id,
       organizer_id=event.organizer_id,
       date=event.date,
       start_time=event.start_time,
       end_time=event.end_time,
       door_time=event.door_time,
       age_restriction=event.age_restriction,
       is_free_event=event.is_free_event,
       ticket_tiers=event.ticket_tiers,
       poster_image=event.poster_image,
       artist_name=event.artist_name,
       artist_bio=event.artist_bio,
       social_links=event.social_links            


    )
    db.add(db_event)  
    db.commit()  
    db.refresh(db_event)
    return db_event  


@app.get("/venues")     
def get_venues(db:session=Depends(get_db)):
    venues=db.query(database_model.Venue).all()
    return venues   

