from mpmath import *

def f(x):
    mp.dps = x//3
    a = int(x*((mpf(2)**mpf(0.5))/mpf(4.5)))
    b = int((x-1)*((mpf(2)**mpf(0.5))/mpf(4.5)))

    return a-b

for i in range(100):
    print(f(i))










#import math
#def f(x):
#    print(int(x*(math.sqrt(2)/5)) - int((x-1)*(math.sqrt(2)/5)))

#máximo de 16 dígitos