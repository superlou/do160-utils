import numpy as np
import matplotlib.pyplot as plt
from util import rise_fall, damped_sinusoidal


def waveform3(domain, level):
    voc_map = {
        1: 100, 2: 250, 3: 600, 4: 1500, 5:3200
    }
    
    peak = voc_map[level]
    return damped_sinusoidal(domain, peak)


def waveform4(domain, level):
    voc_map = {
        1: 50, 2: 125, 3: 300, 4: 750, 5:1600
    }
    
    peak = voc_map[level]
    return rise_fall(domain, peak)


def example():
    t3 = np.linspace(0, 20e-6, 1000)
    y3 = waveform3(t3, 1)

    t4 = np.linspace(0, 200e-6, 1000)
    y4 = waveform4(t4, 3)
    
    plt.subplot(211)
    plt.plot(t3, y3)
    plt.grid()
    plt.title("Waveform 3")
    
    plt.subplot(212)
    plt.plot(t4, y4)
    plt.grid()
    plt.title("Waveform 4")
    
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    example()