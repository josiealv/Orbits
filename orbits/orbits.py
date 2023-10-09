import numpy as np
from PyAstronomy import pyasl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def main():
    orbit = pyasl.KeplerEllipse(a=1.0, per=1.0, e=0.5, Omega=0.0, i=30.0, w=0.0)
    t = np.linspace(0, 4, 200)

    # pos is 3 col array returned from xyzPos w/ each array size = size of t array
    # coordinates are in (Y, X, Z) 
    pos = orbit.xyzPos(t) # first point in pos corresponds to perigee
    
    plt.plot(0, 0, 'bo', markersize=9, label="Earth")
    plt.plot(pos[::, 1], pos[::, 0], 'k-', label="Satellite Trajectory")
    plt.plot(pos[0, 1], pos[0, 0], 'r*', label="Periapsis")

    plt.legend(loc="upper right")
    plt.title('Orbital Simulation')
    plt.ioff()
    plt.show()  

main()