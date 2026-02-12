from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Time, Float, Boolean, ForeignKey, Text,JSON,Table,Enum as SQLEnum
from sqlalchemy.orm import relationship
from enums import UserRoleEnum,VenuetypeEnum,GenreEnum
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()



class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, unique=True)
    password_hash = Column(String, nullable=False)
    role = Column(SQLEnum(UserRoleEnum,name="user_role_enum"),default=UserRoleEnum.USER ,
                  nullable=False)  # user, organizer, admin
    created_at = Column(String)

    following_artists=relationship("Artist",secondary="user_follow_artist",back_populates="followers")

    following_venues=relationship("Venue",secondary="user_follow_venue",back_populates="venue_followers")

    events = relationship("Event", back_populates="organizer")
    reviews = relationship("Review", back_populates="user")




class Venue(Base):
    __tablename__ = "venues"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Basic info
    name = Column(String, nullable=False)
    type = Column(SQLEnum(VenuetypeEnum ,name="venue_type_enum"),default=VenuetypeEnum.HALL)  # e.g. Jazz Club, Bar, Arena
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

    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    # Relationships
    events = relationship("Event", back_populates="venue")   

    venue_followers=relationship("User",secondary="user_follow_venue",back_populates="following_venues")




class Artist(Base):
    __tablename__ = "artists"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)   
    name = Column(String, nullable=False)
    genre = Column(JSON)  
    followers_count = Column(String)  # e.g. "125K"
    bio = Column(Text)
    long_bio = Column(Text)
    # Images
    images = Column(JSON)
    cover_image = Column(String)
    social_links = Column(JSON)
    stats = Column(JSON)

    followers=relationship("User",secondary ="user_follow_artist" , back_populates="following_artists")





class Event(Base):
    __tablename__ = 'events'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(Text)
    genre = Column(JSON)  # e.g., jazz,CCM , christian/gospel 
    venue_id = Column(UUID(as_uuid=True), ForeignKey("venues.id"))
    organizer_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    date = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)
    door_time = Column(Time)

    age_restriction = Column(String ,default="18")  # e.g., "21+"
    is_free_event = Column(Boolean, default=True)
    ticket_tiers = Column(JSON)  # stores list of ticket tiers as JSON

    poster_image = Column(String,default="https://example.com/default-poster.jpg")

    artist_name = Column(String)
    artist_bio = Column(Text ,default="No bio available")
    social_links = Column(JSON,default=lambda:{"socials":"  "})  # stores website, instagram, spotify, etc.

    is_published = Column(Boolean, default=False)

    # Relationships
    venue = relationship("Venue", back_populates="events")
    organizer = relationship("User", back_populates="events")
    artists = relationship("EventArtist", back_populates="event")
    reviews = relationship("Review", back_populates="event")




class EventArtist(Base):
    __tablename__ = 'event_artists'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    event_id = Column(UUID(as_uuid=True), ForeignKey("events.id"))
    artist_id = Column(UUID(as_uuid=True), ForeignKey("artists.id"))

    event = relationship("Event", back_populates="artists")



class Review(Base):
    __tablename__ = 'reviews'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    rating = Column(Integer)  
    comment = Column(Text)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    event_id = Column(UUID(as_uuid=True), ForeignKey("events.id"))

    user = relationship("User", back_populates="reviews")
    event = relationship("Event", back_populates="reviews")




    # Association tables
    user_follow_artist = Table(
        'user_follow_artist', Base.metadata,
        Column('user_id', UUID(as_uuid=True), ForeignKey('users.id')),
        Column('artist_id', UUID(as_uuid=True), ForeignKey('artists.id'))
    )

    user_follow_venue = Table(
        'user_follow_venue', Base.metadata,
        Column('user_id', UUID(as_uuid=True), ForeignKey('users.id')),
        Column('venue_id', UUID(as_uuid=True), ForeignKey('venues.id'))
    )





    # in this platform artists can know where they are taged as perfomers ,somehow can solve fraud 
    # users also can their favourate artists schedule through the year 
    # users will know the venue history of hosting certain artists and future events 
    # maybe in the futire i could add a feature where artists can claim their profile and manage it
    # also venue can claim their profile and manage it
    # this will increase the platform credibility
    # also i could add a feature where users can follow artists and venues to get notified about new events
    # this will increase user engagement on the platform
    # also mybe in the future i could add wide category of events not just music events maybe art exhibitions , theater plays , comedy shows ,educaitonal etc
    # adding Weddings section for all weddings resources and vendors
    
