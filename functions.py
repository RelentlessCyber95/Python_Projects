# Fuctions

#def greet(name):
    #print(f"Hello, {name}")
    
#greet("William") 

#def add(a, b):
    #return a + b 

#results = add(2, 5)
#print(results)   


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")
    
    greet("Bob", "Good Morning") 
    
       
        