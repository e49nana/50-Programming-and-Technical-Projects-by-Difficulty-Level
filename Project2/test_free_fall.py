from free_fall import simulate_free_fall

def test_free_fall():
    t, y = simulate_free_fall(20, g=10, t_max=2, dt=1)
    assert y[0] == 20
    assert round(y[1], 2) == 15.0
    assert round(y[2], 2) == 0.0
    print("All tests passed.")

if __name__ == "__main__":
    test_free_fall()
