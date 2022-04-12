from crypt import methods
import os
from unicodedata import category

from flask import Flask, request
from utils.profile import profile
from utils.insert import insert
from utils.update import update
from utils.delete import delete

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

@app.route("/user/profile", methods=['GET'])
def show_profile():
    """ profile user API

    Typical Usage:
    curl -X GET "https://internpractice-hivq6xk2fq-de.a.run.app/user/profile?user_id=<id>"
    
    """
    user_id = request.args.get('user_id')
    result = profile(user_id)
    return result

@app.route("/user/insert", methods=['POST'])
def run_insert():
    """ insert user API

    Typical Usage:
    curl -X POST "https://internpractice-hivq6xk2fq-de.a.run.app/user/insert?name=<name>&age=<age>&category=<category>" \
    -H "Content-Length: 0"
    
    """
    name = request.args.get('name')
    age = request.args.get('age')
    category = request.args.get('category')
    result = insert(name, age, category)
    return result

@app.route("/user/update", methods=['PUT'])
def run_update():
    """ update user API

    Typical Usage:
    curl -X PUT "https://internpractice-hivq6xk2fq-de.a.run.app/user/update?name=<name>&age=<age>&category=<category>" \
    -H "Content-Length: 0"
    
    """
    name = request.args.get('name')
    age = request.args.get('age')
    category = request.args.get('category')
    result = update(name, age, category)
    return result

@app.route("/user/delete", methods=['DELETE'])
def run_delete():
    """ delete user API

    Typical Usage:
    curl -X DELETE "https://internpractice-hivq6xk2fq-de.a.run.app/user/delete?user_id=<id>"
    
    """
    user_id = request.args.get('user_id')
    result = delete(user_id)
    return result

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))