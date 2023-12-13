
from lib.Ray import Ray
from lib.HitRecord import HitRecord
from lib.Interval import Interval


class Hittable:
    '''
    Classe base para objetos que podem ser atingidos por raios.
    
    Basicamente, define que a classe filha precisa implementar o método hit
    '''

    def hit(self, ray: Ray, t_interval: Interval) -> "tuple[bool, HitRecord]":
        '''
        Dado um raio e um intervalo de t, será verificado se o raio atinge o objeto.

        ---

        Parâmetros:

            - ray: Ray - Raio que será verificado se atinge o objeto.

            - t_interval: Interval - Intervalo de t que será verificado se o raio atinge o objeto. Se o raio atingir o objeto em um t que não está dentro do intervalo, então, o objeto não foi atingido.

        ---

        Retorno:

            Se o raio atingiu o objeto, então, será retornado uma tupla contendo True e um HitRecord com as informações da intersecção.
            Caso contrário, será retornado uma tupla contendo False e None.
        '''
        raise NotImplementedError('Esse método método deve ser implementado na classe filha.')