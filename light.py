import numpy as np
class Light:
    def __init__(self, position, intensity):
        self.position = np.array(position)
        self.intensity = intensity
    def model_lambert_lightning(self,normal, light_direction):
        return max(np.dot(normal, light_direction), 0) * self.intensity
    def model_phong_specular(self, normal, light_direction, view_direction, shininess):
         
        reflect_direction = 2 * np.dot(normal, light_direction) * normal - light_direction
        spec_angle = max(0, np.dot(view_direction, reflect_direction))
        return self.intensity * (spec_angle ** shininess)