
from typing import Union

from lib.vec.Vec3 import Point3, Vec3
from lib.objects.Hittable import Hittable
from lib.Ray import Ray
from lib.HitRecord import HitRecord
from lib.Interval import Interval
from lib.materials.Material import Material

import numpy as np


def barycentric(point1: Point3, point2: Point3, point3: Point3, intersect_point: Point3):
    '''
    Calcula as coordenadas baricêntricas de um ponto em relação a um triângulo.

    ---

    Parâmetros:

        - point1: Point3 - Primeiro vértice do triângulo.

        - point2: Point3 - Segundo vértice do triângulo.

        - point3: Point3 - Terceiro vértice do triângulo.
        
        - intersect_point: Point3 - Ponto a ser calculado as coordenadas baricêntricas.
    
    ---

    Retorno:

        - tuple[float, float, float] - Tupla contendo as coordenadas baricêntricas do ponto.
    '''

    # https://ceng2.ktu.edu.tr/~cakir/files/grafikler/Texture_Mapping.pdf
    
    v0 = point2 - point1
    v1 = point3 - point1
    v2 = intersect_point - point1

    d00 = v0.dot(v0)
    d01 = v0.dot(v1)
    d11 = v1.dot(v1)
    d20 = v2.dot(v0)
    d21 = v2.dot(v1)

    denom = d00 * d11 - d01 * d01

    v = (d11 * d20 - d01 * d21) / denom
    w = (d00 * d21 - d01 * d20) / denom
    u = 1.0 - v - w

    return u, v, w


class Triangle(Hittable):

    def __init__(self, vertex_1: Point3, vertex_2: Point3, vertex_3: Point3, material: Material, normals: 'list[Point3, Point3, Point3]' = None):
        '''
        Construtor de um triângulo.

        ---

        Parâmetros:

            - vertex_1: Point3 - Primeiro vértice do triângulo.

            - vertex_2: Point3 - Segundo vértice do triângulo.

            - vertex_3: Point3 - Terceiro vértice do triângulo.

            - material: Material - Material do triângulo.

            - normals: tuple[Point3, Point3, Point3] - Tupla contendo as normais de cada vértice do triângulo. Caso não seja especificado, as normais serão calculadas automaticamente.
        '''
        self.__material = material
        self.__vertexes = np.array([vertex_1, vertex_2, vertex_3])
        
        if normals is not None:
            for i in range(len(normals)):
                normals[i] = normals[i].unit_vector()
            self.__normals = np.array(normals)
        else:
            self.__normals = None
    
    @property
    def vertexes(self) -> np.ndarray:
        '''
        Retorna um array contendo os vértices do triângulo.
        '''
        return self.__vertexes
    
    @property
    def vertex_1(self) -> Point3:
        '''
        Retorna o primeiro vértice do triângulo.
        '''
        return self.__vertexes[0]
    
    @property
    def vertex_2(self) -> Point3:
        '''
        Retorna o segundo vértice do triângulo.
        '''
        return self.__vertexes[1]
    
    @property
    def vertex_3(self) -> Point3:
        '''
        Retorna o terceiro vértice do triângulo.
        '''
        return self.__vertexes[2]
    
    @property
    def normals(self) -> Union[np.ndarray, None]:
        '''
        Retorna um array contendo as normais de cada vértice do triângulo.
        '''
        return self.__normals
    
    @property
    def normal_1(self) -> Union[Point3, None]:
        '''
        Retorna a normal do primeiro vértice do triângulo.
        '''
        return self.__normals[0] if self.__normals is not None else None
    
    @property
    def normal_2(self) -> Union[Point3, None]:
        '''
        Retorna a normal do segundo vértice do triângulo.
        '''
        return self.__normals[1] if self.__normals is not None else None
    
    @property
    def normal_3(self) -> Union[Point3, None]:
        '''
        Retorna a normal do terceiro vértice do triângulo.
        '''
        return self.__normals[2] if self.__normals is not None else None
    
    def __getitem__(self, index) -> Point3:
        '''
        Retorna o vértice especificado.

        0 = primeiro vértice, 1 = segundo vértice, 2 = terceiro vértice.
        '''
        return self.__vertexes[index]

    def hit(self, ray: Ray, t_interval: Interval) -> "tuple[bool, HitRecord]":
        '''
        Verifica se um raio atinge a triângulo.

        ---

        Parâmetros:

            - ray: Ray - Raio a ser verificado.

            - t_interval: Interval - Intervalo de t em que o raio pode atingir a triângulo.
        
        ---

        Retorno:

            - tuple[bool, HitRecord] - Tupla contendo um booleano que indica se o raio atingiu a triângulo e um registro de acerto (hit record) com informações sobre o acerto. Caso o raio não atinja a triângulo, o registro de acerto é None.
        '''
        # Descobrindo o vetor normal
        v1_to_v2 = self.vertex_2 - self.vertex_1
        v1_to_v3 = self.vertex_3 - self.vertex_1
        normal = v1_to_v2.cross(v1_to_v3)

        # Descobrindo o valor P: intersecção do raio com o plano formado pelo triângulo
        normal_dot_ray_dir = normal.dot(ray.direction)
        if normal_dot_ray_dir == 0:
            return False, None  # O raio é paralelo ao plano
        
        d = -normal.dot(self.vertex_1)
        t = -(normal.dot(ray.origin) + d) / normal_dot_ray_dir

        if t not in t_interval:
            return False, None  # O triângulo está atrás do raio
        
        intersect_point = ray.at(t)

        # Verificando se o ponto de intersecção está dentro ou fora do triângulo
        # Todo lugar que retornar False, quer dizer que o ponto está à direita da aresta, logo, fora do triângulo
        # Só estará dentro do triângulo se para todas as arestas, o ponto estiver para esquerda
        edge_1 = self.vertex_2 - self.vertex_1
        vp1= intersect_point - self.vertex_1
        c = edge_1.cross(vp1)
        if normal.dot(c) < 0:
            return False, None
        
        edge_2 = self.vertex_3 - self.vertex_2
        vp2= intersect_point - self.vertex_2
        c = edge_2.cross(vp2)
        if normal.dot(c) < 0:
            return False, None

        edge_3 = self.vertex_1 - self.vertex_3
        vp3= intersect_point - self.vertex_3
        c = edge_3.cross(vp3)
        if normal.dot(c) < 0:
            return False, None
        
        if self.__normals is None:
            return True, HitRecord(intersect_point, normal, t, ray, self.__material)
        else:
            # Calculando as coordenadas baricêntricas
            w1, w2, w3 = barycentric(self.vertex_1, self.vertex_2, self.vertex_3, intersect_point)
            normal = w1 * self.normal_1 + w2 * self.normal_2 + w3 * self.normal_3
            normal = normal.unit_vector()

            return True, HitRecord(intersect_point, normal, t, ray, self.__material)
    
    def scale(self, factor: float):
        '''
        Escala o triângulo.

        ---

        Parâmetros:

            - factor: float - Fator de escala.
        '''
        for i in range(len(self.__vertexes)):
            self.__vertexes[i] *= factor
    
    def translate(self, offset: Vec3):
        '''
        Translada o triângulo.

        ---

        Parâmetros:

            - offset: Vec3 - Vetor de translação.
        '''
        for i in range(len(self.__vertexes)):
            self.__vertexes[i] += offset