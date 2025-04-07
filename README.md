# Brownian Motion Robot Simulation

## How it Works

The robot follows these rules:
1. Moves in straight lines at constant speed
2. When hitting a wall:
   - Stops at the wall
   - Gradually rotates for 0.3-0.6 seconds to a new random angle:
     * Left wall → Rotates to between -89° and +89° (facing right half)
     * Right wall → Rotates to between 91° and 269° (facing left half)
     * Bottom wall → Rotates to between 1° and 179° (facing upper half)
     * Top wall → Rotates to between 181° and 359° (facing lower half)
   - Continues moving in new direction after rotation

## Running the Demo

1. Install requirements:
```bash
pip3 install numpy matplotlib
```

2. Run the demo:
```bash
python3 examples/demo.py
```




## Code Structure

- `brownian/robot.py`: Handles robot movement and wall bounces
- `brownian/simulation.py`: Manages simulation state and robot's path
- `brownian/visualizer.py`: Draws the animation using matplotlib
- `examples/demo.py`: Shows how to use the simulation

## Requirements

- Python 3
- NumPy
- Matplotlib
