import pygame
import numpy as np


class camera :
    def __init__(self, position, df ,alpha,beta,translation_vector,matrice_de_rotation , mash):
        self.position = np.array(position)  
        self.focal_de_camera = df
        self.alpha = alpha
        self.beta = beta
        self.translation_vector = translation_vector
        self.matrice_de_rotation=matrice_de_rotation

        self.matrice_des_paramètres_intrinsèques= self.calculer_de_K()
        self.matrice_des_paramètres_extrinsiques = self.calculer_de_RS()
        self.mash = mash
    def calculer_de_K(self):
        
        fALPHA = self.focal_de_camera * self.alpha
        fBETA = self.focal_de_camera * self.beta
        u0, v0 = self.position
        
        K = np.array([
            [fALPHA, 0, u0],
            [0, fBETA, v0],
            [0, 0, 1]
        ])
        return K
    def calculer_de_RS(self):
        RS =np.hstack((self.matrice_de_rotation, self.translation_vector))
        return RS
    def matrice_de_projection (self):
        p=np.dot(self.matrice_des_paramètres_intrinsèques, self.matrice_des_paramètres_extrinsiques)
 
        return p
       
    
