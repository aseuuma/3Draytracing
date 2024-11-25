import numpy as np
class Light:
    def __init__(self, position, intensity):
        self.position = np.array(position)
        self.intensity = intensity
    def model_lambert_lightning(self,normal, light_direction):
        return max(np.dot(normal, light_direction), 0) * self.intensity