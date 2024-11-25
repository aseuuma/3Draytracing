import pygame
import numpy as np
from mesh import Mesh
from camera import Camera
from light import Light
from sphere import Sphere
# Pygame setup
pygame.init()
screen_width, screen_height = 600, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("3D Raytracing ")
clock = pygame.time.Clock()

f_length = 400    # focal length (f)
alpha = 1   # for x-axis
beta = 1    # for y-axis
u0, v0 = screen_width // 2, screen_height // 2    # center of projection


# Initialize the camera
focal_length = 1
mesh_object = Mesh('eyeball.obj')
sphere_vertices, sphere_faces = mesh_object.open_3D_object('eyeball.obj')
sphere_vertices = sphere_vertices  + np.array([0, 0, 300])
camera = Camera(focal_length, screen_width, screen_height , 400 , 400 , focal_length)
centre_sphere = np.mean(sphere_vertices, axis = 0)
# La distance entre le centre et tous les points de sphere
distances = np.linalg.norm(sphere_vertices - centre_sphere, axis=1)
radius_sphere = np.mean(distances)
print(radius_sphere)
# Scene setup
spheres = [
    Sphere(center=[0, 0, -5], radius=radius_sphere, color=[255, 255, 0]),
]
light = Light(position=[5, 10, -5], intensity=1.0)

ambient_light = 0.1  # Ambient light intensity

# Rendering loop
for y in range(screen_height):
    for x in range(screen_width):
        ray_origin, ray_direction = camera.generate_ray(x, y)

        closest_t = 100
        closest_color = np.array([0, 0, 0])

        for sphere in spheres:
            t = sphere.Intersections(ray_origin, ray_direction)
            if t and t < closest_t:
                normal = sphere.normal(ray_origin, ray_direction)
                if normal is None:  # Skip if no valid normal
                    continue
                closest_t = t
                intersection_point = ray_origin + t * ray_direction

                # Calculate light direction
                light_direction = light.position - intersection_point
                light_direction /= np.linalg.norm(light_direction)

                # Diffuse lighting calculation
                diffuse = light.model_lambert_lightning(normal, light_direction)

                # Combine ambient and diffuse lighting
                color = ambient_light * sphere.color + diffuse * sphere.color
                closest_color = np.clip(color, 0, 255)

        # Set pixel color
        screen.set_at((x, y), tuple(closest_color.astype(int)))

    pygame.display.flip()