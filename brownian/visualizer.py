import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arrow
from matplotlib.animation import FuncAnimation
import numpy as np

class Visualizer:
    def __init__(self, sim):
        self.sim = sim
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        self.setup_plot()
        self.robot_dot = None
        self.direction = None
        self.trail = None
        
    def setup_plot(self):
        size = self.sim.state['box_size']
        margin = size * 0.1
        
        self.ax.set_xlim(-margin, size + margin)
        self.ax.set_ylim(-margin, size + margin)
        
        self.ax.plot([0, size, size, 0, 0],
                    [0, 0, size, size, 0],
                    'k-', linewidth=2)
        
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_title('Robot Movement')
        self.ax.set_aspect('equal')
        
    def update(self, frame):
        self.sim.step()
        state = self.sim.state
        
        if self.robot_dot:
            self.robot_dot.remove()
        if self.direction:
            self.direction.remove()
        if self.trail:
            self.trail.remove()
        
        pos = state['robot']['position']
        angle = state['robot']['angle']
        bouncing = state['robot']['bouncing']
        
        size = state['box_size'] * 0.02
        self.robot_dot = Circle(pos, size, color='red' if bouncing else 'blue')
        self.ax.add_patch(self.robot_dot)
        
        dx = np.cos(angle) * size * 2
        dy = np.sin(angle) * size * 2
        self.direction = Arrow(pos[0], pos[1], dx, dy, width=size)
        self.ax.add_patch(self.direction)
        
        path = np.array(state['path'])
        self.trail, = self.ax.plot(path[:, 0], path[:, 1], 'g-', alpha=0.5)
        
    def animate(self, duration):
        frames = int(duration / self.sim.dt)
        self.anim = FuncAnimation(
            self.fig, self.update,
            frames=frames,
            interval=self.sim.dt * 1000,
            blit=False
        )
        plt.show()
        
    def save(self, filename, duration):
        frames = int(duration / self.sim.dt)
        self.anim = FuncAnimation(
            self.fig, self.update,
            frames=frames,
            interval=self.sim.dt * 1000,
            blit=False
        )
        
        if filename.endswith('.gif'):
            self.anim.save(filename, writer='pillow')
        elif filename.endswith('.mp4'):
            self.anim.save(filename, writer='ffmpeg')
        else:
            raise ValueError("Filename must end in .gif or .mp4")