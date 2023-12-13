import numpy as np

from lib.vec.Vec3 import Vec3, Color
from lib.Ray import Ray
from lib.HitRecord import HitRecord
from lib.utils import random_double
from lib.materials.Material import Material

class Dielectric(Material):
    
    def __init__(self, ir: float):
        self.ir = ir
    
    def scatter(self, ray: Ray, rec: HitRecord) -> 'tuple[bool, Ray, Color]':
        attenuation = Color([1.0, 1.0, 1.0])
        refraction_ratio = 1.0 / self.ir if rec.front_face else self.ir

        unit_direction = ray.direction.unit_vector()
        cos_theta = min((-unit_direction).dot(rec.normal), 1.0)
        sin_theta = np.sqrt(1.0 - cos_theta ** 2)

        cannot_refract = refraction_ratio * sin_theta > 1.0
        if cannot_refract or self.reflectance(cos_theta, refraction_ratio) > random_double():
            direction = Vec3.reflect(unit_direction, rec.normal)
        else:
            direction = Vec3.refract(unit_direction, rec.normal, refraction_ratio)

        scattered = Ray(rec.p, direction)
        return True, scattered, attenuation
    
    @staticmethod
    def reflectance(cosine: float, ref_idx: float) -> float:
        r0 = (1 - ref_idx) / (1 + ref_idx)
        r0 = r0 ** 2
        return r0 + (1 - r0) * (1 - cosine) ** 5