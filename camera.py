import numpy as np

class Camera:
    def __init__(self, focal_length, alpha, beta, principal_point, rotation_matrix, translation_vector, mesh, width, height):
        self.focal_length = focal_length
        self.alpha = alpha
        self.beta = beta
        self.principal_point = np.array(principal_point)
        self.rotation_matrix = np.array(rotation_matrix)
        self.translation_vector = np.array(translation_vector).reshape(-1, 1)
        self.mesh = mesh
        self.width = width
        self.height = height

        self.intrinsic_matrix = self.compute_intrinsic_matrix()
        self.extrinsic_matrix = self.compute_extrinsic_matrix()
        self.projection_matrix = self.compute_projection_matrix()

    def compute_intrinsic_matrix(self):
        falpha = self.focal_length * self.alpha
        fbeta = self.focal_length * self.beta
        u0, v0 , F = self.principal_point
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


    def project_points_3d(self):
        points = np.array(self.mesh.vertices)
        points_3d = np.hstack((points, np.ones((points.shape[0], 1))))
        points_2d = np.dot(self.projection_matrix, points_3d.T).T
        return points_2d[:, :2] / points_2d[:, 2, np.newaxis]
