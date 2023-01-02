import numpy as np


def rise_fall(domain, peak, t1=6.4e-6, t2=69e-6):
    y = np.zeros(domain.shape)
    
    rise_end = np.argmax(domain > t1)
    t_rise = domain[0:rise_end]
    t_fall = domain[rise_end:]

    # Calculate rising waveform in the form y = at^2 + bt
    # through points (0, 0) and (t1, p), with y' = 0 at t1.
    a = -peak / (t1 ** 2)
    b = 2 * peak / t1
    y[0:rise_end] = a * (t_rise ** 2) + b * t_rise
    
    # Calculate falling waveform in the form y = c * exp(-at)
    # with peak at t1 and 50% of peak at (t2 - t1).
    a = -np.log(0.5) / (t2 - t1)
    c = peak
    y[rise_end:] = c * np.exp(-a * (t_fall - t1))
    
    return y


def damped_sinusoidal(domain, peak, freq=1e6):
    a = freq * np.log(2) / 4.0
    c = peak / np.exp(-np.log(2) / 16)
    y = c * np.exp(-a * domain) * np.sin(2 * np.pi * freq * domain)
    return y