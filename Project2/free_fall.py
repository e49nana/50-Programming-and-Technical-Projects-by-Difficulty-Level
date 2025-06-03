import numpy as np
import matplotlib.pyplot as plt

def simulate_free_fall(y0, g=9.81, t_max=5, dt=0.01):
    t = np.arange(0, t_max, dt)
    y = y0 - 0.5 * g * t**2
    y = np.maximum(y, 0)
    return t, y

def plot_trajectory(t, y):
    plt.plot(t, y)
    plt.xlabel("Time (s)")
    plt.ylabel("Height (m)")
    plt.title("Free Fall without Air Resistance")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    y0 = float(input("Initial height (m): "))
    t, y = simulate_free_fall(y0)
    plot_trajectory(t, y)
