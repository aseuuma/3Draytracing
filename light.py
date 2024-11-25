import numpy as np
class Light:
    def __init__(self, position, intensity):
        self.position = np.array(position)
        self.intensity = intensity
    def model_lambert_lightning(normal, light_direction, light_intensity):
        return max(np.dot(normal, light_direction), 0) * light_intensity