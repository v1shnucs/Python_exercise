from .robot import Robot

class Simulation:
    def __init__(self, box_size=10.0, speed=1.0, dt=0.05):
        self.robot = Robot(box_size=box_size, speed=speed)
        self.dt = dt
        self.time = 0.0
        self.path = [(self.robot.x, self.robot.y)]
        
    def step(self):
        self.robot.move(self.dt)
        self.path.append((self.robot.x, self.robot.y))
        self.time += self.dt
        
    def run(self, duration):
        steps = int(duration / self.dt)
        for _ in range(steps):
            self.step()
            
    def reset(self):
        box_size = self.robot.box_size
        speed = self.robot.speed
        self.robot = Robot(box_size=box_size, speed=speed)
        self.path = [(self.robot.x, self.robot.y)]
        self.time = 0.0
        
    @property
    def state(self):
        return {
            'robot': self.robot.state,
            'path': self.path,
            'time': self.time,
            'box_size': self.robot.box_size
        }