import pygame
import numpy as np
from mesh import Mesh
from camera import Camera
from light import Light
from sphere import Sphere
from floor import Floor
# Pygame setup
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("3D Raytracing ")


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
#print(radius_sphere)

scaling_factor = 0.5  # Adjust this value to control the sphere size
small_radius = radius_sphere * scaling_factor


spheres = [
    Sphere(center=[-2, -1, -6], radius=small_radius, color=[255, 0, 255]),
    Sphere(center=[0, -1, -5], radius=small_radius, color=[255, 255, 0]),
    Sphere(center=[2, 0, -6], radius=radius_sphere, color=[255, 0, 0]),
]
light = Light(position=[10, 10, -5], intensity=1.0)

ambient_light = 0.1 
background_color =  np.array([	135, 206, 235]) 
def shadow(intersection_point, light_direction, spheres, current_sphere):
  
    for sphere in spheres:
        if sphere is current_sphere: 
            continue
        shadow_t = sphere.Intersections(intersection_point + 0.001 * light_direction, light_direction)
        if shadow_t:  
            return True
    return False



floor = Floor(y=-2, color=[100, 255, 100])  # Gray floor at y = -2


for y in range(screen_height):
    for x in range(screen_width):
        ray_origin, ray_direction = camera.generate_ray(x, y)

        closest_t = 100
        closest_color = background_color  # Start with the background color

        # Check for intersections with spheres
        for sphere in spheres:
            t = sphere.Intersections(ray_origin, ray_direction)
            if t and t < closest_t:
                normal = sphere.normal(ray_origin, ray_direction)
                if normal is None:
                    continue
                closest_t = t
                intersection_point = ray_origin + t * ray_direction

                # Calculate light direction
                light_direction = light.position - intersection_point
                light_direction /= np.linalg.norm(light_direction)
                view_direction = -ray_direction
                # Shadow check
                in_shadow = shadow(intersection_point, light_direction, spheres, sphere)

                if in_shadow:
                    color = ambient_light * sphere.color
                else:
                    sh = 32
                    shiness = light.model_phong_specular(normal, light_direction, view_direction, sh)
                    diffuse = light.model_lambert_lightning(normal, light_direction)
                    color = ambient_light * sphere.color + diffuse * sphere.color +shiness * np.array([255, 255, 255])

                closest_color = np.clip(color, 0, 255)

        # Check for intersection with the floor
        t = floor.Intersections(ray_origin, ray_direction)
        if t and t < closest_t:
            closest_t = t
            intersection_point = ray_origin + t * ray_direction

            # Calculate light direction
            light_direction = light.position - intersection_point
            light_direction /= np.linalg.norm(light_direction)

            # Shadow check
            in_shadow = shadow(intersection_point, light_direction, spheres, None)

            if in_shadow:
                color = ambient_light * floor.color  # Only ambient lighting
            else:
                diffuse = light.model_lambert_lightning(floor.normal(), light_direction)
                color = ambient_light * floor.color + diffuse * floor.color

            closest_color = np.clip(color, 0, 255)

        # Set pixel color
        screen.set_at((x, y), tuple(closest_color.astype(int)))

    pygame.display.flip()

# Add an event loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
