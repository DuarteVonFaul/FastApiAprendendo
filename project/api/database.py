from sqlalchemy import create_engine
from sqlalchemy.orm import Session 

from api.models import table_registry




class DataBase():

    def __init__(self, connection='sqlite:///database.db'):
        self.engine = create_engine(connection)
        self.session = None
        
        pass

    def mySession(self):
        if(not self.session):
            self.session = Session(self.engine)
        return self.session
    
    def migration(self):
        table_registry.metadata.create_all(self.engine)
    
    def drop(self):
        table_registry.metadata.drop_all(self.engine)



database = DataBase()