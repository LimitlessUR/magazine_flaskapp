from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Magazine:
    db_name = 'magazines'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.title = db_data['title']
        self.description = db_data['description']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']


    @classmethod
    def save(cls,data):
        query = "INSERT INTO magazines (title, description, user_id) VALUES (%(title)s,%(description)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM magazines;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_magazines = []
        for row in results:
            all_magazines.append( cls(row) )
        return all_magazines
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM magazines WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @staticmethod
    def validate_magazine(magazine):
        is_valid = True
        if len(magazine['title']) < 3:
            is_valid = False
            flash("Title must be at least 3 characters","magazine")
        if len(magazine['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters","magazine")
        return is_valid