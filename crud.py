from sqlalchemy.orm import Session

import models, schemas

"""
    This class used for basic CRUD operations.
    Create functions in this class was temporary and made for testing the API.
"""

#District creation.
def create_district(db: Session, district: schemas.DistrictCreate, city:int):
    db_district = models.District(**district.dict(), city_id=city)
    db.add(db_district)
    db.commit()
    return db_district

#Coordinate creation.
def create_coordinate(db:Session, coordinate: schemas.CoordinateCreate):
    db_coordinate = models.Coordinate(latitude=coordinate.latitude, longitude= coordinate.longitude, event_id=coordinate.event_id)
    db.add(db_coordinate)
    db.commit()
    db.refresh(db_coordinate)
    return db_coordinate

#Event creation.
def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(title=event.title, description=event.description, user_id=event.user_id, duration=event.duration, stuffs=event.stuffs, important_info=event.important_info, price= event.price, district_id=event.district_id, category_id=event.category_id)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    #db_coordinate=models.Event.location(latitude= event.location.latitude, longitude=event.location.longitude, event_id=event.id)
    return db_event

#Category creation.
def create_category(db:Session, category: schemas.CategoryCreate):
    db_category= models.Category(category_name=category.category_name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

#City creation.
def create_city(db: Session, city: schemas.CityCreate):
    db_city = models.City(city_name=city.city_name)
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

#User creation.
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(user_name=user.user_name, hashed_password= fake_hashed_password, city_id=user.city_id, about=user.about, star=user.star)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#Language creation.
def create_language(db: Session, language: schemas.LanguageCreate):
    db_language = models.Language(lang=language.lang)
    db.add(db_language)
    db.commit()
    db.refresh(db_language)
    return db_language

#Comment creation.
def create_comment(db:Session, comment: schemas.CommentCreate):
    db_comment= models.Comment(star_given= comment.star_given, event_comment= comment.event_comment, event_id= comment.event_id, user_id= comment.user_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

#Language for events creation. Made for side table.
def create_eventlang(db: Session, eventlang: schemas.EventLanguageCreate):
    db_eventlang = models.EventLanguage(event_id=eventlang.event_id, language_id=eventlang.language_id)
    db.add(db_eventlang)
    db.commit()
    db.refresh(db_eventlang)
    return db_eventlang

#Create date for events. TODO: Make this function better.
def add_date_to_event(db: Session, event_date: schemas.EventDateCreate):
    db_event_date = models.EventDate(date_of_event= event_date.date_of_event, event_id=event_date.event_id)
    db.add(db_event_date)
    db.commit()
    db.refresh(db_event_date)
    return db_event_date

#Add images for event.
def add_event_image(db: Session, event_image: schemas.EventImageCreate):
    db_event_image= models.EventImage(image_path=event_image.image_path, event_id=event_image.event_id)
    db.add(db_event_image)
    db.commit()
    db.refresh(db_event_image)
    return db_event_image

#Add participant to event
def participate(db: Session, participant: schemas.ParticipantCreate):
    db_participant = models.Participant(user_id=participant.user_id, event_date_id=participant.event_date_id)
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    return db_participant

#Get functions

def get_event_by_id(db:Session, event: int):
    return db.query(models.Event).filter(models.Event.id == event).first()

def get_city_by_name(db: Session, city: str):
    return db.query(models.City).filter(models.City.city_name == city).first()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()