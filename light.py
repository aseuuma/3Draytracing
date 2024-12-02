import numpy as np
class Light:
    def __init__(self, position, intensity):
        self.position = np.array(position)
        self.intensity = intensity
    def model_lambert_lightning(self,normal, light_direction):
        return max(np.dot(normal, light_direction), 0) * self.intensity
    def model_phong_specular(self, normal, light_direction, view_direction, shininess):
        # The reflection vector (R_m) is calculated as:
        # R_m = 2 * (L_m . N) * N - L_m
        # Where:
        # L_m is the light direction vector
        # N is the normal vector at the point of intersection
        # The dot product of L_m and N is used to determine how much of the light is reflected
        reflect_direction = 2 * np.dot(normal, light_direction) * normal - light_direction
        spec_angle = max(0, np.dot(view_direction, reflect_direction))
        return self.intensity * (spec_angle ** shininess)