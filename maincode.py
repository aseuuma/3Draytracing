import pygame
import numpy as np
import mesh
import camera
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D ratracing")

file_path = 'CUBEE.obj' 
mesh_object = mesh(file_path)
mesh_object.open_3D_object()
Camera = camera(
    focal_length=2,
    alpha=400,
    beta=400,
    principal_point=(width / 2, height / 2),
    rotation_matrix=[[0.36, 0.48, -0.8], [-0.8, 0.6, 0.0], [0.48, 0.64, 0.6]],  # Corrected to 3x3
    translation_vector=np.array([0, 0, -10]),  # Move the camera back to see the object
    mesh=mesh_object  # Pass the mesh to the camera
)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 
    screen.fill((0, 0, 0))

 
    projected_points = Camera.project_points_3d()

    for face in mesh_object.faces:
        for i in range(len(face)):
            start_vertex = projected_points[face[i]]
            end_vertex = projected_points[face[(i + 1) % len(face)]]
            # Draw lines between the projected points
            pygame.draw.line(screen, (255, 255, 255), start_vertex.astype(int), end_vertex.astype(int), 1)

    pygame.display.flip()

pygame.quit()

































pygame.quit()
