class mesh :
    def __init__(self, filename):
        self.filename = filename
        self.vertices = []
        self.faces = []
        self.Vertex_Texture =[]
        self.Vertex_Normal = []
    def open_3Dobject (self):
        with open(self.filename) as file:
            for line in file:
                if line.startswith("v "):
                    vertex = list(map(float, line.strip().split()[1:4]))
                    self.vertices.append(vertex)
                elif line.startswith("f "):
                    vertex = list(map(float, line.strip().split()[1:4]))
                    self.faces.append(vertex) 
                elif line.startswith("vt "):
                    vertex = list(map(float, line.strip().split()[1:4]))
                    self.Vertex_Texture.append(vertex)
                elif line.startswith("vn "):
                    vertex = list(map(float, line.strip().split()[1:4]))
                    self.Vertex_Texture.append(vertex)

        return  