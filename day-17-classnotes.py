class User:
    def __init__(self, user_id, username): # constructor
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user): # all methods must have self when as an object
        user.follower += 1
        self.following += 1

user_1 = User(10231, 'john')