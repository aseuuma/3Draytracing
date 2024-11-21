import numpy as np 

class Mesh:
    def __init__(self, file_path):
        # Read and parse the .obj file to extract vertices
        self.vertices , self.faces = self.open_3D_object(file_path)

    def open_3D_object(self, file_path):
        vertices = []
        faces = []

        with open ( file_path, 'r') as file:
            for line in file:
                if line.startswith('v '):
                    # Read vertex positions
                    parts = line.strip().split()
                    print(parts)
                    vertices.append([float(parts[1]), float(parts[2]), float(parts[3])])
                elif line.startswith('f '):
                    # Read face definitions
                    parts = line.strip().split()
                    print(parts)
                    face = [int(p.split('/')[0]) - 1 for p in parts[1:]]
                    print(face)
                    faces.append(face)

        return np.array(vertices), faces

  
