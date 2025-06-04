import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generate_measurements(func, x_range=(0, 10), noise_level=0.1, n_points=50):
    x = np.linspace(*x_range, n_points)
    y_true = func(x)
    noise = np.random.normal(0, noise_level, size=n_points)
    y_measured = y_true + noise
    return x, y_true, y_measured

def save_to_csv(x, y_true, y_measured, filename="measurements.csv"):
    df = pd.DataFrame({
        "x": x,
        "true_value": y_true,
        "measured_value": y_measured
    })
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def plot_measurements(x, y_true, y_measured):
    plt.plot(x, y_true, label="True Curve")
    plt.scatter(x, y_measured, color="red", label="Measured (with noise)")
    plt.xlabel("x")
    plt.ylabel("Measurement")
    plt.title("Simulated Experimental Data")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    func = np.sin
    x, y_true, y_measured = generate_measurements(func)
    save_to_csv(x, y_true, y_measured)
    plot_measurements(x, y_true, y_measured)
