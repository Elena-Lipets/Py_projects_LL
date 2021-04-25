class Road:
    __length = None
    __width = None

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def asphalt_mass(self, depth, m_per_m):
        mass = self.__width * self.__length * depth * m_per_m
        return mass

highway = Road(50, 6)
print(highway.asphalt_mass(20, 15))

