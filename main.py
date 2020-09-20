from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import models, crud, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/city_add/", response_model=schemas.City)
def create_city(city: schemas.CityCreate, db: Session = Depends(get_db)):
    db_city = crud.get_city_by_name(db, city=city.city_name)
    if db_city:
        raise HTTPException(status_code=400, detail="City already exist")
    return crud.create_city(db=db, city=city)

@app.post("/district_add/{city_id}", response_model=schemas.District)
def create_district(city_id:int, district: schemas.DistrictCreate, db: Session = Depends(get_db)):
    return crud.create_district(db=db,district=district, city=city_id)

@app.post('/user_add/', response_model=schemas.User)
def create_user(user:schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db,user=user)

@app.post('/event_add/', response_model=schemas.Event)
def create_event(event:schemas.EventCreate, db: Session = Depends(get_db)):
    return crud.create_event(db=db,event=event)

@app.post('/coordinate_add/', response_model=schemas.Coordinate)
def create_coordinate(coordinate:schemas.CoordinateCreate, db: Session = Depends(get_db)):
    return crud.create_coordinate(db=db,coordinate=coordinate)
@app.post('/category_add/', response_model=schemas.Category)
def create_categoty(category:schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db,category=category)

@app.post('/language_add/', response_model=schemas.Language)
def create_language(language:schemas.LanguageCreate, db: Session = Depends(get_db)):
    return crud.create_language(db=db,language=language)

@app.post('/eventlang_add/', response_model=schemas.EventLanguage)
def create_language(eventlang:schemas.EventLanguageCreate, db: Session = Depends(get_db)):
    return crud.create_eventlang(db=db,eventlang=eventlang)

@app.post('/event_date_add/', response_model=schemas.EventDate)
def create_event_date(event_date:schemas.EventDateCreate, db: Session = Depends(get_db)):
    return crud.add_date_to_event(db=db,event_date=event_date)
    
@app.post('/comment_add/', response_model=schemas.Comment)
def create_comment(comment:schemas.CommentCreate, db: Session = Depends(get_db)):
    return crud.create_comment(db=db,comment=comment)

@app.get("/events/{event_id}", response_model=schemas.Event)
def read_user(event_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_event_by_id(db, event=event_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
