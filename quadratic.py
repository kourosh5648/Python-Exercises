import sys
import math

b = float(sys.argv[1])
c = float(sys.argv[2])

discriminant = b*b - 4.0*c

if discriminant < 0:
    print("moadele rishe haghighi nadarad (delta manfi ast)")
else:
    d = math.sqrt(discriminant)
    print((-b + d) / 2.0)
    print((-b - d) / 2.0)