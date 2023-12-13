
from lib.vec.Vec3 import Color
from lib.Ray import Ray

class Material:
    def scatter(self, ray: Ray, rec) -> 'tuple[bool, Ray, Color]':
        raise NotImplementedError