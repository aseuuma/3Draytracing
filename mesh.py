import numpy as np
class Mesh:
    def __init__(self, filename):
        self.filename = filename
        self.vertices = []
        self.faces = []
        self.VN = []
        self.VT=[]
    
    def open_3D_object(self):
        with open(self.filename) as file:
            for line in file:
                if line.startswith("v "):
                    vertex = list(map(float, line.strip().split()[1:4]))
                    self.vertices.append(vertex)
                elif line.startswith("f "):
                    face = line.strip().split()[1:]  # Skip the 'f' part
                    vertex_indices = [int(v.split('/')[0]) - 1 for v in face]  # Convert to zero-based index
                    self.faces.append(vertex_indices)
                elif line.startswith("vt "):
                    vertex = list(map(float, line.strip().split()[1:4]))
                    self.VT.append(vertex)
                elif line.startswith("vn "):
                    vertex = list(map(float, line.strip().split()[1:4]))
                    self.VN.append(vertex)
