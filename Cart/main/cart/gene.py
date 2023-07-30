import secrets

def otpgen():
    opt=secrets.randbelow(99999)+1
    return opt