import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from brownian import Simulation, Visualizer

def main():
    sim = Simulation(
        box_size=6.0,     # Smaller box to see more bounces
        speed=2.5,        # Good speed for visible movement
        dt=0.02           # 50fps for smooth rotation animation
    )
    
    vis = Visualizer(sim)
    
    print("Creating animation...")
    vis.save('brownian_motion.gif', duration=10.0)
    print("Saved as brownian_motion.gif")
    
    print("\nStarting live view (press Ctrl+C to exit)")
    sim.reset()
    vis.animate(duration=30.0)

if __name__ == "__main__":
    main()