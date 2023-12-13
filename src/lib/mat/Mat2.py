
from typing import Union
import numpy as np
from lib.vec.Vec2 import Vec2
from lib.mat.Mat import Mat

class Mat2(Mat):
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

    def __init__(self, matrix: np.ndarray = np.zeros((2, 2), dtype=np.float64)):
        '''
        Construtor da classe de matrizes. Recebe uma matriz numpy que será utilizada para guardar os dados da matriz.

        --- 

        Parâmetros:

            - matrix: np.ndarray - Matriz numpy que será utilizada para guardar os dados da matriz.
        '''
        super().__init__(matrix, (2, 2))

    def __neg__(self) -> 'Mat2':
        '''
        Inverte o sinal de todos elementos da matriz.

        Exemplo:

        >>> m = Mat2(np.array([[1, 2], [3, 4]]))
        >>> print(-m)
        -1.0 -2.0
        -3.0 -4.0

        ---

        Retorno:

            - Mat2 - Versão negativa da matriz.
        '''
        return super().__neg__()
    
    def __getitem__(self, key) -> Union[np.float64, np.ndarray]:
        '''
        Retorna o valor (ou valores) dos indices escolhidos.

        Acessando uma linha:

        >>> m = Mat2(np.array([[1, 2], [3, 4]))
        >>> print(m[0])
        1.0 2.0

        Acessando um elemento:

        >>> m = Mat2(np.array([[1, 2], [3, 4]))
        >>> print(m[0,0])
        1.0

        Acessando uma coluna:

        >>> m = Mat2(np.array([[1, 2], [3, 4]))
        >>> print(m[:,0])
        1.0
        3.0

        Para mais operações de índices, veja: https://numpy.org/doc/stable/user/basics.indexing.html

        ---

        Parâmetros:
            
            - key: - Índice de acesso à matriz

        ---

        Retorno:
            
            - Union[np.ndarray, np.float64] - Valores contidos nos índices escolhidos.
        '''
        return super().__getitem__(key)
    

    def __add__(self, other: Union['Mat2', Vec2, np.float64]) -> 'Mat2':
        '''
        Soma elemento a elemento de duas matrizes.
        
        Ou soma um número a cada elemento da matriz.

        Ou soma um vetor a cada linha da matriz.

        Exemplo:

        Para soma de matrizes:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> m2 = Mat2(np.array([[5, 6], [7, 8]]))
        >>> print(m1 + m2)
        6.0 8.0
        10.0 12.0

        Para soma de um vetor:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> v1 = Vec2([5, 6])
        >>> print(m1 + v1)
        6.0 8.0
        8.0 10.0

        Para soma de um número:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> print(m1 + 1)
        2.0 3.0
        4.0 5.0

        ---

        Parâmetros:

            - other: Union['Mat2', Vec2, np.float64] - Matriz, vetor ou número a ser somado.
        
        ---

        Retorno:

            - Mat2 - Resultado da soma.
        '''
        return super().__add__(other)
    
    def __sub__(self, other: Union['Mat2', Vec2, np.float64]) -> 'Mat2':
        '''
        Subtrai elemento a elemento de duas matrizes.
        
        Ou subtrai um número a cada elemento da matriz.

        Ou subtrai um vetor a cada linha da matriz.

        Exemplo:

        Para subtração de matrizes:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> m2 = Mat2(np.array([[5, 6], [7, 8]]))
        >>> print(m1 - m2)
        -4.0 -4.0
        -4.0 -4.0

        Para subtração de um vetor:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> v1 = Vec2([5, 6])
        >>> print(m1 - v1)
        -4.0 -4.0
        -2.0 -2.0

        Para subtração de um número:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> print(m1 - 1)
        0.0 1.0
        2.0 3.0

        ---

        Parâmetros:

            - other: Union['Mat2', Vec2, np.float64] - Matriz, vetor ou número a ser subtraido.
        
        ---

        Retorno:

            - Mat2 - Resultado da subtração.
        '''
        return super().__sub__(other)
    
    def __mul__(self, other: Union['Mat2', Vec2, np.float64]) -> 'Mat2':
        '''
        Multiplica elemento a elemento de duas matrizes.
        
        Ou multiplica um número a cada elemento da matriz.

        Ou multiplica um vetor a cada linha da matriz.

        Exemplo:

        Para multiplicação de matrizes:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> m2 = Mat2(np.array([[5, 6], [7, 8]]))
        >>> print(m1 * m2)
        5.0 12.0
        21.0 32.0

        Para multiplicação de um vetor:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> v1 = Vec2([5, 6])
        >>> print(m1 * v1)
        5.0 12.0
        15.0 24.0

        Para multiplicação de um número:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> print(m1 * 2)
        2.0 4.0
        6.0 8.0
        
        ---

        Parâmetros:

            - other: Union['Mat2', Vec2, np.float64] - Matriz, vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Mat2 - Resultado da multiplicação.
        '''
        return super().__mul__(other)
    
    def __truediv__(self, other: Union['Mat2', Vec2, np.float64]) -> 'Mat2':
        '''
        Divide elemento a elemento de duas matrizes.
        
        Ou Divide um número a cada elemento da matriz.

        Ou Divide um vetor a cada linha da matriz.

        Exemplo:

        Para divisão de matrizes:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> m2 = Mat2(np.array([[5, 6], [7, 8]]))
        >>> print(m1 / m2)
        0.2 0.33
        0.43 0.5

        Para divisão de um vetor:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> v1 = Vec2([5, 6])
        >>> print(m1 / v1)
        0.2 0.33
        0.6 0.67

        Para divisão de um número:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> print(m1 / 2)
        0.5 1.0
        1.5 2.0

        ---

        Parâmetros:

            - other: Union['Mat2', Vec2, np.float64] - Matriz, vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Mat2 - Resultado da divisão.
        '''
        return super().__truediv__(other)


    def __iadd__(self, other: Union['Mat2', Vec2, np.float64]) -> 'Mat2':
        '''
        Soma elemento a elemento de duas matrizes.
        
        Ou soma um número a cada elemento da matriz.

        Ou soma um vetor a cada linha da matriz.

        Exemplo:

        Para soma de matrizes:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> m2 = Mat2(np.array([[5, 6], [7, 8]]))
        >>> m1 += m2
        >>> print(m1)
        6.0 8.0
        10.0 12.0

        Para soma de um vetor:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> v1 = Vec2([5, 6])
        >>> m1 += v1
        >>> print(m1)
        6.0 8.0
        8.0 10.0

        Para soma de um número:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> m1 += 1
        >>> print(m1)
        2.0 3.0
        4.0 5.0

        ---

        Parâmetros:

            - other: Union['Mat2', Vec2, np.float64] - Matriz, vetor ou número a ser somado.
        
        ---

        Retorno:

            - Mat2 - Resultado da soma.

        '''
        return super().__iadd__(other)
    
    def __isub__(self, other: Union['Mat2', Vec2, np.float64]) -> 'Mat2':
        '''
        Subtrai elemento a elemento de duas matrizes.
        
        Ou subtrai um número a cada elemento da matriz.

        Ou subtrai um vetor a cada linha da matriz.

        Exemplo:

        Para subtração de matrizes:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> m2 = Mat2(np.array([[5, 6], [7, 8]]))
        >>> m1 -= m2
        >>> print(m1)
        -4.0 -4.0
        -4.0 -4.0

        Para subtração de um vetor:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> v1 = Vec2([5, 6])
        >>> m1 -= v1
        >>> print(m1)
        -4.0 -4.0
        -2.0 -2.0

        Para subtração de um número:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> m1 -= 1
        >>> print(m1)
        0.0 1.0
        2.0 3.0

        ---

        Parâmetros:

            - other: Union['Mat2', Vec2, np.float64] - Matriz, vetor ou número a ser subtraido.
        
        ---

        Retorno:

            - Mat2 - Resultado da subtração.
        '''
        return super().__isub__(other)
    
    def __imul__(self, other: Union['Mat2', Vec2, np.float64]) -> 'Mat2':
        '''
        Multiplica elemento a elemento de duas matrizes.
        
        Ou multiplica um número a cada elemento da matriz.

        Ou multiplica um vetor a cada linha da matriz.

        Exemplo:

        Para multiplicação de matrizes:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> m2 = Mat2(np.array([[5, 6], [7, 8]]))
        >>> m1 *= m2
        >>> print(m1)
        5.0 12.0
        21.0 32.0

        Para multiplicação de um vetor:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> v1 = Vec2([5, 6])
        >>> m1 *= v1
        >>> print(m1)
        5.0 12.0
        15.0 24.0

        Para multiplicação de um número:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> m1 *= 2
        >>> print(m1)
        2.0 4.0
        6.0 8.0

        ---

        Parâmetros:

            - other: Union['Mat2', Vec2, np.float64] - Matriz, vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Mat2 - Resultado da multiplicação.
        '''
        return super().__imul__(other)

    def __itruediv__(self, other: Union['Mat2', Vec2, np.float64]) -> 'Mat2':
        '''
        Divide elemento a elemento de duas matrizes.
        
        Ou Divide um número a cada elemento da matriz.

        Ou Divide um vetor a cada linha da matriz.

        Exemplo:

        Para divisão de matrizes:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> m2 = Mat2(np.array([[5, 6], [7, 8]]))
        >>> m1 /= m2
        >>> print(m1)
        0.2 0.33
        0.43 0.5

        Para divisão de um vetor:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> v1 = Vec2([5, 6])
        >>> m1 /= v1
        >>> print(m1)
        0.2 0.33
        0.6 0.67

        Para divisão de um número:
        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> m1 /= 2
        >>> print(m1)
        0.5 1.0
        1.5 2.0

        ---

        Parâmetros:

            - other: Union['Mat2', Vec2, np.float64] - Matriz, vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Mat2 - Resultado da divisão.
        '''
        return super().__itruediv__(other)
    
    def __repr__(self) -> str:
        '''
        Retorna uma string representando a matriz.

        Exemplo:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> print(m1)
        1.0 2.0
        3.0 4.0

        ---

        Retorno:
            
                - str - String representando a matriz.
        '''
        return super().__repr__()
    
    def dot(self, other: 'Mat2') -> 'Mat2':
        '''
        Retorna o resultado da multiplicação de matrizes.

        Exemplo:

        >>> m1 = Mat2(np.array([[1, 2], [3, 4]]))
        >>> m2 = Mat2(np.array([[5, 6], [7, 8]]))
        >>> print(m1.dot(m2))
        19.0 22.0
        43.0 50.0

        ---

        Parâmetros:

            - other: Mat2 - Segundo vetor do produto escalar.
        
        ---

        Retorno:
            
            - Mat2 - Resultado do produto escalar.
        '''
        return super().dot(other)
