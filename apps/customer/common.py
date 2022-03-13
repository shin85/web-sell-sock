import hashlib
import random
import string



class Common():
    # hashlib md5 string
    def md5_hash(string):
        return hashlib.md5(string.encode('utf-8')).hexdigest()
    
    # random string
    def random_string(size=20, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    
    # password md5
    def md5_password(password, salt = None):
        # if salt is None, random salt
        if salt is None:
            salt = Common.random_string(size = 20)
        return Common.md5_hash(password + salt), salt