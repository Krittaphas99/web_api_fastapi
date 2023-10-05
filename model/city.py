from sqlalchemy import Table ,Column
from sqlalchemy.sql.sqltypes import Boolean,Integer,String,CHAR
from config.db import Base



class City(Base):
    __tablename__ = 'city'
    ID = Column(Integer,primary_key=True,index=True,autoincrement=True)
    Name = Column(String(65),unique=True)
    CountryCode = Column(String(3))
    District = Column(String(50),unique=True)
    Population = Column(Integer)
    
    def __init__(self,Names,CountryCodes,Districts,Populations):
        self.Name = Names
        self.CountryCode = CountryCodes
        self.District = Districts
        self.Population = Populations

