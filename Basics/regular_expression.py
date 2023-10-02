import re

# Method 1
# def check_valid_password(password_input):

#     if len(password_input) < 8:
#         return False

#     if not re.search(r'[A-Z]', password_input):
#         return False

#     if not re.search(r'[a-z]', password_input):
#         return False

#     if not re.search(r'[0-9]', password_input):
#         return False

#     if not re.search(r'[!@#$%^&*()-=_+[\]{};:\'",.<>?/\\|]', password_input):
#         return False
#     return True

# password_input = input("Enter your password: ")
# if check_valid_password(password_input):
#     print("Correct Format")
# else:
#     print('Incorrect Format')



# Method 2
# def password_check(password_input):
#     if len(password_input) > 8 and re.search(r'[A-Z]', password_input) and re.search(r'[a-z]', password_input) and re.search(r'[0-9]', password_input) and re.search(r'[!@#$%^&*()-=_+[\]{};:\'",.<>?/\\|]', password_input):
#         print("Correct Password")
#     else:
#         print("Password should be at least 8 characters with Upper and lower Case letters ,should have at least a number and special characters ")

# password_input = input("Enter your password: ")
# password_check(password_input)



# Method 3
password_input = input("Enter your password: ")
message = "Correct Password"
if len(password_input) > 8:
    if re.search(r'[0-9]', password_input):
        if re.search(r'[A-Z]', password_input):
            if re.search(r'[!@#$%^&*()-=_+[\]{};:\'",.<>?/\\|]', password_input):
                if re.search(r'[a-z]', password_input):
                    print("Hurray🎉✨! , Correct Password")
                else:
                    print("Password has no Lower Case characters")
            else:
                print("Password has no Special characters")
        else:
            print("Password has no Upper case  characters")
    else:
        print("Password has no Numeric characters")
else:
    print("Password is less than 8 Characters")
