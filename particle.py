"""
Class for particle definition
"""
import numpy as np

class Particle():
    def __init__(self, coord, velocity):
        self.coord = np.asarray(coord)
        self.velocity = np.asarray(velocity)
    
    def position(self, coord):
        self.coord = np.asarray(coord)

    def speed(self, velocity):
        self.velocity = np.asarray(velocity)

class Particle2d(Particle):
    def __init__(self, coord, velocity):
        super().__init__(coord, velocity)
        self.coord = np.array([coord[0], coord[1]])
        self.velocity = np.array([velocity[0], velocity[1]])

if __name__ == "__main__":

    m0 = Particle((0, 0, 0), 0)
    m1 = Particle2d((0, 0), (1, 0))

    print(m0.coord)
    print(m1.coord)
    m1.position((1, 1))
    print(m1.coord)