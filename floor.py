import numpy as np 

class Floor:
    def __init__(self, y, color):
     
        self.y = y
        self.color = np.array(color)

    def Intersections(self, ray_origin, ray_direction):
      
        if ray_direction[1] == 0:  # Ray is parallel to the floor
            return None

        t = (self.y - ray_origin[1]) / ray_direction[1]
        if t > 0:
            return t
        return None

    def normal(self):
      
        return np.array([0, 1, 0])
