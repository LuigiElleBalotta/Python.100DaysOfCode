class User:
    def __init__(self, user_id, username, followers=0, following=0):
        print("User is being created")
        self.__id = user_id
        self.username = username
        self.followers = followers
        self.following = 0

    def __str__(self):
        return f"User {self.__id} is {self.username}"

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(user_id="001", username="luigi")
user_2 = User(user_id="002", username="mario")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
