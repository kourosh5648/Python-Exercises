import sys

year = int(sys.argv[1])

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("sal", year, "kabise ast")
else:
    print("sal", year, "kabise nist")