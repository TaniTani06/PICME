import math
from decimal import *
getcontext().prec = 25      #digits after the 16th are not precise

x = Decimal(math.sqrt(Decimal(2)))/Decimal(4.5)

print (x)