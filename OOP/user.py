# class User:

#     def __init__(self,username,email,password):
#         self.username = username
#         self._email = email
#         self.password = password

#     def get_email(self):
#         return self._email
    
#     def set_email(self, new_email):
#        if '@' in new_email:
#         self._email = new_email
#         print("Email Has been Changed!")
#        return new_email

# user1 = User("Alex","alec12@gmail.com","123")
# print(user1.get_email())

# user1.set_email("james22@gmail.com")
# print(user1.get_email())



# Getters and Setters
class User:

    def __init__(self,username,email,password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email):
       if '@' in new_email:
        self._email = new_email
        print("Email Has been Changed!")
       return new_email


user1 = User("Alex","alec12@gmail.com","123")
print(user1.email)
user1.email = 'james@gmail.com'
# user1.email = 'james@gmail.com'
print(user1.email)
