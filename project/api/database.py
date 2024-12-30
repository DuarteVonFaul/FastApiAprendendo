from sqlalchemy import create_engine
from sqlalchemy.orm import Session 

from api.models import table_registry




class DataBase():

    def __init__(self, connection='sqlite:///database.db'):
        self.engine = create_engine(connection)
        
        pass

    def mySession(self):
        if(not self.mySession):
            self.mySession = Session(self.engine)
        return self.mySession
    
    def migration(self):
        table_registry.metadata.create_all(self.engine)



database = DataBase()