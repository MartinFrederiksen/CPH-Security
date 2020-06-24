import re

passwords = ["letmein", "tech", "private", "123456", "admin1"]

def checkPassword(password):
    if password in passwords:
        print("No defualt passwords allowed")
    elif re.search(r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)[A-Za-z\d@$!#%*?&]{8,}", password) == None:
        print("Password must contain at least 1 uppercase letter, 1 lowercase letter, 1 digit, 1 speciel char and be minimum 8 chars long")
    else:
        print("Password is valid")

checkPassword("Tech12!!")
