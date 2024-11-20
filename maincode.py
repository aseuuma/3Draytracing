import pygame
import numpy as np
from  mesh import Mesh
from camera import Camera
from sphere import Sphere
pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Raytracing")


file_path = 'eyeball.obj'  
mesh_object = Mesh(file_path)
mesh_object.open_3D_object()

spheres = [
    Sphere(center=[0, 0, -5], radius=2, color=(255, 0, 0)),   
    Sphere(center=[2, 1, -6], radius=1, color=(0, 255, 0)), 
    Sphere(center=[-2, -1, -4], radius=1, color=(0, 0, 255)),
    Sphere(center=[-2,29 , -4], radius=2, color=(0, 255, 255))
]
camera = Camera(
    focal_length=2,
    alpha=400,
    beta=400,
    principal_point=(width / 2, height / 2),
    rotation_matrix=[[0.36, 0.48, -0.8], [-0.8, 0.6, 0.0], [0.48, 0.64, 0.6]], 
    translation_vector=np.array([0, 0, -10]),  
    mesh=mesh_object  
)

running = True
clock = pygame.time.Clock()

for y in range(screen_height):
    for x in range(screen_width):
        ray_origin, ray_direction = camera.generate_ray(x, y)

        pixel_color = (0, 0, 0)  # Default background color (black)
        intersection_point = None

 
        for sphere in spheres:
            t = sphere.intersect(ray_origin, ray_direction)
            if t is not None:
                intersection_point = ray_origin + t * ray_direction  # Calculate intersection point
                pixel_color = sphere.color
                break  # Once we find the intersection, no need to check further spheres

       
        screen.set_at((x, y), pixel_color)
   
        if pixel_color != (0, 0, 0):
            print(f"Pixel ({x},{y}): Intersection at t={t}")

    pygame.display.flip()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()


    projected_points = camera.project_avec_rotation()

    for face in mesh_object.faces:
        for i in range(len(face)):
            start_vertex = projected_points[face[i]]
            end_vertex = projected_points[face[(i + 1) % len(face)]]
            pygame.draw.line(screen, (255, 255, 255), start_vertex.astype(int), end_vertex.astype(int), 1)

    pygame.display.flip()

pygame.quit()
