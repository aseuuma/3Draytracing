
import numpy as np

# Camera class
class Camera:
    def __init__(self, focal_length, screen_width, screen_height , alpha , beta , principal_point):
        self.focal_length = focal_length
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.alpha = alpha
        self.beta = beta
        self.principal_point = np.array(principal_point)

    def generate_ray(self, pixel_x, pixel_y):
        # Normalize pixel coordinates to NDC
        ndc_x = (pixel_x + 0.5) / self.screen_width * 2 - 1
        ndc_y = 1 - (pixel_y + 0.5) / self.screen_height * 2
        ndc_y /= self.screen_width / self.screen_height

        # Generate ray direction and normalize it
        ray_direction = np.array([ndc_x, ndc_y, -self.focal_length])
        ray_direction /= np.linalg.norm(ray_direction)
        ray_origin = np.array([0, 0, 0])
        return ray_origin, ray_direction
