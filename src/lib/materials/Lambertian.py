
from lib.vec.Vec3 import Vec3, Color
from lib.Ray import Ray
from lib.HitRecord import HitRecord
from lib.materials.Material import Material


class Lambertian(Material):

    def __init__(self, albedo: Color):
        self.albedo = albedo
    
    def scatter(self, ray: Ray, rec: HitRecord) -> 'tuple[bool, Ray, Color]':
        direction: Vec3 = rec.normal + Vec3.random_unit_vector()
        if direction.near_zero():
            direction = rec.normal
        
        scattered = Ray(rec.p, direction)
        attenuation = self.albedo
        return True, scattered, attenuation