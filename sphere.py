import numpy as np
from Ray import ray


class Sphere:
  def __init__(self, center, radius, color , ray):
        self.center = np.array(center)
        self.radius = radius
        self.color = color
        self.ray = ray
  
