def outer():
    n = 5
 
    def inner():
        nonlocal n
        n += 1
        print(n)
 
    return inner
 
 
fn = outer()

fn()
fn()
fn()
	
# return inner

fn = outer()

fn()    # 6
fn()
fn()

def multiply(n):
    def inner(m): return n * m
 
    return inner
 
 
fn = multiply(5)
print(fn(5))
print(fn(6))
print(fn(7))

# def inner(m): return n * m

fn = multiply(5)

print(fn(6))

def multiply(n): return lambda m: n * m
 
 
fn = multiply(5)
print(fn(5))
print(fn(6))
print(fn(7))