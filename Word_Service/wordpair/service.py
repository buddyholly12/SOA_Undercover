from nameko.rpc import rpc

import dependencies, schemas
import pymysql
class BreweryService:
    # ---------------------- Service Name ----------------------    
    name = 'word_Pair'
    # ----------------------- Dependency -----------------------
    database = dependencies.Database()
    # ------------------------ Functions -----------------------

    def __init__(self):
        print("Service Constructor")

    @rpc
    def get_all_wordPair(self):
        brewery = self.database.get_all_wordPair()
        self.database.close_connection()
        return schemas.BookSchema(many=True).dump(brewery)
    
    @rpc
    def get_wordPair_by_id(self, id,status):
        self.database.get_wordPair_by_id(id, status)
    
    @rpc
    def search_wordPair(self, id, status):
        self.database.search_wordPair(id,status)

    def __del__(self):
        print("Service Destructor")