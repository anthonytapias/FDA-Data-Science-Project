from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, Text, ForeignKey


class Adverse_Events(Base): #association table
    __tablename__ = 'events'
    id = Column(Integer, primary_key = True)
    sex = Column(Integer) #should we do int or text here?
    weight = Column(Integer)
    age = Column(Integer)


    manufacturers = relationship('Manufacturers', back_populates='events')
    manufacturer_id = Column(Integer, ForeignKey('manufacturers_id'))

    brands = relationship('Brands', back_populates='events')
    brand_id = Column(Integer, ForeignKey('brands_id'))

    reactions = relationship('Reactions', back_populates='events')
    reactions_id = Column(Integer, ForeignKey('reactions_id'))



class Brands(Base): # many brand-drugs are associated with many manufacturers through adverse events
    __tablename__ = 'brands'
    id = Column(Integer, primary_key = True)
    events = relationship('Events', back_populates='brands') #many:many
    name = Column(Text)
    manufacturers = relationship('Manufacturers', secondary='events', back_populates('brands')) # many:many through association table


class Manufacturers(Base): # many manufacturers are associated with many drugs through adverse events
    __tablename__ = 'manufacturers'
    id = Column(Integer, primary_key = True)
    name =
    events_id = Column(Integer)
    brand_id = Column(Integer)


class Holidays(Base): # one holiday to many adverse events
    __tablename__ = 'holidays'
    id = Column(Integer, primary_key = True)
    name = Column(Text)
    date = Column(Text) #text? YYYY-MM-DD?
    events_id = Column(Integer)


class Reactions(Base): #many reactions from 1 or more drugs through an adverse event
    __tablename__ = 'reactions'
    id = Column(Integer, primary_key = True)
    events_id = Column(Integer)
    manufacturers =
    manufacturers_id = Column(Integer)
    brands =
    brand_id = Column(Integer)
