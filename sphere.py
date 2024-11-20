import numpy as np
from Ray import ray

class Ray :
    def __init__(self, origin,direction):
        self.origin = origin
        self.direction = direction
class Sphere:
  def __init__(self, center, radius, color , ray):
        self.center = np.array(center)
        self.radius = radius
        self.color = color
        self.ray = ray
  
  def intersect(self, ray_origin, ray_direction):
        oc = ray_origin - self.center
        a = np.dot(ray_direction, ray_direction)
        b = 2.0 * np.dot(oc, ray_direction)
        c = np.dot(oc, oc) - self.radius ** 2
        discriminant = b ** 2 - 4 * a * c

        if discriminant < 0:
            return None

        t1 = (-b - np.sqrt(discriminant)) / (2 * a)
        t2 = (-b + np.sqrt(discriminant)) / (2 * a)

        if t1 > 0:
            return t1
        if t2 > 0:
            return t2
        return None
