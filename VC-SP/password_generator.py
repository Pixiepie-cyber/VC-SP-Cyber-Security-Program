import random

class PasswordGenerator:
    def __init__(self):
        self.pwd_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        self.password = ""

    
        for i in range(32):
            self.password += random.choice(self.pwd_list)
        print(self.password)


#passwdGen = PasswordGenerator()

