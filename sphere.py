import numpy as np
from camera import Camera
class Sphere:
  def __init__(self, center, radius, color , ray):
        self.center = np.array(center)
        self.radius = radius
        self.color = color
        
  def get_normal(self, point):
        # Calculate surface normal
        return (point - self.center) / np.linalg.norm(point - self.center)
  def normal(self, ray_origin, ray_direction):
        t = Camera.intersect(ray_origin, ray_direction)
        if t is None:
            return None  
        intersection_point = ray_origin + t * ray_direction
        return self.get_normal(intersection_point)