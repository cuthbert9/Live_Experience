from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import date, time
from enums import UserRoleEnum,VenuetypeEnum,GenreEnum
from uuid import UUID



class UserBase(BaseModel):
    full_name: str
    email: str
    phone: Optional[str] 
    role: UserRoleEnum=UserRoleEnum.USER
    following_artists: Optional[List[UUID]] = None
    following_venues: Optional[List[UUID]] = None


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: UUID

    class Config:
        from_attributes = True



class VenueBase(BaseModel):
    name: str
    type: VenuetypeEnum=VenuetypeEnum.HALL
    description: Optional[str] 

    address: Optional[str] 
    phone: Optional[str] 
    website: Optional[str] =None

    latitude: Optional[float] = None
    longitude: Optional[float] = None

    hours: Optional[Dict[str, Any]] = None
    amenities: Optional[List[Any]] = None
    images: Optional[List[str]] = None

    capacity: Optional[int] = None
    venue_followers: Optional[List[UUID]] = None


class VenueCreate(VenueBase):
    owner_id: Optional[UUID] = None


class VenueResponse(VenueBase):
    id: UUID
    rating: float
    reviews_count: int

    class Config:
        from_attributes = True


class ArtistBase(BaseModel):
    name: str
    genre: Optional [List[str]] = None
    followers_count: Optional[str] = None

    bio: Optional[str] = None
    long_bio: Optional[str] = None

    images: Optional[List[str]] = None
    cover_image: Optional[str] = None

    social_links: Optional[Dict[str, Any]] = None
    stats: Optional[Dict[str, Any]] = None
    followers: Optional[List[UUID]] = None


class ArtistCreate(ArtistBase):
    pass


class ArtistResponse(ArtistBase):
    id: UUID

    class Config:
        from_attributes = True


class EventBase(BaseModel):
    title: str
    description: Optional[str] = None
    genre: Optional[List[str]] = None

    venue_id: UUID
    organizer_id: UUID

    date: date
    start_time: time
    end_time: time
    door_time: time

    age_restriction: Optional[str] 
    is_free_event: bool = True

    ticket_tiers: Optional[List[Dict[str, Any]]] = None

    poster_image: Optional[str] 

    artist_name: str 
    artist_bio: Optional[str]
    social_links: Optional[Dict[str, str]] 


class EventCreate(EventBase):
    pass


class EventResponse(EventBase):
    id: UUID
    is_published: bool

    class Config:
        from_attributes = True




class ReviewBase(BaseModel):
    rating: int
    comment: Optional[str] = None


class ReviewCreate(ReviewBase):
    event_id: UUID


class ReviewResponse(ReviewBase):
    id: UUID
    user_id: UUID
    event_id: UUID

    class Config:
        from_attributes = True
