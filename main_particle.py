import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from particle import Particle2d
import numpy as np

GRAVITY = -9.81
T_START = 0
T_END = 10
STEP = 1000

INTERV = (T_END - T_START)/STEP

t = np.linspace(T_START, T_END, STEP)
m1 = Particle2d([0,0], [0,0])

if __name__ == "__main__":

    fig, ax = plt.subplots()
    xdata, ydata = [], []
    ln, = ax.plot([], [], 'ro')

    def init():
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1000, 0.5)
        ax.grid()
        return ln,

    def update(t):
        m1.speedup([0, GRAVITY*INTERV + m1.velocity[1]])
        m1.move([0, m1.velocity[1]*INTERV + m1.coord[1]])
        text = ax.text(-0.98, -100, "t= {00:.3f} s ".format(t) + "speed= {:.2f}".format(m1.velocity[1]) + r" m.s$^{-1}$")
        ln.set_data(m1.coord[0], m1.coord[1])
        return ln, text

    ani = FuncAnimation(fig, update, frames=t,
                        init_func=init, blit=True,
                        interval=INTERV*1e3
                        )
    plt.show()