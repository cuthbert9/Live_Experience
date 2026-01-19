from pydantic import BaseModel
from typing import List, Optional
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
    description: Optional[str] = None
    location_name: Optional[str] = None
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class VenueCreate(VenueBase):
    pass


class VenueResponse(VenueBase):
    id: int

    class Config:
        from_attributes = True




class ArtistBase(BaseModel):
    stage_name: str
    real_name: Optional[str] = None
    genre: Optional[str] = None
    bio: Optional[str] = None


class ArtistCreate(ArtistBase):
    pass


class ArtistResponse(ArtistBase):
    id: int

    class Config:
        from_attributes = True



class EventBase(BaseModel):
    title: str
    description: Optional[str] = None
    event_date: date
    start_time: time
    end_time: Optional[time] = None
    entry_fee: Optional[float] = 0
    music_type: Optional[str] = None
    venue_id: int
    poster_image: Optional[str] = None


class EventCreate(EventBase):
    artist_ids: List[int] = []


class EventResponse(EventBase):
    id: int
    status: str

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
