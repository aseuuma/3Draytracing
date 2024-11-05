import pygame
import numpy as np


class camera :
    def __init__(self, position, df ,alpha,beta):
        self.position = np.array(position)  
        self.focal_de_camera = df
        self.alpha = alpha
        self.beta = beta



        self.intrinsic_matrix = self.calculer_de_K()
       

    def calculer_de_K(self):
        
        fALPHA = self.focal_de_camera * self.alpha
        fBETA = self.focal_de_camera * self.beta
        u0, v0 = self.principal_point
        
        K = np.array([
            [fALPHA, 0, u0],
            [0, fBETA, v0],
            [0, 0, 1]
        ])
        return K
    

       
    
