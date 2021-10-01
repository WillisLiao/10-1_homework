import math
r, h = map(float, input().split())
mass= math.pi * r**2 *h
print("{:.2f}".format(mass))