
from lib.vec.Vec3 import Point3
from lib.objects.Hittable import Hittable
from lib.Ray import Ray
from lib.HitRecord import HitRecord
from lib.Interval import Interval
from lib.materials.Material import Material

import numpy as np


class Sphere(Hittable):

    def __init__(self, center: Point3, radius: float, material: Material):
        '''
        Construtor de uma esfera.
        
        ---

        Parâmetros:

            - center: Point3 - Centro da esfera.

            - radius: float - Raio da esfera.
        '''
        self.__material = material
        self.__center = center
        self.__radius = radius
    
    @property
    def center(self):
        '''
        Centro da esfera.
        '''
        return self.__center
    
    @property
    def radius(self):
        '''
        Raio da esfera.
        '''
        return self.__radius

    def hit(self, ray: Ray, t_interval: Interval) -> "tuple[bool, HitRecord]":
        '''
        Verifica se um raio atinge a esfera.

        ---

        Parâmetros:

            - ray: Ray - Raio a ser verificado.

            - t_interval: Interval - Intervalo de t em que o raio pode atingir a esfera.
        
        ---

        Retorno:

            - tuple[bool, HitRecord] - Tupla contendo um booleano que indica se o raio atingiu a esfera e um registro de acerto (hit record) com informações sobre o acerto. Caso o raio não atinja a esfera, o registro de acerto é None.
        '''
        oc = ray.origin - self.center
        a = ray.direction.squared_length()
        half_b = oc.dot(ray.direction)
        c = oc.dot(oc) - self.radius ** 2

        discriminant = half_b ** 2 - a * c

        if discriminant < 0:
            return False, None
        else:
            root = np.sqrt(discriminant)
            t = (-half_b - root) / a
            if t not in t_interval:
                t = (-half_b + root) / a
                if t not in t_interval:
                    return False, None
            
            p = ray.at(t)
            normal = (p - self.center) / self.radius
            return True, HitRecord(p, normal, t, ray, self.__material)