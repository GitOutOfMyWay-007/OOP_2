# Creating own CLASS
class User:  # Creating a Class named User
    def __init__(self, user_id, username):  # Object method
        self.user_id = user_id  # CONSTRUCTOR ( special method - to initialize the object's initial state by assigning values to the object's properties)
        self.username = username  # Object attribute
        self.followers = 0  # Default attribute
        self.following = 0  # Default attribute

    def follow(self,
               user):  # Self should always be a parameter inside the object-method, (so that method knows the object that called it)
        self.following += 1
        user.followers += 1


user_1 = User("191902", "Sarthak")  # Creating an Object and passing values to the parameters from the User Class
# user_1.id = "191902"  # Creating object attribute
# user_1.username = "Sarthak"  # Creating Object attribute

user_2 = User("191905", "Arin")
user_2.complaints = 1  # change default value of the complaints attribute
print(user_1.user_id, user_1.username, user_1.following, user_1.followers)
print(user_2.user_id, user_2.username, user_2.following, user_2.followers)

user_1.follow(user_2)
# user1(Object) uses the follow(method) to follow user2(another object).  So user1 = instance of class, because user1(self) calls the method(follow)
print(user_1.user_id, user_1.username, user_1.following, user_1.followers)
print(user_2.user_id, user_2.username, user_2.following, user_2.followers)
