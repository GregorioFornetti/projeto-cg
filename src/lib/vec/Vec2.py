
from typing import Union
import numpy as np
from lib.vec.Vec import Vec


class Vec2(Vec):
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

    def __init__(self, vector: Union[np.ndarray, list] = np.zeros((2,), dtype=np.float64)):
        '''
        Construtor da classe Vec2. Recebe as coordenadas x e y.

        --- 

        Parâmetros:

            - vector: Union[np.ndarray, list] - Lista ou array com as coordenadas x e y do vetor.
        '''
        super().__init__(vector, (2,))
    
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
    

    def __neg__(self) -> 'Vec2':
        '''
        Inverte o sinal de todas as coordenadas do vetor.

        Exemplo:

        >>> v = Vec2([1, 2])
        >>> print(-v)
        -1.0 -2.0

        ---

        Retorno:

            - Vec2 - Versão com sinais invertidos do vetor.
        '''
        return super().__neg__()
    
    def __getitem__(self, key: int) -> np.float64:
        '''
        Retorna a coordenada do vetor de acordo com o índice.

        Exemplo:

        >>> v = Vec2([1, 2])
        >>> print(v[0])
        1.0

        ---

        Parâmetros:
            
            - key: int - Índice da coordenada do vetor (0 = x e y = 1).

        ---

        Retorno:
            
            - np.float64 - Valor da coordenada escolhida.
        '''
        return super().__getitem__(key)
    

    def __add__(self, other: Union['Vec2', np.float64]) -> 'Vec2':
        '''
        Soma elemento a elemento de dois vetores. Ou soma um número a cada elemento do vetor.

        Exemplo:

        Somando dois vetores

        >>> v1 = Vec2([1, 2])
        >>> v2 = Vec2([3, 4])
        >>> print(v1 + v2)
        4.0 6.0

        Somando um vetor e um número:

        >>> v1 = Vec2(1, 2)
        >>> print(v1 + 1)
        2.0 3.0

        ---

        Parâmetros:

            - other: Union['Vec2', np.float64] - Vetor ou número a ser somado.
        
        ---

        Retorno:

            - Vec2 - Resultado da soma.

        '''
        return super().__add__(other)
    
    def __sub__(self, other: Union['Vec2', np.float64]) -> 'Vec2':
        '''
        Subtrai elemento a elemento de dois vetores. Ou subtrai um número a cada elemento do vetor.

        Exemplo:

        Subtraindo dois vetores:

        >>> v1 = Vec2([1, 2])
        >>> v2 = Vec2([3, 4])
        >>> print(v1 - v2)
        -2.0 -2.0

        Subtraindo um vetor e um número:

        >>> v1 = Vec2([1, 2])
        >>> print([v1 - 1])
        0.0 1.0

        ---

        Parâmetros:

            - other: Union['Vec2', np.float64] - Vetor ou número a ser subtraído.

        ---

        Retorno:
            
                - Vec2 - Resultado da subtração.
        
        '''
        return super().__sub__(other)
    
    def __mul__(self, other: Union['Vec2', np.float64]) -> 'Vec2':
        '''
        Multiplica elemento a elemento de dois vetores. Ou multiplica um número a cada elemento do vetor.

        Exemplo:

        Multiplicando dois vetores:

        >>> v1 = Vec2([1, 2])
        >>> v2 = Vec2([3, 4])
        >>> print(v1 * v2)
        3.0 8.0

        Multiplicando um vetor e um número:

        >>> v1 = Vec2([1, 2])
        >>> print(v1 * 2)
        2.0 4.0

        ---

        Parâmetros:

            - other: Union['Vec2', np.float64] - Vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Vec2 - Resultado da multiplicação.
        '''
        return super().__mul__(other)
    
    def __truediv__(self, other: Union['Vec2', np.float64]) -> 'Vec2':
        '''
        Divide elemento a elemento de dois vetores. Ou divide um número a cada elemento do vetor.

        Exemplo:

        Dividindo dois vetores:

        >>> v1 = Vec2([1, 2])
        >>> v2 = Vec2([3, 4])
        >>> print(v1 / v2)
        0.33 0.50

        Dividindo um vetor e um número:

        >>> v1 = Vec2([1, 2])
        >>> print(v1 / 2)
        0.5 1.0

        ---

        Parâmetros:

            - other: Union['Vec2', np.float64] - Vetor ou número a ser utilizado como divisor.

        ---

        Retorno:

            - Vec2 - Resultado da divisão.
        '''
        return super().__truediv__(other)


    def __iadd__(self, other: Union['Vec2', np.float64]) -> 'Vec2':
        '''
        Soma elemento a elemento de dois vetores. Ou soma um número a cada elemento do vetor.

        Exemplo:

        Somando dois vetores:

        >>> v1 = Vec2([1, 2])
        >>> v2 = Vec2([3, 4])
        >>> v1 += v2
        >>> print(v1)
        4.0 6.0

        Somando um vetor e um número:

        >>> v1 = Vec2([1, 2])
        >>> v1 += 1
        >>> print(v1)
        2.0 3.0

        ---

        Parâmetros:

            - other: Union['Vec2', np.float64] - Vetor ou número a ser somado.
        
        ---

        Retorno:

            - Vec2 - Resultado da soma.
        '''
        return super().__iadd__(other)
    
    def __isub__(self, other: Union['Vec2', np.float64]) -> 'Vec2':
        '''
        Subtrai elemento a elemento de dois vetores. Ou subtrai um número a cada elemento do vetor.

        Exemplo:

        Subtraindo dois vetores:

        >>> v1 = Vec2([1, 2])
        >>> v2 = Vec2([3, 4])
        >>> v1 -= v2
        >>> print(v1)
        -2.0 -2.0

        Subtraindo um vetor e um número:

        >>> v1 = Vec2([1, 2])
        >>> v1 -= 1
        >>> print(v1)
        0.0 1.0

        ---

        Parâmetros:

            - other: Union['Vec2', np.float64] - Vetor ou número a ser subtraído.
        
        ---

        Retorno:

            - Vec2 - Resultado da subtração.
        '''
        return super().__isub__(other)
    
    def __imul__(self, other: Union['Vec2', np.float64]) -> 'Vec2':
        '''
        Multiplica elemento a elemento de dois vetores. Ou multiplica um número a cada elemento do vetor.

        Exemplo:

        Multiplicando dois vetores:

        >>> v1 = Vec2([1, 2])
        >>> v2 = Vec2([3, 4])
        >>> v1 *= v2
        >>> print(v1)
        3.0 8.0

        Multiplicando um vetor e um número:

        >>> v1 = Vec2([1, 2])
        >>> v1 *= 2
        >>> print(v1)
        2.0 4.0

        ---

        Parâmetros:

            - other: Union['Vec2', np.float64] - Vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Vec2 - Resultado da multiplicação.
        '''
        return super().__imul__(other)

    def __itruediv__(self, other: Union['Vec2', np.float64]) -> 'Vec2':
        '''
        Divide elemento a elemento de dois vetores. Ou divide um número a cada elemento do vetor.

        Exemplo:

        Dividindo dois vetores:

        >>> v1 = Vec2([1, 2])
        >>> v2 = Vec2([3, 4])
        >>> v1 /= v2
        >>> print(v1)
        0.33 0.50

        Dividindo um vetor e um número:

        >>> v1 = Vec2([1, 2])
        >>> v1 /= 2
        >>> print(v1)
        0.5 1.0

        ---

        Parâmetros:

            - other: Union['Vec2', np.float64] - Vetor ou número a ser dividido.
        
        ---

        Retorno:

            - Vec2 - Resultado da divisão.
        '''
        return super().__itruediv__(other)
    
    def __repr__(self) -> str:
        '''
        Retorna uma string representando o vetor.

        A string é composta pelas coordenadas x e y do vetor, separadas por um espaço.

        Exemplo:

        >>> v = Vec2([1, 2])
        >>> print(v)
        1.0 2.0
        '''
        return f"{self.vec[0]} {self.vec[1]}"
    
    
    def length(self) -> np.float64:
        '''
        Retorna o comprimento do vetor.

        Exemplo:

        >>> v = Vec2([1, 2])
        >>> print(v.length())  # sqrt(1 ** 2 + 2 ** 2)
        2.23606797749979
        '''
        return super().length()
    
    def squared_length(self) -> np.float64:
        '''
        Retorna o comprimento do vetor ao quadrado.

        Exemplo:

        >>> v = Vec2([1, 2])
        >>> print(v.squared_length())  # 1 ** 2 + 2 ** 2
        5.0
        '''
        return super().squared_length()
    
    def dot(self, other: 'Vec2') -> np.float64:
        '''
        Retorna o produto escalar entre dois vetores.

        Exemplo:

        >>> v1 = Vec2([1, 2])
        >>> v2 = Vec2([3, 4])
        >>> print(v1.dot(v2))
        11.0

        ---

        Parâmetros:

            - other: 'Vec2' - Segundo vetor do produto escalar.
        
        ---

        Retorno:
            
            - np.float64 - Resultado do produto escalar.
        '''
        return super().dot(other)
    
    def cross(self, other: 'Vec2') -> np.float64:
        '''
        Retorna o produto vetorial entre dois vetores.

        Exemplo:

        >>> v1 = Vec2([1, 2])
        >>> v2 = Vec2([3, 4])
        >>> print(v1.cross(v2))
        -2.0

        ---

        Parâmetros:

            - other: 'Vec2' - Segundo vetor do produto vetorial.
        
        ---

        Retorno:

            - np.float64 - Resultado do produto vetorial.
        '''
        if not isinstance(other, Vec2):
            raise TypeError(f"Tipo inválido para produto vetorial, esperado: Vec2, recebido: {type(other)}")
        
        return self.vec[0] * other.vec[1] - self.vec[1] * other.vec[0]
    
    def unit_vector(self) -> 'Vec2':
        '''
        Retorna o vetor unitário.

        Exemplo:

        >>> v = Vec2([1, 2])
        >>> print(v.unit_vector())
        0.45 0.89

        ---

        Retorno:

            - Vec2 - Vetor unitário.
        '''
        return super().unit_vector()

Point2 = Vec2