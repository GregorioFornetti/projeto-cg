from lib.vec.Vec3 import Point3, Vec3

class Ray:

    def __init__(self, origin: Point3, direction: Vec3):
        '''
        Construtor de um raio (Ray).

        ---

        Parâmetros:

            - origin: Point3 - Ponto de origem do raio.

            - direction: Vec3 - Vetor que indica a direção do raio.
        '''
        self.__origin = origin
        self.__direction = direction
    
    @property
    def origin(self) -> Point3:
        '''
        Ponto de origem do raio.
        '''
        return self.__origin
    
    @property
    def direction(self) -> Vec3:
        '''
        Vetor que indica a direção do raio.
        '''
        return self.__direction

    def at(self, t: float) -> Point3:
        '''
        Retorna o ponto em que o raio para no tempo t.
        '''
        return self.origin + t * self.direction