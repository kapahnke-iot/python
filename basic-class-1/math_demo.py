x, y = 5.0, 10
print ('x =', x, ',', 'y =', y)
import math

# The math module provides a couple of constants
pi = math.pi
e = math.e
print ('The value of pi is:', pi)
print ('The rounded value of pi is:', round(pi, 10))

# The float class allows creation of special numbers
pos_inf = float('inf')
neg_inf = float('-inf')
not_a_num = float('nan')

# The math module provides functions to detect these numbers
print ('math.isinf(pos_inf) =', math.isinf(pos_inf))
print ('math.isinf(neg_inf) =', math.isinf(neg_inf))
print ('math.isinf(not_a_num) =', math.isnan(not_a_num))


