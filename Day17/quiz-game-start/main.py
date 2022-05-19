# creates the user class(object) from the initial code example representation
class User:
    # this init creates the initial values for the items in the object
    def __init__(self, user_id, username):
        # including a print statement here in the init will print every time the object is created
        # print("new user being created...")
        # initializes the id for the user based on the user_id passed in for the code
        self.id = user_id
        # initializes the username for the user based on the username passed in when the object was created
        self.username = username
        self.followers = 0
        self.following = 0

    # creates a method
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('001', 'angela')
user_2 = User('002', 'bob')

user_1.follow(user_2)
