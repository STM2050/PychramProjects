from flask import Flask, request

app = Flask(__name__)

users = {
    "DanyGoT15": {
        "mobile_phone": "555-555-5555",
        "todos": [
            {"description": "Do laundry",
             "completed": False},
            {
                "description": "Call Saiteria",
                "completed": False
            }
            ,
            {
                "description": "Take out trash",
                "completed": True
            },
            {
                "description": "Wash dishes",
                "completed": True
            }
        ]
    },
    "SG2118": {
        "mobile_phone": "555-555-5556",
        "todos": []
    }
}

@app.route('/test')
def hello():
    print("Hi, the hello() function is being executed")
    return "Hello"

@app.route('/users')
def get_all_users():
    my_users = []
    for key in users:
        user = {
            "username": key,
            "mobile_phone" : users[key]['mobile_phone'],
            "todos": users[key]['todos']
        }
        my_users.append(user)

    return {
        "users": my_users
    }, 200

@app.route("/users/<username>")
def get_user_by_username(username):
    if username in users:
        return {
            "username": username,
            "mobile_phone": users[username]['mobile_phone'],
            "todos": users[username]['todos']
        }
    else:
        return {
            "message": f"User with username {username} does not exist!"
        }, 404
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if data['username'] in users:
        return {
            "message": f"User with username {data['username']} already exists! Cannot create a new user"
        }, 400
    else:
        users[data['username']] = {
            "mobile_phone": data['mobile_phone'],
            "todos": []
        }
        return{
            "username": data['username'],
            "mobile_phone": users[data['username']]['mobile_phone'],
            "todos": users[data['username']]['todos']
        }, 201
@app.route('/users/<username>/todos')
def get_all_todos_by_user(username):
    if username not in users:
        return {
            "message": f"User with username {username} that you are trying to retrive todos from does not exist"
        }, 404
    if request.args.get("completed"):
        if request.args.get("completed") == 'yes':
            completed_todos = []
            for todo in users[username]['todos']:
                if todo['completed']:
                    completed_todos.append(todo)
            return {
                "todos": completed_todos
            }, 200
        elif request.args.get("completed") == 'no':
            uncompleted_todos = []
            for todo in users[username]['todos']:
                if not todo['completed']:
                    uncompleted_todos.append(todo)
            return {
                "todos": uncompleted_todos
            }, 200
    return {
        "todos": users[username]['todos']
    }, 200
@app.route('/users/<username>/todos', methods=['POST'])
def create_todo(username):
    if username not in users:
        return{
            "message": f"User with username {username} that you are trying to add a todo does not exist"
        }, 404
    json = request.get_json()

    if str(json['description']).strip() == '':
        return {
            "message": "Description for todo cannot be blank"
        }, 400
    new_todo = {
        "description": json['description'],
        "completed": False
    }
    users[username]['todos'].append(new_todo)

    return new_todo, 200

app.run(port=5050)