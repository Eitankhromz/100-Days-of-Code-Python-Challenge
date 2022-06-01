class User:

    def __init__(self, user_id, username):
        # print("new user being created...")
        # self is the object itself
        # [object].[attribute_name] = [argument]
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follows(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Elon")

print(user_1.username)

# user_2 = User()
# user_2.id = "002"
# user_2.username = "Jeff"
# instead of ^^^^^
user_2 = User("002", "Jeff")

user_2.follows(user_1)
print(user_1.followers)

# CONSTRUCTOR
# def __init__(self):
#     #initialize attributes
