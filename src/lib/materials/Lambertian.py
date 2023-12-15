
from lib.vec.Vec3 import Vec3, Color
from lib.Ray import Ray
from lib.HitRecord import HitRecord
from lib.materials.Material import Material


class Lambertian(Material):

    def __init__(self, albedo: Color):
        '''
        Construtor da classe Lambertian (difuso).

        ---

        Parâmetros:

            - albedo: Color - Cor do objeto.
        
        '''
        self.albedo = albedo
    
    def scatter(self, ray: Ray, rec: HitRecord) -> 'tuple[bool, Ray, Color]':
        '''
        Gera um novo raio a partir do raio que atingiu o objeto. O raio novo é gerado de forma aleatória, mas raios mais próximos da normal do objeto atingido são mais prováveis.

        ---

        Parâmetros:

            - ray: Ray - Raio que atingiu o objeto.

            - rec: HitRecord - Informações do objeto atingido.

        ---

        Retorno:

            - tuple[bool, Ray, Color] - Tupla contendo se o raio foi espalhado, o raio espalhado e a cor do raio espalhado.
        '''
        direction: Vec3 = rec.normal + Vec3.random_unit_vector()
        if direction.near_zero():
            direction = rec.normal
        
        scattered = Ray(rec.p, direction)
        attenuation = self.albedo
        return True, scattered, attenuation