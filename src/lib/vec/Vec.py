'''
Classe base para os vetores: Vec2, Vec3 e Vec4
'''


from typing import Union
import numpy as np


class Vec:
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

    def __init__(self, vector: Union[np.ndarray, list], shape: tuple):
        '''
        Construtor da classe de vetores. Recebe um array numpy (ou uma lista) que será utilizada para guardar os dados do vetor.

        ---

            - vector: Union[np.ndarray, list] - Vetor numpy (ou lista) que será utilizada para guardar os dados do vetor.

            - shape: tuple - Shape do vetor.
        '''
        if isinstance(vector, list):
            self.vec = np.array(vector, dtype=np.float64)
        elif isinstance(vector, np.ndarray):
            if vector.dtype != np.float64:
                self.vec = vector
            else:
                self.vec = vector.astype(np.float64)
        else:
            raise TypeError(f"Vetor com tipo inválido, esperado: list ou np.ndarray, recebido: {type(vector)}")
        
        self.shape = shape
        if self.vec.shape != shape:
            raise ValueError(f"Vetor com shape inválido, esperado: {shape}, recebido: {self.vec.shape}")
    
    def __neg__(self) -> 'Vec':
        '''
        Inverte o sinal de todos os elementos do vetor.

        ---

        Retorno:

            - Vec - Vetor com sinal invertido.
        '''
        return self.__class__(-self.vec)
    
    def __getitem__(self, key) -> Union[np.float64, np.ndarray]:
        '''
        Retorna o valor (ou valores) dos indices escolhidos.

        Para mais operações de índices, veja: https://numpy.org/doc/stable/user/basics.indexing.html

        ---

        Parâmetros:
            
            - key: - Índice de acesso à matriz

        ---

        Retorno:
            
            - Union[np.ndarray, np.float64] - Valores contidos nos índices escolhidos.
        '''
        return self.vec[key]
    
    def __setitem__(self, key, value):
        '''
        Atribui valores aos indices escolhidos

        ---

        Parâmetros:
            
            - key: - Índice de acesso à matriz

            - value: - Valores a serem colocado
        '''
        self.vec[key] = value
    
    def __add__(self, other: Union['Vec', np.float64]) -> 'Vec':
        '''
        Soma elemento a elemento de dois vetores.
        
        Ou soma um número a cada elemento do vetor.

        ---

        Parâmetros:

            - other: Union['Vec', np.float64] - Vetor ou número a ser somado.
        
        ---

        Retorno:

            - Vec - Resultado da soma.

        '''
        if isinstance(other, Vec):
            # Somando um vetor com outro vetor - cada elemento do vetor é somado com o elemento correspondente do outro vetor
            return self.__class__(self.vec + other.vec)
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            # Somando uma matriz e um número - cada elemento da matriz é somado com o número
            return self.__class__(self.vec + other)
        else:
            return NotImplemented  # força a chamada do método __radd__ do outro objeto, que pode estar implementado
    
    def __radd__(self, other: Union['Vec', np.float64]) -> 'Vec':
        '''
        Soma elemento a elemento de dois vetores.
        
        Ou soma um número a cada elemento do vetor.

        ---

        Parâmetros:

            - other: Union['Vec', np.float64] - Vetor ou número a ser somado.
        
        ---

        Retorno:

            - Vec - Resultado da soma.

        '''
        return self.__add__(other)
    
    def __sub__(self, other: Union['Vec', np.float64]) -> 'Vec':
        '''
        Subtrai elemento a elemento de dois vetores.
        
        Ou subtrai um número a cada elemento do vetor.

        ---

        Parâmetros:

            - other: Union['Vec', np.float64] - Vetor ou número a ser usado para subtração.
        
        ---

        Retorno:

            - Vec - Resultado da subtração.

        '''
        if isinstance(other, Vec):
            # Subtraindo um vetor com outro vetor - cada elemento do vetor é somado com o elemento correspondente do outro vetor
            return self.__class__(self.vec - other.vec)
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            # Subtraindo uma matriz e um número - cada elemento da matriz é somado com o número
            return self.__class__(self.vec - other)
        else:
            return NotImplemented  # força a chamada do método __rsub__ do outro objeto, que pode estar implementado
    
    def __rsub__(self, other: Union['Vec', np.float64]) -> 'Vec':
        '''
        Subtrai elemento a elemento de dois vetores.
        
        Ou subtrai um número a cada elemento do vetor.

        ---

        Parâmetros:

            - other: Union['Vec', np.float64] - Vetor ou número a ser usado para subtração.
        
        ---

        Retorno:

            - Vec - Resultado da subtração.

        '''
        # A ordem importa, pois a subtração não é comutativa
        # EX: 1 - vec != vec - 1
        if isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            return self.__class__(other - self.vec)
        return self.__sub__(other)
    
    def __mul__(self, other: Union['Vec', np.float64]) -> 'Vec':
        '''
        Multiplica elemento a elemento de dois vetores.
        
        Ou multiplica um número a cada elemento do vetor.

        ---

        Parâmetros:

            - other: Union['Vec', np.float64] - Vetor ou número a ser usado para multiplicação.
        
        ---

        Retorno:

            - Vec - Resultado da multiplicação.

        '''
        if isinstance(other, Vec):
            # Multiplicando um vetor com outro vetor - cada elemento do vetor é somado com o elemento correspondente do outro vetor
            return self.__class__(self.vec * other.vec)
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            # Multiplicando uma matriz e um número - cada elemento da matriz é somado com o número
            return self.__class__(self.vec * other)
        else:
            return NotImplemented  # força a chamada do método __rmul__ do outro objeto, que pode estar implementado
    
    def __rmul__(self, other: Union['Vec', np.float64]) -> 'Vec':
        '''
        Multiplica elemento a elemento de dois vetores.
        
        Ou multiplica um número a cada elemento do vetor.

        ---

        Parâmetros:

            - other: Union['Vec', np.float64] - Vetor ou número a ser usado para multiplicação.
        
        ---

        Retorno:

            - Vec - Resultado da multiplicação.

        '''
        return self.__mul__(other)
    
    def __truediv__(self, other: Union['Vec', np.float64]) -> 'Vec':
        '''
        Divide elemento a elemento de dois vetores.
        
        Ou divide um número a cada elemento do vetor.

        ---

        Parâmetros:

            - other: Union['Vec', np.float64] - Vetor ou número a ser usado para divisão.
        
        ---

        Retorno:

            - Vec - Resultado da divisão.

        '''
        if isinstance(other, Vec):
            # Dividindo um vetor com outro vetor - cada elemento do vetor é somado com o elemento correspondente do outro vetor
            return self.__class__(self.vec / other.vec)
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            # Dividindo uma matriz e um número - cada elemento da matriz é somado com o número
            return self.__class__(self.vec / other)
        else:
            return NotImplemented  # força a chamada do método __rtruediv__ do outro objeto, que pode estar implementado
    
    def __rtruediv__(self, other: Union['Vec', np.float64]) -> 'Vec':
        '''
        Divide elemento a elemento de dois vetores.
        
        Ou divide um número a cada elemento do vetor.

        ---

        Parâmetros:

            - other: Union['Vec', np.float64] - Vetor ou número a ser usado para divisão.
        
        ---

        Retorno:

            - Vec - Resultado da divisão.

        '''
        # A ordem importa, pois a divisão não é comutativa
        # EX: 1 / vec != vec / 1
        if isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            return self.__class__(other / self.vec)
        return self.__truediv__(other)
    
    def __iadd__(self, other: Union['Vec', np.float64]) -> 'Vec':
        '''
        Soma elemento a elemento de dois vetores.
        
        Ou soma um número a cada elemento do vetor.

        ---

        Parâmetros:

            - other: Union['Vec', np.float64] - Vetor ou número a ser somado.
        
        ---

        Retorno:

            - Vec - Resultado da soma.

        '''
        if isinstance(other, Vec):
            # Somando um vetor com outro vetor - cada elemento do vetor é somado com o elemento correspondente do outro vetor
            self.vec += other.vec
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            # Somando uma matriz e um número - cada elemento da matriz é somado com o número
            self.vec += other
        else:
            return NotImplemented
        return self

    def __isub__(self, other: Union['Vec', np.float64]) -> 'Vec':
        '''
        Subtrai elemento a elemento de dois vetores.
        
        Ou subtrai um número a cada elemento do vetor.

        ---

        Parâmetros:

            - other: Union['Vec', np.float64] - Vetor ou número a ser usado para subtração.
        
        ---

        Retorno:

            - Vec - Resultado da subtração.

        '''
        if isinstance(other, Vec):
            # Subtraindo um vetor com outro vetor - cada elemento do vetor é somado com o elemento correspondente do outro vetor
            self.vec -= other.vec
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            # Subtraindo uma matriz e um número - cada elemento da matriz é somado com o número
            self.vec -= other
        else:
            return NotImplemented
        return self
    
    def __imul__(self, other: Union['Vec', np.float64]) -> 'Vec':
        '''
        Multiplica elemento a elemento de dois vetores.
        
        Ou multiplica um número a cada elemento do vetor.

        ---

        Parâmetros:

            - other: Union['Vec', np.float64] - Vetor ou número a ser usado para multiplicação.
        
        ---

        Retorno:

            - Vec - Resultado da multiplicação.

        '''
        if isinstance(other, Vec):
            # Multiplicando um vetor com outro vetor - cada elemento do vetor é somado com o elemento correspondente do outro vetor
            self.vec *= other.vec
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            # Multiplicando uma matriz e um número - cada elemento da matriz é somado com o número
            self.vec *= other
        else:
            return NotImplemented
        return self
    
    def __itruediv__(self, other: Union['Vec', np.float64]) -> 'Vec':
        '''
        Divide elemento a elemento de dois vetores.
        
        Ou divide um número a cada elemento do vetor.

        ---

        Parâmetros:

            - other: Union['Vec', np.float64] - Vetor ou número a ser usado para divisão.
        
        ---

        Retorno:

            - Vec - Resultado da divisão.

        '''
        if isinstance(other, Vec):
            # Dividindo um vetor com outro vetor - cada elemento do vetor é somado com o elemento correspondente do outro vetor
            self.vec /= other.vec
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            # Dividindo uma matriz e um número - cada elemento da matriz é somado com o número
            self.vec /= other
        else:
            return NotImplemented
        return self
    
    def __repr__(self) -> str:
        '''
        Representação em string do vetor.

        ---

        Retorno:

            - str - String que representa o vetor.
        '''
        string = ''
        for i in range(self.shape[0]):
            string += f'{self.vec[i]} '
        return string[:-1]
    
    def length(self) -> np.float64:
        '''
        Retorna o comprimento do vetor.
        '''
        return np.sqrt(self.squared_length())

    def squared_length(self) -> np.float64:
        '''
        Retorna o comprimento do vetor ao quadrado.
        '''
        return np.dot(self.vec, self.vec)
        
    def dot(self, other: 'Vec') -> 'Vec':
        '''
        Retorna o produto escalar entre dois vetores.

        ---

        Parâmetros:

            - other: Vec - Segundo vetor do produto escalar.
        
        ---

        Retorno:
            
            - np.float64 - Resultado do produto escalar.
        '''
        if not isinstance(other, Vec):
            raise TypeError(f"Tipo inválido para produto escalar, esperado: Vec, recebido: {type(other)}")
        
        return np.dot(self.vec, other.vec)

    def unit_vector(self) -> 'Vec':
        '''
        Retorna o vetor unitário.

        ---

        Retorno:

            - Vec - Vetor unitário.
        '''
        return self / self.length()
