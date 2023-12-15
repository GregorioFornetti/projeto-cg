
from typing import Union

from lib.objects.Hittable import Hittable
from lib.Ray import Ray
from lib.HitRecord import HitRecord
from lib.Interval import Interval
from lib.objects.Model import Model


class HittableList:
    
    def __init__(self):
        '''
        Construtor de uma lista de objetos que podem ser atingidos por um raio.
        Um objeto desta classe representa o mundo ou uma cena.
        '''
        self.objects: list[Hittable] = []
    
    def add(self, obj: Union[Hittable, Model]):
        '''
        Adiciona um objeto à lista de objetos que podem ser atingidos por um raio.

        ---

        Parâmetros:

            - obj: Hittable - Objeto a ser adicionado.
        '''
        if isinstance(obj, Model):
            for face in obj.faces:
                self.objects.append(face)
        else:
            self.objects.append(obj)
    
    def clear(self):
        '''
        Limpa (esvazia) a lista de objetos que podem ser atingidos por um raio.
        '''
        self.objects.clear()
    
    def hit(self, ray: Ray, interval: Interval) -> "tuple[bool, HitRecord]":
        '''
        Verifica se um raio atinge algum objeto da lista de objetos que podem ser atingidos por um raio.

        ---

        Parâmetros:

            - ray: Ray - Raio a ser verificado.

            - interval: Interval - Intervalo de t em que o raio pode atingir algum objeto.
        
        ---

        Retorno:

            - tuple[bool, HitRecord] - Tupla contendo um booleano que indica se o raio atingiu algum objeto e um registro de acerto (hit record) com informações sobre o acerto. Caso o raio não atinja nenhum objeto, o registro de acerto é None.
        '''
        hit_anything = False
        closest_so_far = interval.max
        for obj in self.objects:
            hit, rec = obj.hit(ray, Interval(interval.min, closest_so_far))
            if hit:
                hit_anything = True
                closest_so_far = rec.t
                hit_record = rec
        
        if hit_anything:
            return True, hit_record
        else:
            return False, None