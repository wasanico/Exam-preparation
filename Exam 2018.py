


#Exo 1.1 : reductor


def reduce(func, L, output):
    reduced = output
    for elem in L:
        reduced.append(min(elem,func))   
    return reduced

def limitMax(maximum):
    return maximum

# print(reduce(limitMax(3), [1, 2, 3, 4, 5, 6], [])) # return [1, 2, 3, 3, 3, 3]


#Exo 1.2 : recursive


from math import sin


def zero(fn, inf, sup):
    a = fn(inf) 
    b = fn(sup)
    if (a > 0 and  b<0) or (a < 0 and b>0):        
        #there exists a racine between the two so then we add the inf with a to have a new bborder closer to what we want
        newinf = inf + a
        newsup = sup + b
        print("new borders :",newinf,newsup)
        return zero(fn,newinf,newsup)
        
    else:
        print("no")
        return None



# zero(sin, 2, 4) # renvoie 3.141592025756836


#Exo 1.3 : decorateur


def password(correct_pswd):
    def decorator(f):
        def wrapper(test_pswd, *args,**kwargs):
            """this wrapper takes an extra argument than the original function.
            This is very unusual. Typically we try hard to keep the wrapper
            function with the same signature as the original"""
            if test_pswd == correct_pswd:
                return f(*args,**kwargs)
            else:
                return "Access denied"
        return wrapper
    return decorator
    

@password("secret")
def add(a, b):
    return a + b

# print(add("secret", 1, 2)) # ValueError Exception
# print(add("yeet", 1, 2)) # 3


#Exo 1.4 : Trees


class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def treeMax(tree):      #find the greatest value of the tree
    print(tree)



t = Tree(0,
        Tree(4, 
            Tree(-5), 
            Tree(3, 
                Tree(8), 
                Tree(1))),
        Tree(2, 
            Tree(4)))

treeMax(t)