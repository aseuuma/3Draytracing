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





































pygame.quit()
