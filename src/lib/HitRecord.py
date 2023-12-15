
from lib.vec.Vec3 import Vec3, Point3
from lib.Ray import Ray
from lib.materials.Material import Material


class HitRecord:

    def __init__(self, p: Point3, normal: Vec3, t: float, ray: Ray, material: Material):
        '''
        Construtor de um registro de acerto (hit).

        ---

        Parâmetros:

            - p: Point3 - Ponto de acerto.

            - normal: Vec3 - Vetor normal do ponto de acerto.

            - t: float - Tempo t do raio no ponto de acerto.

            - ray: Ray - Raio que utilizado

            - material: Material - Material do objeto que foi acertado.
        '''
        self.__material = material
        self.__p = p
        self.__t = t
        self.set_normal(normal, ray)
    
    def set_normal(self, outward_normal: Vec3, ray: Ray):
        '''
        Define o vetor normal do ponto de acerto. Isso depende da direção do raio e da normal do objeto.
        
        Se a normal do objeto aponta para a mesma direção do raio, então o raio está do outro lado da face (lado interno). Logo, a normal deve ser invertida.

        Isso é chamado no construtor automaticamente, para definir a normal e o booleano de front face.
        '''
        self.__front_face = ray.direction.dot(outward_normal) < 0
        self.__normal = outward_normal if self.front_face else -outward_normal
    
    @property
    def p(self):
        '''
        Ponto em que o raio acertou algum objeto.
        '''
        return self.__p
    
    @property
    def normal(self):
        '''
        Vetor normal do ponto de acerto.
        '''
        return self.__normal
    
    @property
    def t(self):
        '''
        Tempo t do raio no ponto de acerto.
        '''
        return self.__t
    
    @property
    def front_face(self):
        '''
        Booleano que indica se o raio acertou o objeto pela frente ou por trás.

        Se for verdadeiro (True), o raio acertou o objeto pela frente. Se for falso (False), o raio acertou o objeto por trás.
        '''
        return self.__front_face
    
    @property
    def material(self):
        '''
        Material do objeto que foi acertado.
        '''
        return self.__material