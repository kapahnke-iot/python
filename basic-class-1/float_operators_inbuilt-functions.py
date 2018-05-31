x = 5.0
type(x)    # output only in the python shell
y = float.fromhex('A')
print('x =', x, ',' , 'y =' ,y)
print ('x.as_integer_ratio() =', x.as_integer_ratio())
print('y.hex() =', y.hex())

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
print ('x // y =', x // y)
print ('x % y =', x % y)
print ('x ** y =', x ** y)  # power

# There are several useful builtin functions
print ('divmod(x, y) = ', divmod(x, y))
print ('pow(x,y) = ', pow(x,y))
print ('abs(-x) = ', abs(-x))
print ('int(x) = ', int(x))
print ('float(10) = ', float(x))

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

# Bitwise operations CAN NOT be used
