from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float,DateTime, Time
from sqlalchemy.orm import relationship

from database import Base


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, index=True)
    city_name = Column(String)
    
    user_city = relationship('User',back_populates='city_user')
    district = relationship('District',back_populates='city')

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True)
    hashed_password = Column(String)
    star = Column(Float, default=True)
    about = Column(String)
    city_id = Column(Integer, ForeignKey("cities.id"))

    city_user = relationship("City", back_populates="user_city")
    user_event = relationship("Event", back_populates='event_user')

class District(Base):
    __tablename__= 'districts'
    id = Column(Integer, primary_key=True, index=True)
    district_name=Column(String)
    city_id= Column(Integer, ForeignKey("cities.id"))

    district_event=relationship('Event', back_populates='event_district')
    city = relationship('City',back_populates='district')

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    duration = Column(Integer)
    stuffs = Column(String)
    important_info = Column(String)
    price = Column(Float)
    district_id= Column(Integer, ForeignKey('districts.id'))
    user_id = Column(Integer, ForeignKey("users.id"))
    category_id= Column(Integer, ForeignKey('categories.id'))

    langevent=relationship('EventLanguage', back_populates='eventlang')
    event_district = relationship('District', back_populates='district_event')
    event_category= relationship('Category', back_populates='category_event')
    location = relationship('Coordinate', back_populates='event_location')
    dates = relationship("EventDate", back_populates="evnt")
    event_user = relationship('User', back_populates='user_event')

class Category(Base):
    __tablename__='categories'
    id = Column(Integer, primary_key=True, index=True)
    category_name=Column(String)

    category_event=relationship('Event', back_populates='event_category')

class Coordinate(Base):
    __tablename__='coordinates'
    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    event_id = Column(Integer, ForeignKey('events.id'))
    
    event_location= relationship('Event', back_populates='location')

class EventDate(Base):
    __tablename__='eventDates'
    id = Column(Integer, primary_key=True, index=True)
    date_of_event= Column(DateTime)
    event_id = Column(Integer, ForeignKey('events.id'))

    evnt= relationship('Event',back_populates='dates')

class Language(Base):
    __tablename__='languages'
    id = Column(Integer, primary_key=True, index=True)
    lang = Column(String)

class EventLanguage(Base):
    __tablename__='eventlanguages'
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    language_id = Column(Integer, ForeignKey('languages.id'))

    eventlang= relationship('Event', back_populates='langevent')