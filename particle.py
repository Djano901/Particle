"""
Class for particle definition
"""
import numpy as np

class Particle():
    def __init__(self, coord, velocity):
        self.coord = np.asarray(coord)
        self.velocity = np.asarray(velocity)
    
    def move(self, coord):
        self.coord = np.asarray(coord)

    def speedup(self, velocity):
        self.velocity = np.asarray(velocity)

class Particle2d(Particle):
    def __init__(self, coord, velocity):
        super().__init__(coord, velocity)
        self.coord = np.array([coord[0], coord[1]])
        self.velocity = np.array([velocity[0], velocity[1]])
        self.alpfa = self.angle()

    def angle(self, unit='radian'):
        self.magnitude = np.linalg.norm(self.velocity)
        self.alpfa = np.arccos(self.velocity[0]/self.magnitude)
        if np.arcsin(self.velocity[1]/self.magnitude) < 0 :
            self.alpfa *= -1
        else:
            pass
        
        if unit == 'radian':
            return self.alpfa
        elif unit == 'degree':
            return self.alpfa * 180/np.pi
        else:
            raise KeyError(("unauthorized keyword. 'radian' or 'degree' only accepted"))


if __name__ == "__main__":

    m0 = Particle((0, 0, 0), 0)
    m1 = Particle2d((0, 0), (1, -1))

    print(m1.coord)
    m1.move((1, -1))
    print(m1.coord)
    print("velocity vector :", m1.velocity, "angle (radian):", m1.angle(), "angle (degree) :", m1.angle(unit='degree'))
    print("magnitude :", m1.magnitude)