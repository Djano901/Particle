"""
Class for particle definition
"""
from abc import ABC
import numpy as np

class Particle(ABC):
    def __init__(self, coord):
        self.coord = coord

class Particle2d(Particle):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def position(self):
        return (self.x, self.y)

class Particle3d(Particle2d):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def position(self):
        return (self.x, self.y, self.z)

if __name__ == "__main__":

    m0 = Particle(0)
    m1 = Particle2d(0, 0)
    m2 = Particle2d(10, 10)
    m3 = Particle3d(0, 0, 1)

    print(m0)
    print(m1.position(), m2.position(), m3.position())