import sys
n = int(input(" input number: "))
i = 0 
power = 1
while i <= n:
    print(str(i) + ' ' + str(power))
    i += 1
    power *= 2 


import sys
n = int(input(" imput number: "))
power = 1
for i in range(n + 1):
    print(str(i) + ' ' + str(power))
    power *= 2
    
