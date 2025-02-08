#!usr/bin/python3
'''New engine DBStorage'''
import models
import sqlalchemy
from sqlalchemy import create_engine
from models.base_model import Base
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage():
    '''db storage engine'''

    __engine = None
    __session = None

    def __init__(self):
        '''instantiation of engine'''
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'), getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''query on the current database session (self.__session) all
        objects depending of the class name (argument cls)'''
        clsses = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}
        #clsses = ["State", "City", "Amenity", "Place", "Review", "User"]
        dict_new = {}
        for clss in clsses:
            if cls is None or cls is clss:
                instances = self.__session.query(clsses[clss]).all()
                for instance in instances:
                    key = instance.__class__.__name__ + '.' + instance.id
                    dict_new[key] = instance
        return dict_new

    def new(self, obj):
        '''Add the object to the current database session (self.__session)'''
        self.__session.add(obj)

    def save(self):
        '''commit all changes of the current database session '''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete from the current database session obj if not None'''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''create all tables in the database '''
        Base.metadata.create_all(self.__engine)
        session_make = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_make)
        self.__session = Session

    def close(self):
        '''call remove() method on the private session 
        attribute (self.__session)'''
        self.__session.remove()
