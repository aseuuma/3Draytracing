import pygame
import numpy as np

class Camera : 
    def __init__(self, focal_length, alpha, beta, principal_point, rotation_matrix, translation_vector, mesh):
        
        self.focal_length = focal_length #focalde de camera
        self.alpha = alpha
        self.beta = beta
        self.principal_point = np.array(principal_point)
        
       
        self.rotation_matrix = np.array(rotation_matrix)
        self.translation_vector = np.array(translation_vector).reshape(-1, 1)
        
        
        self.mesh = mesh
        
       
        self.intrinsic_matrix = self.compute_intrinsic_matrix()
        self.extrinsic_matrix = self.compute_extrinsic_matrix()
        self.projection_matrix = self.compute_projection_matrix()

    def compute_intrinsic_matrix(self):
        falpha = self.focal_length * self.alpha
        fbeta = self.focal_length * self.beta
        u0, v0 = self.principal_point
        
        K = np.array([
            [falpha, 0, u0],
            [0, fbeta, v0],
            [0, 0, 1]
        ])
        return K

    def compute_extrinsic_matrix(self):
        return np.hstack((self.rotation_matrix, self.translation_vector))

    def compute_projection_matrix(self):
        return np.dot(self.intrinsic_matrix, self.extrinsic_matrix)   

   
    def project_avec_rotation(self):
      
        points = np.array(self.mesh.vertices)
        points_3d = np.hstack((points, np.ones((points.shape[0], 1))))
        points_2d= np.dot(self.projection_matrix, points_3d.T).T
        return points_2d[:, :2] / points_2d[:, 2, np.newaxis]
    def project_points_3d(self):
        points = np.array(self.mesh.vertices)

        points[:, 2] += self.translation_vector[2] 
        projected_points = points[:, :2] / points[:, 2, np.newaxis] #مقسمة على Z هنا

        projected_points[:, 0] = projected_points[:, 0] *self.alpha *self.focal_length + self.principal_point[0]
        projected_points[:, 1] = projected_points[:, 1] * self.beta *self.focal_length + self.principal_point[1]

        return projected_points
