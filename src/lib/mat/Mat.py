'''
Classe base para as Matrizes (Mat2, Mat3 e Mat4)
'''


from typing import Union
import numpy as np
from lib.vec.Vec import Vec


class Mat:
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

    def __init__(self, matrix: Union[np.ndarray, list], shape: tuple):
        '''
        Construtor da classe de matrizes. Recebe uma matriz numpy (ou uma lista) que será utilizada para guardar os dados da matriz.

        --- 

        Parâmetros:

            - matrix: Union[np.ndarray, list] - Matriz numpy (ou lista) que será utilizada para guardar os dados da matriz.

            - shape: tuple - Shape da matriz.
        '''
        if isinstance(matrix, list):
            self.matrix = np.array(matrix, dtype=np.float64)
        elif isinstance(matrix, np.ndarray):
            if matrix.dtype != np.float64:
                self.matrix = matrix.astype(np.float64)
            else:
                self.matrix = matrix
        else:
            raise TypeError(f"Matriz com tipo inválido, esperado: list ou np.ndarray, recebido: {type(matrix)}")
        
        self.shape = shape
        if self.matrix.shape != self.shape:
            raise ValueError(f"Matriz com shape inválido, esperado: {self.shape}, recebido: {self.matrix.shape}")

    def __neg__(self) -> 'Mat':
        '''
        Inverte o sinal de todos elementos da matriz.

        ---

        Retorno:

            - Mat - Versão negativa da matriz.
        '''
        return self.__class__(-self.matrix)
    
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
        return self.matrix[key]

    def __setitem__(self, key, value):
        '''
        Atribui valores aos indices escolhidos

        ---

        Parâmetros:
            
            - key: - Índice de acesso à matriz

            - value: - Valores a serem colocado
        '''
        self.matrix[key] = value

    

    def __add__(self, other: Union['Mat', Vec, np.float64]) -> 'Mat':
        '''
        Soma elemento a elemento de duas matrizes.
        
        Ou soma um número a cada elemento da matriz.

        Ou soma um vetor a cada linha da matriz.

        ---

        Parâmetros:

            - other: Union['Mat', Vec, np.float64] - Matriz, vetor ou número a ser somado.
        
        ---

        Retorno:

            - Mat - Resultado da soma.

        '''
        if isinstance(other, Mat):
            # Somando duas matrizes - elemento a elemento
            return self.__class__(self.matrix + other.matrix)
        elif isinstance(other, Vec):
            # Somando uma matriz e um vetor - cada linha da matriz é somada com o vetor
            return self.__class__(self.matrix + other.vec)
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            # Somando uma matriz e um número - cada elemento da matriz é somado com o número
            return self.__class__(self.matrix + other)
        else:
            return NotImplemented  # força a chamada do método __radd__ do outro objeto, que pode estar implementado
    
    def __radd__(self, other: Union['Mat', Vec, np.float64]) -> 'Mat':
        return self.__add__(other)
    
    def __sub__(self, other: Union['Mat', Vec, np.float64]) -> 'Mat':
        '''
        Subtrai elemento a elemento de duas matrizes.
        
        Ou subtrai um número a cada elemento da matriz.

        Ou subtrai um vetor a cada linha da matriz.

        ---

        Parâmetros:

            - other: Union['Mat', Vec, np.float64] - Matriz, vetor ou número a ser subtraido.
        
        ---

        Retorno:

            - Mat - Resultado da subtração.
        '''
        if isinstance(other, Mat):
            # Subtraindo duas matrizes - elemento a elemento
            return self.__class__(self.matrix - other.matrix)
        elif isinstance(other, Vec):
            # Subtraindo uma matriz e um vetor - cada linha da matriz é subtraida com o vetor
            return self.__class__(self.matrix - other.vec)
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            # Subtraindo uma matriz e um número - cada elemento da matriz é subtraido com o número
            return self.__class__(self.matrix - other)
        else:
            return NotImplemented  # força a chamada do método __rsub__ do outro objeto, que pode estar implementado
    
    def __rsub__(self, other: Union['Mat', Vec, np.float64]) -> 'Mat':
        # A ordem importa, pois a subtração não é comutativa
        # EX: 1 - mat != mat - 1
        if isinstance(other, Vec):
            return self.__class__(other.vec - self.matrix)
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            return self.__class__(other - self.matrix)
        else:
            return self.__sub__(other)
    
    def __mul__(self, other: Union['Mat', Vec, np.float64]) -> 'Mat':
        '''
        Multiplica elemento a elemento de duas matrizes.
        
        Ou multiplica um número a cada elemento da matriz.

        Ou multiplica um vetor a cada linha da matriz.

        ---

        Parâmetros:

            - other: Union['Mat', Vec, np.float64] - Matriz, vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Mat - Resultado da multiplicação.
        '''
        if isinstance(other, Mat):
            # Multiplicando duas matrizes - elemento a elemento
            return self.__class__(self.matrix * other.matrix)
        elif isinstance(other, Vec):
            # Multiplicando uma matriz e um vetor - cada linha da matriz é multiplicada com o vetor
            return self.__class__(self.matrix * other.vec)
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            # Multiplicando uma matriz e um número - cada elemento da matriz é multiplicado com o número
            return self.__class__(self.matrix * other)
        else:
            return NotImplemented  # força a chamada do método __rmul__ do outro objeto, que pode estar implementado
    
    def __rmul__(self, other: Union['Mat', Vec, np.float64]) -> 'Mat':
        return self.__mul__(other)
    
    def __truediv__(self, other: Union['Mat', Vec, np.float64]) -> 'Mat':
        '''
        Divide elemento a elemento de duas matrizes.
        
        Ou Divide um número a cada elemento da matriz.

        Ou Divide um vetor a cada linha da matriz.

        ---

        Parâmetros:

            - other: Union['Mat', Vec, np.float64] - Matriz, vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Mat - Resultado da divisão.
        '''
        if isinstance(other, Mat):
            # Dividindo duas matrizes - elemento a elemento
            return self.__class__(self.matrix / other.matrix)
        elif isinstance(other, Vec):
            # Dividindo uma matriz e um vetor - cada linha da matriz é dividida com o vetor
            return self.__class__(self.matrix / other.vec)
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            # Dividindo uma matriz e um número - cada elemento da matriz é dividido com o número
            return self.__class__(self.matrix / other)
        else:
            return NotImplemented  # força a chamada do método __rtruediv__ do outro objeto, que pode estar implementado

    def __rtruediv__(self, other: Union['Mat', Vec, np.float64]) -> 'Mat':
        # A ordem importa, pois a divisão não é comutativa
        # EX: 1 / mat != mat / 1
        if isinstance(other, Vec):
            return self.__class__(other.vec / self.matrix)
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            return self.__class__(other / self.matrix)
        else:
            return self.__truediv__(other)

    def __iadd__(self, other: Union['Mat', Vec, np.float64]) -> 'Mat':
        '''
        Soma elemento a elemento de duas matrizes.
        
        Ou soma um número a cada elemento da matriz.

        Ou soma um vetor a cada linha da matriz.

        ---

        Parâmetros:

            - other: Union['Mat', Vec, np.float64] - Matriz, vetor ou número a ser somado.
        
        ---

        Retorno:

            - Mat - Resultado da soma.

        '''
        if isinstance(other, Mat):
            # Somando duas matrizes - elemento a elemento
            self.matrix += other.matrix
            return self
        elif isinstance(other, Vec):
            # Somando uma matriz e um vetor - cada linha da matriz é somada com o vetor
            self.matrix += other.vec
            return self
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            # Somando uma matriz e um número - cada elemento da matriz é somado com o número
            self.matrix += other
            return self
        else:
            return NotImplemented
    
    def __isub__(self, other: Union['Mat', Vec, np.float64]) -> 'Mat':
        '''
        Subtrai elemento a elemento de duas matrizes.
        
        Ou subtrai um número a cada elemento da matriz.

        Ou subtrai um vetor a cada linha da matriz.

        ---

        Parâmetros:

            - other: Union['Mat', Vec, np.float64] - Matriz, vetor ou número a ser subtraido.
        
        ---

        Retorno:

            - Mat - Resultado da subtração.
        '''
        if isinstance(other, Mat):
            # Subtraindo duas matrizes - elemento a elemento
            self.matrix -= other.matrix
            return self
        elif isinstance(other, Vec):
            # Subtraindo uma matriz e um vetor - cada linha da matriz é subtraida com o vetor
            self.matrix -= other.vec
            return self
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            # Subtraindo uma matriz e um número - cada elemento da matriz é subtraido com o número
            self.matrix -= other
            return self
        else:
            return NotImplemented
    
    def __imul__(self, other: Union['Mat', Vec, np.float64]) -> 'Mat':
        '''
        Multiplica elemento a elemento de duas matrizes.
        
        Ou multiplica um número a cada elemento da matriz.

        Ou multiplica um vetor a cada linha da matriz.

        ---

        Parâmetros:

            - other: Union['Mat', Vec, np.float64] - Matriz, vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Mat - Resultado da multiplicação.
        '''
        if isinstance(other, Mat):
            # Multiplicando duas matrizes - elemento a elemento
            self.matrix *= other.matrix
            return self
        elif isinstance(other, Vec):
            # Multiplicando uma matriz e um vetor - cada linha da matriz é multiplicada com o vetor
            self.matrix *= other.vec
            return self
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            # Multiplicando uma matriz e um número - cada elemento da matriz é multiplicado com o número
            self.matrix *= other
            return self
        else:
            return NotImplemented

    def __itruediv__(self, other: Union['Mat', Vec, np.float64]) -> 'Mat':
        '''
        Divide elemento a elemento de duas matrizes.
        
        Ou Divide um número a cada elemento da matriz.

        Ou Divide um vetor a cada linha da matriz.

        ---

        Parâmetros:

            - other: Union['Mat', Vec, np.float64] - Matriz, vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Mat - Resultado da divisão.
        '''
        if isinstance(other, Mat):
            # Dividindo duas matrizes - elemento a elemento
            self.matrix /= other.matrix
            return self
        elif isinstance(other, Vec):
            # Dividindo uma matriz e um vetor - cada linha da matriz é dividida com o vetor
            self.matrix /= other.vec
            return self
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            # Dividindo uma matriz e um número - cada elemento da matriz é dividido com o número
            self.matrix /= other
            return self
        else:
            return NotImplemented
    
    def __repr__(self) -> str:
        '''
        Retorna uma string representando a matriz.

        ---

        Retorno:
            
                - str - String representando a matriz.
        '''
        string = ""
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                string += f"{self.matrix[i,j]} "
            string = string[:-1]
            string += "\n"
        return string
    
    def dot(self, other: 'Mat') -> 'Mat':
        '''
        Retorna o resultado da multiplicação de matrizes.

        ---

        Parâmetros:

            - other: Mat - Segundo vetor do produto escalar.
        
        ---

        Retorno:
            
            - Mat - Resultado do produto escalar.
        '''
        if not isinstance(other, Mat):
            raise TypeError(f"Tipo inválido para multiplicação de matrizes, esperado: Mat, recebido: {type(other)}")
        
        return self.__class__(self.matrix.dot(other.matrix))
