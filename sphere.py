import numpy as np



class Sphere:
  def __init__(self, center, radius, color):
        self.center = np.array(center)
        self.radius = radius
        self.color = color
