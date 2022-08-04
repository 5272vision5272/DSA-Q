def lo(function):
    def wrapper1():
        fun=function()
        lowers=fun.lower()
        return lowers
    return wrapper1

def split(function):
    def wrapper1():
        fun=function()
        uppers=fun.split()
        return uppers
    return wrapper1
@split
@lo
def hello():
    return "HHello world"

print(hello())