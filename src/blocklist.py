import threading

class Blocklist:
    __access_token  = []
    __refresh_token = []

    @classmethod
    def add(cls, token, type):
        if type == 'access':
            cls.__access_token.append(token)
        else: 
            cls.__refresh_token.append(token)

    @classmethod
    def check(cls, token):
        return token in cls.__refresh_token \
            or token in cls.__access_token

    @classmethod
    def clear_access_token(cls):
        cls.__access_token.clear()

    @classmethod
    def clear_refresh_token(cls):
        cls.__refresh_token.clear() 

blocklist = Blocklist()

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

set_interval(blocklist.clear_access_token, 60*15)
set_interval(blocklist.clear_refresh_token, 60*60*24)
