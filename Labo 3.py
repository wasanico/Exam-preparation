import time


#Exo 1 call hello

def hello():
    print("hello")
def call(func):
    func()
# call(hello)


#Exo 2 call + params

def add(a,b):
    return a+b
def newcall(n, i, j):
    return n(i,j)
# print(newcall(add, 2, 9))


#exo 3 compute

def newadd (a, b):      #DO NOT FORGET THE RETURN
    return a + b
def sub (a, b):
    return a - b
def compute(a, b, op= newadd):
    return op(a,b)
def newnewcall(n, a, b, *args, **kwargs):
    return n (a, b, *args, **kwargs)

# print ( newnewcall ( compute , 2, 9)) # Affiche ’11’
# print ( newnewcall ( compute , 2, 9, op= sub ))

"""
 ________________________________________________________________________________________________ Part 2

"""

#Exo 1 decorator

def sleep(t):
    def decorator(f):
        def wrapper(*args,**kwargs):        #I don't really understand here...
            res = f(*args,**kwargs)
            time.sleep(t)
            return res  
        return wrapper
    return decorator

@sleep(0.1)
def printnum (i):
    print (i)
cnt = 3


# while cnt > 0:
#     printnum (cnt)
#     cnt -= 1
# print ("KA - BOOM !")


#Exo 2


def binrep(n):
    while n>0:
        bit = n% 2
        n //=2
        yield bit

b = binrep(12) # en binaire c'est 1100  or we can  use bin(num)
for i in b:
    print(i)
while True:
    try:
        print(next(b))
    except StopIteration:
        break