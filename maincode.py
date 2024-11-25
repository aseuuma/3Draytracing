import pygame
import numpy as np
from mesh import Mesh
from camera import Camera
# Pygame setup
pygame.init()
width, height = 600, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Raytracing ")
clock = pygame.time.Clock()

f_length = 400    # focal length (f)
alpha = 1   # for x-axis
beta = 1    # for y-axis
u0, v0 = width // 2, height // 2    # center of projection

mesh_object = Mesh('eyeball.obj')
sphere_vertices, sphere_faces = mesh_object.open_3D_object('eyeball.obj')

camera = Camera(
    focal_length=f_length,
    alpha=alpha,
    beta=beta,
    principal_point=(width / 2, height / 2 , 2),
    rotation_matrix=[[0.36, 0.48, -0.8], [-0.8, 0.6, 0.0], [0.48, 0.64, 0.6]], 
    translation_vector=np.array([0, 0, -10]),  
    mesh=mesh_object,
    width=width,
    height=height
)
# Translate the vertices along z_axis
sphere_vertices = sphere_vertices * 100 + np.array([0, 0, 300])

# Define the camera position in 3D space
camera_position = camera.principal_point  # Camera at origin
centre_sphere = np.mean(sphere_vertices, axis = 0)
# La distance entre le centre et tous les points de sphere
distances = np.linalg.norm(sphere_vertices - centre_sphere, axis=1)
radius_sphere = np.mean(distances)



def Intersections(origin_ray, direction_ray, centre_sphere, radius_sphere):
    o_c = origin_ray - centre_sphere
    # From the quadratic equation we found:
    a = np.dot(direction_ray, direction_ray)
    b = 2 * np.dot(o_c , direction_ray)
    c = np.dot(o_c , o_c) - radius_sphere**2

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

colored_pixels = set()

# Main loop
running = True
while running:
    # screen.fill((85,0,102))
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for y in range(width):
        for x in range(height):
            # Pour eviter de recolorer les pixels 2 fois
            if (x, y) in colored_pixels:
                continue
            position_point =np.array([x - u0, y - v0, f_length])
            direction_ray = position_point - camera_position
            direction_ray = direction_ray / np.linalg.norm(direction_ray)  # Normalize

            t = Intersections(camera_position, direction_ray, centre_sphere, radius_sphere)
            if t is not None:
                #print(t)
                # Colorer le pixel
                # screen.set_at((x,y), (255, 0, 255))
                depth_color = int(255 - min(t, 255))
                color = (depth_color, depth_color, 0) 
                #print(color)
                screen.set_at((x, y), color)
                colored_pixels.add((x, y))

                pygame.display.update()


    # pygame.display.flip()
    clock.tick(30)
pygame.quit()
