from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Time, Float, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship

Base = declarative_base()



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, unique=True)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="user")  # user, organizer, admin
    created_at = Column(String)

    events = relationship("Event", back_populates="organizer")
    reviews = relationship("Review", back_populates="user")




class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    location_name = Column(String)   # Masaki, Mikocheni, etc
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    cover_image = Column(String)

    owner_id = Column(Integer, ForeignKey("users.id"))

    events = relationship("Event", back_populates="venue")




class Artist(Base):
    __tablename__ = 'artists'
 
    id = Column(Integer, primary_key=True, index=True)
    stage_name = Column(String, nullable=False)
    real_name = Column(String)
    genre = Column(String)
    bio = Column(Text)
    profile_image = Column(String)




class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)

    event_date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)

    entry_fee = Column(Float)
    music_type = Column(String)  # Live Band, DJ, Jazz, Acoustic
    poster_image = Column(String)

    status = Column(String, default="pending")  # pending, approved, rejected

    venue_id = Column(Integer, ForeignKey("venues.id"))
    organizer_id = Column(Integer, ForeignKey("users.id"))

    venue = relationship("Venue", back_populates="events")
    organizer = relationship("User", back_populates="events")
    artists = relationship("EventArtist", back_populates="event")
    reviews = relationship("Review", back_populates="event")



class EventArtist(Base):
    __tablename__ = 'event_artists'

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    artist_id = Column(Integer, ForeignKey("artists.id"))

    event = relationship("Event", back_populates="artists")



class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer)  
    comment = Column(Text)

    user_id = Column(Integer, ForeignKey("users.id"))
    event_id = Column(Integer, ForeignKey("events.id"))

    user = relationship("User", back_populates="reviews")
    event = relationship("Event", back_populates="reviews")
