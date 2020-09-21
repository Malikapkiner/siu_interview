from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float,DateTime, Time
from sqlalchemy.orm import relationship

from database import Base

#This class created for database model classes.

#City table for events and users city.
class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, index=True)
    city_name = Column(String)
    
    #Relations 
    user_city = relationship('User',back_populates='city_user')
    district = relationship('District',back_populates='city')

#User class for user table.
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True)
    hashed_password = Column(String)
    star = Column(Float, default=True)
    about = Column(String)
    city_id = Column(Integer, ForeignKey("cities.id"))

    #Relations
    city_user = relationship("City", back_populates="user_city")
    user_event = relationship("Event", back_populates='event_user')
    user_comment = relationship('Comment', back_populates='user')
    user_participant = relationship('Participant', back_populates='participant_user')

#District class for district table.
class District(Base):
    __tablename__= 'districts'
    id = Column(Integer, primary_key=True, index=True)
    district_name=Column(String)
    city_id= Column(Integer, ForeignKey("cities.id"))

    #Relations
    district_event=relationship('Event', back_populates='event_district')
    city = relationship('City',back_populates='district')

#Event class for events
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

    #Relations
    lang_event=relationship('EventLanguage', back_populates='event_lang')
    event_district = relationship('District', back_populates='district_event')
    event_category= relationship('Category', back_populates='category_event')
    location = relationship('Coordinate', back_populates='event_location')
    dates = relationship("EventDate", back_populates="evnt")
    event_user = relationship('User', back_populates='user_event')
    event_comment=relationship('Comment', back_populates='comment_for_event')
    event_image = relationship('EventImage', back_populates='image_event')

#Category class for event categories.
class Category(Base):
    __tablename__='categories'
    id = Column(Integer, primary_key=True, index=True)
    category_name=Column(String)

    #Relations
    category_event=relationship('Event', back_populates='event_category')

#Coordinate class for event locations.
class Coordinate(Base):
    __tablename__='coordinates'
    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    event_id = Column(Integer, ForeignKey('events.id'))
    
    #Relations
    event_location= relationship('Event', back_populates='location')

class EventDate(Base):
    __tablename__='eventDates'
    id = Column(Integer, primary_key=True, index=True)
    date_of_event= Column(DateTime)
    event_id = Column(Integer, ForeignKey('events.id'))

    #Relations
    evnt= relationship('Event',back_populates='dates')
    participants = relationship('Participant', back_populates='participant_event')


#Language class for events language
class Language(Base):
    __tablename__='languages'
    id = Column(Integer, primary_key=True, index=True)
    lang = Column(String)
    langu = relationship('EventLanguage', back_populates='lang')

#TODO: Give this class better name and make it better.
#This class is a side table for many-to-many relationship between language and event
class EventLanguage(Base):
    __tablename__='eventlanguages'
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    language_id = Column(Integer, ForeignKey('languages.id'))

    #Relations
    event_lang= relationship('Event', back_populates='lang_event')
    lang= relationship('Language', back_populates='langu')

#Comment class for event comments.
class Comment(Base):
    __tablename__='comments'
    id = Column(Integer, primary_key=True, index=True)
    star_given = Column(Float)
    event_comment = Column(String)
    event_id = Column(Integer, ForeignKey('events.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    #Relations
    comment_for_event = relationship('Event', back_populates='event_comment')
    user= relationship('User', back_populates='user_comment')

#Images for Events one-to many relationship
class EventImage(Base):
    __tablename__='eventImages'
    id = Column(Integer, primary_key=True, index=True)
    image_path= Column(String)
    event_id= Column(Integer, ForeignKey('events.id'))

    #Relations
    image_event = relationship('Event', back_populates='event_image')

class Participant(Base):
    __tablename__='participants'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    event_date_id = Column(Integer, ForeignKey("eventDates.id"))

    participant_event= relationship('EventDate', back_populates='participants')
    participant_user = relationship('User', back_populates='user_participant')
