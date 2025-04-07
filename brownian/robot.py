import numpy as np

class Robot:
    def __init__(self, box_size=10.0, speed=1.0):
        self.box_size = box_size
        self.speed = speed
        
        self.x = box_size / 2
        self.y = box_size / 2
        self.angle = np.random.uniform(0, 2*np.pi)
        
        self.bouncing = False
        self.turn_time = 0
        self.turn_duration = 0
        self.min_bounce = np.pi/180
        self.start_angle = self.angle
        self.target_angle = self.angle
        
    def move(self, dt):
        if self.bouncing:
            self.turn_time -= dt
            # Calculate rotation progress (0 to 1)
            progress = 1 - (self.turn_time / self.turn_duration)
            # Interpolate angle
            self.angle = self._interpolate_angle(
                self.start_angle, 
                self.target_angle, 
                min(1.0, progress)
            )
            if self.turn_time <= 0:
                self.bouncing = False
                self.angle = self.target_angle
            return
            
        new_x = self.x + self.speed * np.cos(self.angle) * dt
        new_y = self.y + self.speed * np.sin(self.angle) * dt
        
        if new_x <= 0:
            self._start_bounce('left')
            new_x = 0
        elif new_x >= self.box_size:
            self._start_bounce('right')
            new_x = self.box_size
        elif new_y <= 0:
            self._start_bounce('bottom')
            new_y = 0
        elif new_y >= self.box_size:
            self._start_bounce('top')
            new_y = self.box_size
        else:
            self.x = new_x
            self.y = new_y
            
    def _interpolate_angle(self, start, end, t):
        # Find the shortest rotation direction
        diff = end - start
        if diff > np.pi:
            diff -= 2 * np.pi
        elif diff < -np.pi:
            diff += 2 * np.pi
        return start + diff * t
            
    def _start_bounce(self, wall):
        self.bouncing = True
        self.turn_duration = np.random.uniform(0.3, 0.6)  # Longer duration to see rotation
        self.turn_time = self.turn_duration
        self.start_angle = self.angle
        
        angle_range = np.pi - 2*self.min_bounce
        if wall == 'left':
            self.target_angle = np.random.uniform(-angle_range/2, angle_range/2)
        elif wall == 'right':
            self.target_angle = np.pi + np.random.uniform(-angle_range/2, angle_range/2)
        elif wall == 'bottom':
            self.target_angle = np.pi/2 + np.random.uniform(-angle_range/2, angle_range/2)
        else:  # top
            self.target_angle = 3*np.pi/2 + np.random.uniform(-angle_range/2, angle_range/2)
            
    @property
    def state(self):
        return {
            'position': (self.x, self.y),
            'angle': self.angle,
            'bouncing': self.bouncing
        }