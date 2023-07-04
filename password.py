class PasswordCheck():
    pass_ = Noneone
    commonPass = ["123456", "123456789", "password", "12345", "1234567", "1234567890", "letmein", "football", 
    "guest", "a1b2c3", "Password1", "1234", "abc123", "12345678", "qwerty", "baseball", "unknown", "soccer"]
    
    enteredPasswords = []
    ditOfPasses = {}
    
    def _init(self):
        self.manager()
        
    def _str_(self):
        return(self.pass_, self.commonPass, self.ditOfPasses, self.enteredPasswords)
    
    def manager(self):
        
        
    
    length = len(password)         
    has_uppercase = any(char.isupper() for char in password)         
    has_lowercase = any(char.islower() for char in password)         
    has_number = any(char.isdigit() for char in password)         
    has_special_char = bool(re.search(r"[!@#$%^&*()_+=\-[\]{};':\"\\|,.<>/?]", password))