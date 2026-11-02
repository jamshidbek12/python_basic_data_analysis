a = int(input())
b = int(input())

def check(func):
    def wrapper(a,b):
        if(b!=0):
            return func(a,b)            
        else:
            return("Denominator can't be zero")
    return wrapper

    

@check
def div(a,b):
    return int(a/b)

print(div(a,b))
