# Introduction to Recursive
# Recursion in computer science is a method of solving a problem where the solution
# depends on solutions to smaller instances of the same problem (as opposed to iteration).

# Example: fibonacci sequence
def fibonacci(number):
    if(number > 1):
        return fibonacci(number-1) + fibonacci(number-2)
    else:
        return number

print (fibonacci(10))
#%%
# Task: Create a function to calculate factorial value
def factorial(number):
    if(number > 1):
        return number * factorial(number-1)
    else:
        return number
    
print (factorial(4))
#%% fibonacci2
def fibonacci2(n,_cache={}):
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, fibonacci2(n-1) + fibonacci2(n-2))
    return n
#%% factorial2
def factorial2(n,_cache={}):
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n,n*factorial2(n-1))
    return n