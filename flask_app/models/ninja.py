
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, be sure to install flask-bcrypt: pipenv install flask-bcrypt


class Ninja:
    db = "dojos_and_ninjas" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added her for class association?



    # Create Users Models
    
    @classmethod
    def create_ninja(cls, data):
        query = """
        INSERT INTO ninjas (dojo_id, first_name, last_name, age)
        VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s)
        ;
        """

        return connectToMySQL(cls.db).query_db(query,data)


    # Read Users Models
    # @classmethod
    # def get_all_dojos(cls):
    #     query = """
    #     SELECT * FROM dojos;
    #     """
    #     results = connectToMySQL(cls.db).query_db(query)
    #     all_dojos = []
    #     for dojo in results:
    #         all_dojos.append(cls(dojo))
    #         print (dojo)
    #     return all_dojos
        
    # @classmethod
    # def get_one_dojo(cls, dojo_id):
    #     query = """
    #     SELECT * FROM dojos
    #     WHERE id = %(id)s;
    #     """
    #     data = {'id': dojo_id}
    #     result = connectToMySQL(cls.db).query_db(query,data)
    #     return cls(result[0])


    # Update Users Models



    # Delete Users Models

