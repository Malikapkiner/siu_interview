from typing import List, Optional
import datetime
from pydantic import BaseModel


class DistrictBase(BaseModel):
    district_name: str

class DistrictCreate(DistrictBase):
    pass


class District(DistrictBase):
    id: int
    city_id: int

    class Config:
        orm_mode = True

class CityBase(BaseModel):
    city_name: str


class CityCreate(CityBase):
    pass


class City(CityBase):
    id: int
    #user_city = List[District]= []
    #district = List[District]= []

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

class EventDateBase(BaseModel):
    date_of_event: datetime.datetime
    event_id: int


class EventDateCreate(EventDateBase):
    pass

class EventDate(EventDateBase):
    id: int

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

class CategoryBase(BaseModel):
    category_name: str


class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
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
    event_user: User
    location: List[Coordinate] = []
    dates : List[EventDate] = []
    langevent: List[EventLanguage] = []

    class Config:
        orm_mode = True

