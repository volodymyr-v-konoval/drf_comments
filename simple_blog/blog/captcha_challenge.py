import random
import string

valid_chars = str(string.ascii_letters + string.digits)

def captcha_castom_challenge():
    
    ret = u''
    for i in range(4):
        ret += random.choice(valid_chars)
    return(ret, ret)
