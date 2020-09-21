from typing import List, Optional
import datetime
from pydantic import BaseModel

class CityBase(BaseModel):
    city_name: str


class CityCreate(CityBase):
    pass


class City(CityBase):
    id: int


    class Config:
        orm_mode = True

class DistrictBase(BaseModel):
    district_name: str

class DistrictCreate(DistrictBase):
    pass


class District(DistrictBase):
    id: int
    city_id: int
    city: City

    class Config:
        orm_mode = True




class UserBase(BaseModel):
    user_name: str
    star: float
    about: str
    city_id: int



class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    city_user: City

    class Config:
        orm_mode = True

class ParticipantBase(BaseModel):
    event_date_id: int
    user_id: int

class ParticipantCreate(ParticipantBase):
    pass

class Participant(ParticipantBase):
    id: int
    participant_user: User

    class Config:
        orm_mode = True

class EventDateBase(BaseModel):
    date_of_event: datetime.datetime
    event_id: int


class EventDateCreate(EventDateBase):
    pass

class EventDate(EventDateBase):
    id: int
    participants: List[Participant] = []

    class Config:
        orm_mode = True
        
class CoordinateBase(BaseModel):
    latitude: float
    longitude: float

    event_id: int


class CoordinateCreate(CoordinateBase):
    pass

class Coordinate(CoordinateBase):
    id: int

    class Config:
        orm_mode = True




class EventImageBase(BaseModel):
    image_path : str
    event_id: int


class EventImageCreate(EventImageBase):
    pass

class EventImage(EventImageBase):
    id: int

    class Config:
        orm_mode = True

class CategoryBase(BaseModel):
    category_name: str


class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True




class LanguageBase(BaseModel):
    lang: str

class LanguageCreate(LanguageBase):
    pass

class Language(LanguageBase):
    id: int
    class Config:
        orm_mode = True

class EventLanguageBase(BaseModel):
    event_id: int
    language_id:int

class EventLanguageCreate(EventLanguageBase):
    pass

class EventLanguage(EventLanguageBase):
    id: int
    lang: Language
    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    star_given: float
    event_comment: str
    event_id: int
    user_id: int

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    user: User
    class Config:
        orm_mode = True




class EventBase(BaseModel):
    title: str
    description: str
    duration : int
    stuffs : str
    important_info : str
    price : float
    user_id: int
    district_id : int
    category_id: int
    event_district: District
    event_category: Category



class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    event_image: List[EventImage] = []
    event_user: User
    location: List[Coordinate] = []
    dates : List[EventDate] = []
    lang_event: List[EventLanguage] = []
    event_comment: List[Comment] = []


    class Config:
        orm_mode = True

