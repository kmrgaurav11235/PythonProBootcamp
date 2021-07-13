# Convention is to use Pascal Case (capitalize every word) for a Class
class User:
    # pass  # pass keyword can be used in functions or classes to leave them blank

    def __init__(self, user_id, username):
        # This is Python Constructor -- it is called every time a new object is being created
        # "self" represents the current object
        print("Creating new user...")
        self.id = user_id  # id is now an attribute of User. To refer it use "self.id"
        self.username = username  # username is now an attribute of User
        self.followers = 0  # Default parameter
        self.following = 0  # Default parameter

    # Adding method to a class
    def follow(self, user):
        # A method, unlike a function always needs to have a "self" parameter
        self.following += 1
        user.followers += 1


# user_1 = User()
# # Another way of adding attributes
# user_1.attribute1 = "001"
# user_1.attribute2 = "Rhaenyra"

user_1 = User("001", "Rhaenyra")
print(user_1.username)

# user_2 = User() # Not allowed anymore as Empty constructor is not defined
user_2 = User("002", "Aegon II")
print(user_2.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
