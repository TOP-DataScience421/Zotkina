from math import sqrt

class Tetrahedron:
    def __init__(self, edge):
        self.edge = edge

    def surface(self):
        s = self.edge / 2
        area = sqrt(3) * s**2
        return area

    def volume(self):
        return (self.edge**3) / (6 * sqrt(2))

 #тестирование
#>>> t1 = Tetrahedron(5)
#>>> t1.edge
#5
#>>> t1 = Tetrahedron(6)
#>>> t1.surface()
#15.588457268119894
#>>> t1.volume()
#25.455844122715707 
  