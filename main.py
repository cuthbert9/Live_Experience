from fastapi import FastAPI,Depends
from database import SessionLocal, engine  
from fastapi.middleware.cors import CORSMiddleware
import database_model
import models
from sqlalchemy.orm import session
from security.security import create_token,hash_password,verify_password

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

@app.get("/events/{event_id}")
def get_event_by_Id(event_id:int,db:session=Depends(get_db)):
    event=db.query(database_model.Event).filter(database_model.Event.id==event_id).first()
    return event

@app.get("events")
def get_event_by_genre (event_genre:str , db:session=Depends(get_db)):
    events=db.query(database_model.Event).filter(database_model.Event.genre.contains([event_genre])).all()

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

@app.post("/venues")
def create_venue(venue:models.VenueCreate,db:session=Depends(get_db )):
    db_venue=database_model.Venue(
       name=venue.name,
       address=venue.address,
       city=venue.city,
       state=venue.state,
       zip_code=venue.zip_code,
       capacity=venue.capacity,
       description=venue.description,
       social_links=venue.social_links,
       stats=venue.stats
    )
    db.add(db_venue)  
    db.commit()  
    db.refresh(db_venue)
    return db_venue

@app.get("/venues/{venue_id}")
def get_venue_by_Id(venue_id:int,db:session=Depends(get_db)):
    venue=db.query(database_model.Venue).filter(database_model.Venue.id==venue_id).first()
    return venue



@app.get("/artists")     
def get_artists(db:session=Depends(get_db)):
    artists=db.query(database_model.Artist).all()
    return artists  

@app.get("/artists/{artist_id}")
def get_artist_by_id(artist_id:int,db:session=Depends(get_db)):
    artist=db.query(database_model.Artist).filter(database_model.Artist.id==artist_id).first()
    return artist


@app.post("/artists")
def create_artist(artist:models.ArtistCreate,db:session=Depends(get_db )):
    db_artist=database_model.Artist(
       name=artist.name,
       bio=artist.bio,
       followers=artist.followers,
       genre=artist.genre,
       social_links=artist.social_links,
       stats=artist.stats,
       cover_image=artist.cover_image,
       images=artist.images
       
    )
    db.add(db_artist)  
    db.commit()  
    db.refresh(db_artist)
    return db_artist



@app.get("/users/{user_id}")
def get_user(user_id:int,db:session=Depends(get_db)):
    user=db.query(database_model.User).filter(database_model.User.id==user_id).first()
    return user


@app.post("/register")
def register_user(user:models.UserCreate,db:session=Depends(get_db)):

    db_user=database_model.User(
        full_name=user.full_name,
        email=user.email,
        password_hash=user.password_hash
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/login")
def login(email:str ,password:str ,db:session=Depends(get_db)):
    user=db.query(database_model.User).filter(database_model.User.email==email).first()
    if user and user.password_hash==password:
        return {"message":"Login successful"}
    else:
        return {"message":"Invalid credentials"}    