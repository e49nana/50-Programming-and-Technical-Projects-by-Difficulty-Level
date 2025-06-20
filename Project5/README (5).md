# 🕰️ Pendulum Simulator (Python + Pygame)

This is a basic real-time simulation of a simple pendulum using the Pygame library.

## ✅ Features
- Simple physics: angle update using Euler method
- Adjustable parameters: length, gravity, damping
- Real-time animation with visual feedback

## ▶️ Run the Simulation
Install requirements:
```bash
pip install pygame
```

Then run:
```bash
python pendulum.py
```

## 🧠 Physics Behind
The pendulum equation:
```
θ'' + (g / L) * sin(θ) = 0
```
is numerically solved with a damped Euler method.

---

Ideal as a starting point for real-time physics simulations in Python.
