import pygame
import numpy as np
from  mesh import Mesh
from camera import Camera

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Object Projection")


file_path = 'CUBEE.obj'  
mesh_object = Mesh(file_path)
mesh_object.open_3D_object()


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
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  
    screen.fill((0, 0, 0))

    projected_points = camera.project_points_3d()

    for face in mesh_object.faces:
        for i in range(len(face)):
            start_vertex = projected_points[face[i]]
            end_vertex = projected_points[face[(i + 1) % len(face)]]
            pygame.draw.line(screen, (255, 255, 255), start_vertex.astype(int), end_vertex.astype(int), 1)

    pygame.display.flip()

pygame.quit()
