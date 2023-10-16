from fastapi import APIRouter,HTTPException,status,Body
from config.db import db_dependency
from model.city import City
from pydantic import BaseModel
from datetime import datetime, timezone, timedelta
from fastapi.responses import JSONResponse
import random
cityPath = APIRouter()
# Time zone in Thailand UTC+7
tz = timezone(timedelta(hours = 7))
# Create a date object with given timezone
date = datetime.now(tz=tz)

class CityModel(BaseModel):
    ID: int  | None = None
    Name: str | None = None
    CountryCode: str | None = None
    District:  str | None = None
    Population:  int | None = None
    count:  int | None = None



@cityPath.get("/city/{city_id}",status_code=status.HTTP_200_OK)
async def read_data_all(city_id:int,database:db_dependency):
    city = database.query(City).filter(City.ID == city_id).first()
    if city is None:
        raise HTTPException(status_code=404,detail='City not found')
    return {"city":city}


@cityPath.post("/city/create",status_code=status.HTTP_200_OK)
async def creatcity(reqBody:CityModel,database:db_dependency):
    if reqBody.Name != None and reqBody.CountryCode!=None:
        insert = City(Names=reqBody.Name,CountryCodes=reqBody.CountryCode,Districts=reqBody.District,Populations=reqBody.Population)
        database.add(insert)
        database.commit()
    else:
        raise HTTPException(status_code=404,detail='need Name and CountryCode')
    # if city is None:
    #     raise HTTPException(status_code=404,detail='City not found')
    return {"city":insert,"time":date.strftime("%d %m %Y")}

@cityPath.post("/city/genarate",status_code=status.HTTP_200_OK)
async def creatcity(reqBody:CityModel,database:db_dependency):
    list_gen = [] 
    for i in range(reqBody.count):
        insert = City(Names="a"+str(random.randrange(1,100)),CountryCodes="WERQ"+str(random.randrange(1,100)),Districts="city",Populations=random.randrange(1000,100000))
        list_gen.append(insert)
        print(list_gen)
    # database.add(insert)
    # database.commit(list_gen)
    # if city is None:
    #     raise HTTPException(status_code=404,detail='City not found')
    return {"city":list_gen,"time":date.strftime("%d %m %Y")}


@cityPath.get("/city/",status_code=status.HTTP_200_OK)
async def read_data_all(database:db_dependency):
    city = database.query(City).all()
    if city is None:
        raise HTTPException(status_code=404,detail='City not found')
    return city

@cityPath.put("/city/{city_id}",status_code=status.HTTP_200_OK)
async def UpdateCity(city_id:int,reqBody:CityModel,database:db_dependency):
    city = database.query(City).filter(City.ID == city_id).first()
    # city.ID = city_id
    city.Name = reqBody.Name_city
    database.commit()
    database.close()
    if city is None:
        raise HTTPException(status_code=404,detail='City not found')
    return {"city":"finished update"}




 
    