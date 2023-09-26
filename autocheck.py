class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

point = Point(2,3)

point.__x = 12

print(point.__x)

