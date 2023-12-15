
from lib.vec.Vec3 import Color
from lib.Ray import Ray

class Material:
    def scatter(self, ray: Ray, rec) -> 'tuple[bool, Ray, Color]':
        '''
        Gera um raio novo (possivelmente) a partir do raio que atingiu o objeto.

        ---

        Parâmetros:

            - ray: Ray - Raio que atingiu o objeto.

            - rec: HitRecord - Informações do objeto atingido.
        
        ---

        Retorno:

            - tuple[bool, Ray, Color] - Tupla contendo se o raio foi espalhado, o raio espalhado e a cor do raio espalhado.
        '''
        raise NotImplementedError