import math

if __name__ == '__main__':
    ab = int(input())
    bc = int(input())

    deg = round(math.degrees(math.atan2(ab, bc)))
    print("{}°".format(deg))

