# v1 = int(input("Enter v1: "))
# v2 = int(input("Enter v2: "))
# t1 = int(input("Enter t1: "))
# t2 = int(input("Enter t2: "))
#
# a=(v2-v1)/(t2-t1)
# print(a)


def acceleration(v1, v2, t1, t2):
    a = (v2 - v1) / (t2 - t1)
    return a


print(acceleration(0, 10, 0, 20))

