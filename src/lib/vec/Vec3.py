
from typing import Union
import numpy as np
from lib.vec.Vec import Vec
from lib.utils import random_double_range


class Vec3(Vec):
    """
    .. automethod:: __neg__
    .. automethod:: __getitem__
    .. automethod:: __add__
    .. automethod:: __sub__
    .. automethod:: __mul__
    .. automethod:: __truediv__
    .. automethod:: __iadd__
    .. automethod:: __isub__
    .. automethod:: __imul__
    .. automethod:: __itruediv__
    .. automethod:: __repr__
    
    """

    def __init__(self, vector: Union[np.ndarray, list] = np.zeros((3,), dtype=np.float64)):
        '''
        Construtor da classe Vec3. Recebe as coordenadas x, y e z do vetor.

        --- 

        Parâmetros:

            - vector: Union[np.ndarray, list] - Vetor ou lista contendo as coordenadas x, y e z do vetor.
        '''
        super().__init__(vector, (3,))
    
    @property
    def x(self) -> np.float64:
        '''
        Coordenada x do vetor.
        '''
        return self.vec[0]
    
    @x.setter
    def x(self, value: np.float64):
        self.vec[0] = value
    
    @property
    def y(self) -> np.float64:
        '''
        Coordenada y do vetor.
        '''
        return self.vec[1]
    
    @y.setter
    def y(self, value: np.float64):
        self.vec[1] = value

    @property
    def z(self) -> np.float64:
        '''
        Coordenada z do vetor.
        '''
        return self.vec[2]

    @z.setter
    def z(self, value: np.float64):
        self.vec[2] = value
    

    def __neg__(self) -> 'Vec3':
        '''
        Inverte o sinal de todas as coordenadas do vetor.

        Exemplo:

        >>> v = Vec3([1, 2, 3])
        >>> print(-v)
        -1.0 -2.0 -3.0

        ---

        Retorno:

            - Vec3 - Versão negativa do vetor.
        '''
        return super().__neg__()
    
    def __getitem__(self, key: int) -> np.float64:
        '''
        Retorna a coordenada do vetor de acordo com o índice.

        Exemplo:

        >>> v = Vec3([1, 2, 3])
        >>> print(v[0])
        1.0

        ---

        Parâmetros:
            
            - key: int - Índice da coordenada do vetor (0 = x, y = 1 e z = 2).

        ---

        Retorno:
            
            - np.float64 - Valor da coordenada escolhida.
        '''
        return super().__getitem__(key)
    

    def __add__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        '''
        Soma elemento a elemento de dois vetores. Ou soma um número a cada elemento do vetor.

        Exemplo:

        Somando dois vetores

        >>> v1 = Vec3([1, 2, 3])
        >>> v2 = Vec3([4, 5, 6])
        >>> print(v1 + v2)
        5.0 7.0 9.0

        Somando um vetor e um número:

        >>> v1 = Vec3([1, 2, 3])
        >>> print(v1 + 1)
        2.0 3.0 4.0

        ---

        Parâmetros:

            - other: Union['Vec3', np.float64] - Vetor ou número a ser somado.
        
        ---

        Retorno:

            - Vec3 - Resultado da soma.

        '''
        return super().__add__(other)
    
    def __sub__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        '''
        Subtrai elemento a elemento de dois vetores. Ou subtrai um número a cada elemento do vetor.

        Exemplo:

        Subtraindo dois vetores:

        >>> v1 = Vec3([1, 2, 3])
        >>> v2 = Vec3([4, 5, 6])
        >>> print(v1 - v2)
        -3.0 -3.0 -3.0

        Subtraindo um vetor e um número:

        >>> v1 = Vec3([1, 2, 3])
        >>> print(v1 - 1)
        0.0 1.0 2.0

        ---

        Parâmetros:

            - other: Union['Vec3', np.float64] - Vetor ou número a ser subtraído.

        ---

        Retorno:
            
                - Vec3 - Resultado da subtração.
        
        '''
        return super().__sub__(other)
    
    def __mul__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        '''
        Multiplica elemento a elemento de dois vetores. Ou multiplica um número a cada elemento do vetor.

        Exemplo:

        Multiplicando dois vetores:

        >>> v1 = Vec3([1, 2, 3])
        >>> v2 = Vec3([4, 5, 6])
        >>> print(v1 * v2)
        4.0 10.0 18.0

        Multiplicando um vetor e um número:

        >>> v1 = Vec3([1, 2, 3])
        >>> print(v1 * 2)
        2.0 4.0 6.0

        ---

        Parâmetros:

            - other: Union['Vec3', np.float64] - Vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Vec3 - Resultado da multiplicação.
        '''
        return super().__mul__(other)
    
    def __truediv__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        '''
        Divide elemento a elemento de dois vetores. Ou divide um número a cada elemento do vetor.

        Exemplo:

        Dividindo dois vetores:

        >>> v1 = Vec3([1, 2, 3])
        >>> v2 = Vec3([4, 5, 6])
        >>> print(v1 / v2)
        0.25 0.4 0.5

        Dividindo um vetor e um número:

        >>> v1 = Vec3([1, 2, 3])
        >>> print(v1 / 2)
        0.5 1.0 1.5

        ---

        Parâmetros:

            - other: Union['Vec3', np.float64] - Vetor ou número a ser utilizado como divisor.

        ---

        Retorno:

            - Vec3 - Resultado da divisão.
        '''
        return super().__truediv__(other)


    def __iadd__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        '''
        Soma elemento a elemento de dois vetores. Ou soma um número a cada elemento do vetor.

        Exemplo:

        Somando dois vetores:

        >>> v1 = Vec3([1, 2, 3])
        >>> v2 = Vec3([4, 5, 6])
        >>> v1 += v2
        >>> print(v1)
        5.0 7.0 9.0

        Somando um vetor e um número:

        >>> v1 = Vec3([1, 2, 3])
        >>> v1 += 1
        >>> print(v1)
        2.0 3.0 4.0

        ---

        Parâmetros:

            - other: Union['Vec3', np.float64] - Vetor ou número a ser somado.
        
        ---

        Retorno:

            - Vec3 - Resultado da soma.
        '''
        return super().__iadd__(other)
    
    def __isub__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        '''
        Subtrai elemento a elemento de dois vetores. Ou subtrai um número a cada elemento do vetor.

        Exemplo:

        Subtraindo dois vetores:

        >>> v1 = Vec3([1, 2, 3])
        >>> v2 = Vec3([4, 5, 6])
        >>> v1 -= v2
        >>> print(v1)
        -3.0 -3.0 -3.0

        Subtraindo um vetor e um número:

        >>> v1 = Vec3([1, 2, 3])
        >>> v1 -= 1
        >>> print(v1)
        0.0 1.0 2.0

        ---

        Parâmetros:

            - other: Union['Vec3', np.float64] - Vetor ou número a ser subtraído.
        
        ---

        Retorno:

            - Vec3 - Resultado da subtração.
        '''
        return super().__isub__(other)
    
    def __imul__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        '''
        Multiplica elemento a elemento de dois vetores. Ou multiplica um número a cada elemento do vetor.

        Exemplo:

        Multiplicando dois vetores:

        >>> v1 = Vec3([1, 2, 3])
        >>> v2 = Vec3([4, 5, 6])
        >>> v1 *= v2
        >>> print(v1)
        4.0 10.0 18.0

        Multiplicando um vetor e um número:

        >>> v1 = Vec3([1, 2, 3])
        >>> v1 *= 2
        >>> print(v1)
        2.0 4.0 6.0

        ---

        Parâmetros:

            - other: Union['Vec3', np.float64] - Vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Vec3 - Resultado da multiplicação.
        '''
        return super().__imul__(other)

    def __itruediv__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        '''
        Divide elemento a elemento de dois vetores. Ou divide um número a cada elemento do vetor.

        Exemplo:

        Dividindo dois vetores:

        >>> v1 = Vec3([1, 2, 3])
        >>> v2 = Vec3([4, 5, 6])
        >>> v1 /= v2
        >>> print(v1)
        0.25 0.4 0.5

        Dividindo um vetor e um número:

        >>> v1 = Vec3([1, 2, 3])
        >>> v1 /= 2
        >>> print(v1)
        0.5 1.0 1.5

        ---

        Parâmetros:

            - other: Union['Vec3', np.float64] - Vetor ou número a ser dividido.
        
        ---

        Retorno:

            - Vec3 - Resultado da divisão.
        '''
        return super().__itruediv__(other)
    
    def __repr__(self) -> str:
        '''
        Retorna uma string representando o vetor.

        A string é composta pelas coordenadas x, y e z do vetor, separadas por um espaço.

        Exemplo:

        >>> v = Vec3([1, 2, 3])
        >>> print(v)
        1.0 2.0 3.0
        '''
        return f"{self.vec[0]} {self.vec[1]} {self.vec[2]}"
    
    
    def length(self) -> np.float64:
        '''
        Retorna o comprimento do vetor.

        Exemplo:

        >>> v = Vec3([1, 2, 3])
        >>> print(v.length())  # sqrt(1 ** 2 + 2 ** 2 + 3 ** 2)
        3.7416573867739413
        '''
        return super().length()
    
    def squared_length(self) -> np.float64:
        '''
        Retorna o comprimento do vetor ao quadrado.

        Exemplo:

        >>> v = Vec3([1, 2, 3])
        >>> print(v.squared_length())  # 1 ** 2 + 2 ** 2 + 3 ** 2
        14.0
        '''
        return super().squared_length()
    
    def dot(self, other: 'Vec3') -> np.float64:
        '''
        Retorna o produto escalar entre dois vetores.

        Exemplo:

        >>> v1 = Vec3([1, 2, 3])
        >>> v2 = Vec3([4, 5, 6])
        >>> print(v1.dot(v2))
        32.0

        ---

        Parâmetros:

            - other: 'Vec3' - Segundo vetor do produto escalar.
        
        ---

        Retorno:
            
            - np.float64 - Resultado do produto escalar.
        '''
        return super().dot(other)
    
    def cross(self, other: 'Vec3') -> 'Vec3':
        '''
        Retorna o produto vetorial entre dois vetores.

        Exemplo:

        >>> v1 = Vec3([1, 2, 3])
        >>> v2 = Vec3([4, 5, 6])
        >>> print(v1.cross(v2))
        -3.0 6.0 -3.0

        ---

        Parâmetros:

            - other: 'Vec3' - Segundo vetor do produto vetorial.
        
        ---

        Retorno:

            - Vec3 - Resultado do produto vetorial.
        '''
        if not isinstance(other, Vec3):
            raise TypeError(f"Tipo inválido para produto vetorial, esperado: Vec3, recebido: {type(other)}")
        
        return Vec3([self.vec[1] * other.vec[2] - self.vec[2] * other.vec[1],
                    self.vec[2] * other.vec[0] - self.vec[0] * other.vec[2],
                    self.vec[0] * other.vec[1] - self.vec[1] * other.vec[0]])
    
    def unit_vector(self) -> 'Vec3':
        '''
        Retorna o vetor unitário.

        Exemplo:

        >>> v = Vec3([1, 2, 3])
        >>> print(v.unit_vector())
        0.27 0.53 0.80

        ---

        Retorno:

            - Vec3 - Vetor unitário.
        '''
        return super().unit_vector()

    @staticmethod
    def random_range(min: float, max: float) -> 'Vec3':
        '''
        Retorna um vetor com coordenadas aleatórias entre min e max.

        Exemplo:

        >>> print(Vec3.random_range(0, 10))
        7.73 1.71 6.60

        ---

        Parâmetros:

            - min: float - Valor mínimo das coordenadas.
            - max: float - Valor máximo das coordenadas.
        
        ---

        Retorno:

            - Vec3 - Vetor com coordenadas aleatórias.
        '''
        return Vec3([random_double_range(min, max), random_double_range(min, max), random_double_range(min, max)])
    
    # Não entendi o motivo de ficar sorteando várias vezes, pq não só sortear um e depois fazer o unitário (e talvez dividir ?)
    # Talvez seja para não enviesar a probalidade (aumentando a probabilidade) de sair um vetor unitário em direção a um
    # do cantos do cubo, já que a probabilidade disso acontecer é maior.
    @staticmethod
    def random_in_unit_sphere() -> 'Vec3':
        '''
        Retorna um vetor aleatório dentro da esfera unitária.

        Exemplo:

        >>> print(Vec3.random_in_unit_sphere())
        0.73 0.71 0.60

        ---

        Retorno:

            - Vec3 - Vetor aleatório dentro da esfera unitária.
        '''
        while True:
            p = Vec3.random_range(-1, 1)
            if p.squared_length() >= 1:
                continue
            return p

    @staticmethod
    def random_unit_vector() -> 'Vec3':
        '''
        Retorna um vetor aleatório unitário.

        Exemplo:

        >>> print(Vec3.random_unit_vector())
        0.73 0.71 0.60

        ---

        Retorno:

            - Vec3 - Vetor aleatório unitário.
        '''
        return Vec3.random_in_unit_sphere().unit_vector()
    
    @staticmethod
    def random_on_hemisphere(normal: 'Vec3') -> 'Vec3':
        '''
        Retorna um vetor aleatório na hemisfério do vetor normal.

        Exemplo:

        >>> print(Vec3.random_on_hemisphere(Vec3([0, 1, 0])))
        0.73 0.71 0.60

        ---

        Parâmetros:

            - normal: 'Vec3' - Vetor normal.
        
        ---

        Retorno:

            - Vec3 - Vetor aleatório na hemisfério do vetor normal.
        '''
        in_unit_sphere = Vec3.random_in_unit_sphere()
        if in_unit_sphere.dot(normal) > 0.0:
            return in_unit_sphere
        else:
            return -in_unit_sphere
    
    def near_zero(self) -> bool:
        '''
        Retorna Verdadeiro se todos os elementos (x,y,z) do vetor são próximos de zero.
        
        ---

        Retorno:

            - bool - Se o vetor é próximo de zero.
        '''
        s = 1e-8
        return (abs(self.vec[0]) < s) and (abs(self.vec[1]) < s) and (abs(self.vec[2]) < s)
    
    @staticmethod
    def reflect(v: 'Vec3', n: 'Vec3') -> 'Vec3':
        '''
        Retorna o vetor refletido.

        Exemplo:

        >>> print(Vec3.reflect(Vec3([1, 2, 3]), Vec3([0, 1, 0])))
        1.00 -2.00 3.00

        ---

        Parâmetros:

            - v: 'Vec3' - Vetor a ser refletido.
            
            - n: 'Vec3' - Vetor normal.
        
        ---

        Retorno:

            - Vec3 - Vetor refletido.
        '''
        return v - 2 * v.dot(n) * n

    @staticmethod
    def refract(uv: 'Vec3', n: 'Vec3', etai_over_etat: np.float64) -> 'Vec3':
        '''
        Retorna o vetor refratado.

        ---

        Parâmetros:

            - uv: 'Vec3' - Vetor a ser refratado.
            
            - n: 'Vec3' - Vetor normal.
            
            - etai_over_etat: np.float64 - Índice de refração.
        
        ---

        Retorno:

            - Vec3 - Vetor refratado.
        '''
        cos_theta = min((-uv).dot(n), 1.0)
        r_out_perp = etai_over_etat * (uv + cos_theta * n)
        r_out_parallel = -np.sqrt(abs(1.0 - r_out_perp.squared_length())) * n
        return r_out_perp + r_out_parallel

Point3 = Vec3

class Color(Vec3):

    @property
    def r(self) -> np.float64:
        return self.vec[0]
    
    @property
    def g(self) -> np.float64:
        return self.vec[1]
    
    @property
    def b(self) -> np.float64:
        return self.vec[2]

    def __repr__(self):
        return f"{int(255.999 * self.vec[0])} {int(255.999 * self.vec[1])} {int(255.999 * self.vec[2])}"