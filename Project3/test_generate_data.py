from generate_data import generate_measurements
import numpy as np

def test_generate_measurements():
    func = np.sin
    x, y_true, y_measured = generate_measurements(func, (0, np.pi), 0.0, 5)
    assert len(x) == 5
    assert np.allclose(y_true, np.sin(x))
    assert np.allclose(y_measured, y_true)  # No noise test
    print("All tests passed.")

if __name__ == "__main__":
    test_generate_measurements()
