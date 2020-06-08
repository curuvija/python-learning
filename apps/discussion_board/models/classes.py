
class User:

    def __init__(self, name, lastname, email, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password

class DiscussionBoard:
    
    def __init__(self, members, title, goal, time):
        self.member = members
        self.title = title
        self.goal = goal
        self.time = time

    def remove_member(self, user):
        pass

    def add_member(self, user):
        pass

    def raise_hand(self, user):
        pass

    def close(self):
        pass