from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import date, time


class UserBase(BaseModel):
    full_name: str
    email: str
    phone: Optional[str] = None
    role: Optional[str] = "user"


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True



class VenueBase(BaseModel):
    name: str
    type: Optional[str] = None
    description: Optional[str] = None

    address: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None

    latitude: Optional[float] = None
    longitude: Optional[float] = None

    hours: Optional[Dict[str, Any]] = None
    amenities: Optional[List[Any]] = None
    images: Optional[List[str]] = None

    capacity: Optional[int] = None


class VenueCreate(VenueBase):
    owner_id: Optional[int] = None


class VenueResponse(VenueBase):
    id: int
    rating: float
    reviews_count: int

    class Config:
        from_attributes = True


class ArtistBase(BaseModel):
    name: str
    genre: Optional[str] = None
    followers: Optional[str] = None

    bio: Optional[str] = None
    long_bio: Optional[str] = None

    image: Optional[str] = None
    cover_image: Optional[str] = None

    social_links: Optional[Dict[str, Any]] = None
    stats: Optional[Dict[str, Any]] = None


class ArtistCreate(ArtistBase):
    pass


class ArtistResponse(ArtistBase):
    id: int

    class Config:
        from_attributes = True


class EventBase(BaseModel):
    title: str
    description: Optional[str] = None
    genre: Optional[str] = None

    venue_id: int
    organizer_id: int

    date: Optional[date] = None
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    door_time: Optional[time] = None

    age_restriction: Optional[str] = None
    is_free_event: bool = False

    ticket_tiers: Optional[List[Dict[str, Any]]] = None

    poster_image: Optional[str] = None

    artist_name: Optional[str] = None
    artist_bio: Optional[str] = None
    social_links: Optional[Dict[str, Any]] = None


class EventCreate(EventBase):
    pass


class EventResponse(EventBase):
    id: int
    is_published: bool

    class Config:
        from_attributes = True




class ReviewBase(BaseModel):
    rating: int
    comment: Optional[str] = None


class ReviewCreate(ReviewBase):
    event_id: int


class ReviewResponse(ReviewBase):
    id: int
    user_id: int
    event_id: int

    class Config:
        from_attributes = True
