from abc import ABC, abstractmethod

class Ancestor(ABC):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @abstractmethod
    def fabric(self):
        pass


class Coat(Ancestor):

   def fabric(self):
       return round(self.size / 6.5 + 0.5)


class Suit(Ancestor):

    def fabric(self):
        return round(self.size * 2 + 0.3)


class Garments(Ancestor):
    def __init__(self, name, size, g_type):
        super().__init__(name, size)
        self.g_type = g_type

    @property
    def fabric(self):
        if self.g_type == 'coat':
            obj = Coat(self.name, self.size)
            return Coat.fabric(obj)
        elif self.g_type == 'suit':
            obj = Suit(self.name, self.size)
            return Suit.fabric(obj)


# c1 = Coat('Burdock', 850)
# s1 = Suit('suit', 190)
# print(c1.fabric())

c1 = Garments('coat1', 888, 'coat')
s2 = Garments('suit1', 190, 'suit')
print(c1.fabric, s2.fabric)
