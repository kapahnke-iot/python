
x = 5
type(x)  # output only in the python shell
y = 10
y = 0xA    # hexadecimal
y = 0o12   # octal (python2 uses O12)
y = 0b1010 # binary
print ('x =', x, ',', 'y =', y)

# Typically comparisons can be made
print ('x == y =', x == y)
print ('x != y =', x != y)
print ('x >= y =', x >= y)
print ('x > y =', x > y)
print ('x <= y =', x <= y)
print ('x < y =', x < y)

# The usual operators can be used
print ('x + y =', x + y)
print ('x - y =', x - y)
print ('x * y =', x * y)
print ('x / y =', x / y)

# In Python 2, ,x / y uses floor division like
print ('x // y =', x // y)
print ('x % y =', x % y)
print ('x ** y =', x ** y)  # power 

# There are several useful builtin functions
print ('divmod(x, y) = ', divmod(x, y))
print ('pow(x,y) = ', pow(x,y))
print ('abs(-x) = ', abs(-x))
print ('int(5.2) = ', int(5.2))
print ('int("0xff",16) = ', int("0xff",16))
print ('float(x) = ', float(x))

# Inline notification can also be used
print ('x = x + y =', end = ' ')
x += y
print (x)

print ('x = x - y =', end = ' ')
x -= y
print (x)

print ('x = x * y =', end = ' ')
x *= y
print (x)

print ('x = x / y =', end = ' ')
x /= y
print (x)

# Multiple assignments can be done
x, y = 4, 2
print ('x=', x, ',', 'y = ', y)

# Bitwise operations can be used
print ('OR: x | y =' , x | y)
print ('XOR: x ^ y =', x ^ y)
print ('AND: x & y =', x & y)
print ('Left shift: x << y =', x << y)
print ('Right shift: x >> y =', x >> y)
print ('Inversion: ~x =', ~x)




