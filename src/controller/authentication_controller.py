from flask import request, make_response
from db.execution import execute
from src.helpers.utils import validate_request_data
from src.schemas import schema

def login_user():
    try:
        user_details = request.get_json()
        if"id" in user_details and type(user_details['id']) is int and user_details['id']>0:
            result = execute(f"SELECT name from users WHERE id ='{user_details['id']}';")
            if result:
                return make_response("log in success", 200)
            else:
                return make_response("no data with this id", 1000)
        else: raise Exception("id is required to log in")
    except Exception as e:
        return make_response("something went wrong" + e.__str__(), 1000)

def register_user():
    try:
        user_details = request.get_json()
        validate_request_data(schema.register_schema, user_details)
        execute(f"INSERT INTO users(id,name,type) VALUES ({user_details['id']},'{user_details['name']}','{user_details['type']}');")
        result = execute(f"SELECT id from users WHERE name = '{user_details['name']}';")
        if result:
            return make_response(str(result[0]['id']), 200)
        else:
            return make_response("something went wrong in the registration", 1000)
    except Exception as e:
        return make_response("something went wrong"+e.__str__(), 1000)
