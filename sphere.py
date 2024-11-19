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
  
