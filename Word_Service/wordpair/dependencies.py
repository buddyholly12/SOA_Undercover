from nameko.extensions import DependencyProvider

import pymysqlpool
import pymysql

# ----------------------------------- Database Wrapper -----------------------------------

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        print("DB Wrapper Constructor")
        self.connection = connection
    
    def get_all_wordPair(self):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM word_pairs"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_word_pack': row['id_word_pack'],
                'word_1': row['word_1'],
                'word_2': row['word_2'],
                'Status': row['status'],
                'Created_at': row['created_at'],
                'Updated_at': row['updated_at']
            })
        cursor.close()
        return result
    
    def get_wordPair_by_id(self, id,status):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "UPDATE word_pairs SET status = %s WHERE id = %s"
        cursor.execute(sql, (status, id))
        result = cursor.fetchone()
        cursor.close()
        return result

    def search_wordPair(self, id, status):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "DELETE word_pairs SET status = %s WHERE id = %s"
        cursor.execute(sql, (status, id))
        cursor.close()
        self.connection.commit()

    def close_connection(self):
        self.connection.close()
        
# --------------------------------- Dependency Provider ----------------------------------

class Database(DependencyProvider):

    connection_pool = None

    def __init__(self):
        print("DB Dependency Constructor")
        config={'host':'localhost', 'user':'Word_Service', 'password':'ADMIN123', 'database':'Word_Service', 'autocommit':True}
        self.connection_pool = pymysqlpool.ConnectionPool(size=5, name='DB Pool', **config)
    
    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
    
    def __del__(self):
        print("DB Dependency Destructor")
    
    



