import numpy as np
from camera import Camera
class Sphere:
  def __init__(self, center, radius, color ):
        self.center = np.array(center)
        self.radius = radius
        self.color = np.array(color, dtype=np.float32)  
        
  def get_normal(self, point):
        # Calculate surface normal
        return (point - self.center) / np.linalg.norm(point - self.center)
  def normal(self, ray_origin, ray_direction):
        t = self.Intersections(ray_origin, ray_direction)
        if t is None:
            return None  
        intersection_point = ray_origin + t * ray_direction
        return self.get_normal(intersection_point)
  def Intersections(self,origin_ray, direction_ray):
      o_c = origin_ray - self.center
      # From the quadratic equation we found:
      a = np.dot(direction_ray, direction_ray)
      b = 2 * np.dot(o_c , direction_ray)
      c = np.dot(o_c , o_c) - self.radius**2

      # Calcule de Delta
      delta = b**2 - 4 * a * c

      # Calculer les solutions qui sont les intersection avec l'objet sphere
      if delta < 0:
          return None
      else:
          t_1 = (-b + np.sqrt(delta)) / (2 * a)
          t_2 = (-b - np.sqrt(delta)) / (2 * a)
          positive_ts = []
          if t_1 > 0:
              positive_ts.append(t_1)
          if t_2 > 0:
              positive_ts.append(t_2)
          if positive_ts:
              return min(positive_ts)

          return None