class Record(object):
    pass

def function_block():
    ''' function_block documentation '''
    print ('function_block prints this line')
    return None

if function_block():
    print (end='\n')
    print ('function block returned a "True" value')
else:
    print (end='\n')
    print ('function block returned a"False" value')

for count in range(1,6):
    print (count, end=' ')
else:
    print ('At the end of the for loop, count =', count)

print ()

while count > 0:
    print (count, end='  ')
    count -=1
else:
    print ('At the end of the while loop, count =', count)
