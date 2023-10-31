import math

def volume(h, r = 10):
    liquid_volume = ((4*math.pi*r**3)/3) - (math.pi*h**2*(3*r-h))/3
    print(liquid_volume)

volume(2)
