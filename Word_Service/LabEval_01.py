from nameko.rpc import rpc

import dependencies, schemas
import pymysql
class BreweryService:
    # ==========================================================
    # ---------------------- Service Name ----------------------
    # ==========================================================
    
    name = 'word_pack'

    # ==========================================================
    # ----------------------- Dependency -----------------------
    # ==========================================================

    database = dependencies.Database()

    # ==========================================================
    # ------------------------ Functions -----------------------
    # ==========================================================

    def __init__(self):
        print("Service Constructor")

    @rpc
    def get_all_wordPack(self):
        brewery = self.database.get_all_wordPack()
        self.database.close_connection()
        return schemas.BookSchema(many=True).dump(brewery)
    
    @rpc
    def get_wordpack_by_id(self, id):
        brewery = self.database.get_wordpack_by_id(id)
        self.database.close_connection()
        return schemas.BookSchema().dump(brewery)
    
    @rpc
    def search_wordpack(self, id, review):
        self.database.search_wordpack(id, review)

    def __del__(self):
        print("Service Destructor")