from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Time, Float, Boolean, ForeignKey, Text,JSON
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
    __tablename__ = "venues"

    id = Column(Integer, primary_key=True, index=True)

    # Basic info
    name = Column(String, nullable=False)
    type = Column(String)  # e.g. Jazz Club, Bar, Arena
    description = Column(Text)

    address = Column(String)
    phone = Column(String)
    website = Column(String)

    latitude = Column(Float)
    longitude = Column(Float)

    # Ratings (aggregated, not individual reviews)
    rating = Column(Float, default=0)
    reviews_count = Column(Integer, default=0)

    # Structured / flexible data
    hours = Column(JSON)        # {"Mon-Thu": "7PM - 12AM", ...}
    amenities = Column(JSON)    # ["Full Bar", "Food Menu", ...]
    images = Column(JSON)       # ["url1", "url2", ...]

    capacity = Column(Integer)

    owner_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    events = relationship("Event", back_populates="venue")




class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, index=True)

    # Basic identity
    name = Column(String, nullable=False)
    genre = Column(String)

    # Popularity
    followers = Column(String)  # e.g. "125K"

    # Descriptions
    bio = Column(Text)
    long_bio = Column(Text)

    # Images
    image = Column(String)
    cover_image = Column(String)

    # Structured data
    social_links = Column(JSON)
    stats = Column(JSON)






class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    genre = Column(String)  # e.g., jazz, rock, pop
    venue_id = Column(Integer, ForeignKey("venues.id"))
    organizer_id = Column(Integer, ForeignKey("users.id"))

    date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)
    door_time = Column(Time)

    age_restriction = Column(String)  # e.g., "21+"
    is_free_event = Column(Boolean, default=False)
    ticket_tiers = Column(JSON)  # stores list of ticket tiers as JSON

    poster_image = Column(String)

    artist_name = Column(String)
    artist_bio = Column(Text)
    social_links = Column(JSON)  # stores website, instagram, spotify, etc.

    is_published = Column(Boolean, default=False)

    # Relationships
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


    # in this platform artists can know where they are taged as perfomers ,somehow can solve fraud 
    # users also can their favourate artists schedule through the year 
    # users will know the venue history of hosting certain artists and future events 
    # maybe in the futire i could add a feature where artists can claim their profile and manage it
    # also venue can claim their profile and manage it
    # this will increase the platform credibility
    # also i could add a feature where users can follow artists and venues to get notified about new events
    # this will increase user engagement on the platform
    # also mybe in the future i could add wide category of events not just music events maybe art exhibitions , theater plays , comedy shows ,educaitonal etc
    
    
