from flask import request, make_response, render_template
from db.execution import execute

def login_user():
    try:
        id = request.form.get("id")
        if id and int(id)>0:
            result = execute(f"SELECT name from users WHERE id ={id};")
            if result:
                return make_response("log in success", 200)
            else:
                return make_response("no data with this id", 1000)
        else: raise Exception("id is required to log in")
    except Exception as e:
        return make_response("something went wrong" + e.__str__(), 1000)

def register_user():
    try:
        id = request.form.get("id")
        name = request.form.get("name")
        type = request.form.get("type")
        if id and int(id)>0 and name.isalpha() and name and type and type.isalpha():
            execute(f"INSERT INTO users(id,name,type) VALUES ({id},'{name}','{type}');")
            result = execute(f"SELECT id from users WHERE name = '{name}';")
            if result:
                return make_response(str(result[0]['id']), 200)
            else:
                return make_response("something went wrong in the registration", 1000)
        else: raise Exception("id and name and type are required")
    except Exception as e:
        return make_response("something went wrong"+e.__str__(), 1000)
def render_login():
    return render_template("login.html")
def render_hello():
    return render_template("index.html")
def render_register():
    return render_template("register.html")
