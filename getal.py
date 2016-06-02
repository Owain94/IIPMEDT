import math

a = 2.5

frac, whole = math.modf(a)

print(int(whole))
print(int(frac*10))

