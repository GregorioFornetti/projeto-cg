
from lib.vec.Vec3 import Vec3, Color
from lib.Ray import Ray
from lib.HitRecord import HitRecord
from lib.materials.Material import Material

class Metal(Material):
    
    def __init__(self, albedo: Color, fuzz: float = 0.0):
        '''
        Construtor da classe Metal (metálico/reflexivo).

        ---

        Parâmetros:

            - albedo: Color - Cor do objeto.

            - fuzz: float - Grau de reflexividade do objeto. Quanto maior, mais difuso (aleatório).
        '''
        self.albedo = albedo
        self.fuzz = fuzz if fuzz < 1 else 1
    
    def scatter(self, ray: Ray, rec: HitRecord) -> 'tuple[bool, Ray, Color]':
        '''
        Gera um novo raio a partir do raio que atingiu o objeto. O raio novo é a reflexão do raio sobre a superfície do objeto. Se fuzz > 0, o refletido não será perfeito, terá um fator aleatório somado à ele (quão maior o fuzz, mais aleatório).

        ---

        Parâmetros:

            - ray: Ray - Raio que atingiu o objeto.

            - rec: HitRecord - Informações do objeto atingido.

        ---

        Retorno:

            - tuple[bool, Ray, Color] - Tupla contendo se o raio foi espalhado, o raio espalhado e a cor do raio espalhado.
        '''
        reflected = Vec3.reflect(ray.direction.unit_vector(), rec.normal)
        scattered = Ray(rec.p, reflected + self.fuzz * Vec3.random_in_unit_sphere())
        attenuation = self.albedo
        return scattered.direction.dot(rec.normal) > 0, scattered, attenuation