class Todo:
    def __init__(self, description):
        self.description = description
        self.completed = False
class User:
    def __init__(self, username, mobile_phone):
        self.username = username
        self.mobile_phone = mobile_phone
        self.todos = []

user1 = User("Bach21", "512-826-0001")

todo1 = Todo("Sweep floor")
user1.todos.append(todo1)

user1.todos.append(Todo("Make bed"))

print(user1.todos)
print(user1)