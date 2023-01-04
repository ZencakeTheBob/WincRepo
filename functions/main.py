# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
def greet(x):
    return "Hello, " + x + "!"
greet("Bob")

def add(a, b, c):
    return a + b + c
add(5, 3, 2)

def positive(a):
    comparison = a > 0 
    return comparison
positive(50)
positive(-50)
positive(0)

def negative(a):
    comparison = a < 0
    return comparison
negative(50)
negative(-50)
negative(0)