
from typing import Union
import numpy as np
from lib.vec.Vec4 import Vec4
from lib.mat.Mat import Mat

class Mat4(Mat):
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

    def __init__(self, matrix: np.ndarray = np.zeros((4, 4), dtype=np.float64)):
        '''
        Construtor da classe de matrizes. Recebe uma matriz numpy que será utilizada para guardar os dados da matriz.

        --- 

        Parâmetros:

            - matrix: np.ndarray - Matriz numpy que será utilizada para guardar os dados da matriz.
        '''
        super().__init__(matrix, (4, 4))
        
    def __neg__(self) -> 'Mat4':
        '''
        Inverte o sinal de todos elementos da matriz.

        Exemplo:

        >>> m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> print(-m)
        -1.0 -2.0 -3.0 -4.0
        -5.0 -6.0 -7.0 -8.0
        -9.0 -10.0 -11.0 -12.0
        -13.0 -14.0 -15.0 -16.0

        ---

        Retorno:

            - Mat4 - Versão negativa da matriz.
        '''
        return super().__neg__()
    
    def __getitem__(self, key) -> Union[np.float64, np.ndarray]:
        '''
        Retorna o valor (ou valores) dos indices escolhidos.

        Acessando uma linha:

        >>> m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> print(m[0])
        1.0 2.0 3.0 4.0

        Acessando um elemento:

        >>> m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> print(m[0,0])
        1.0

        Acessando uma coluna:

        >>> m = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> print(m[:,0])
        1.0
        5.0
        9.0
        13.0

        Para mais operações de índices, veja: https://numpy.org/doc/stable/user/basics.indexing.html

        ---

        Parâmetros:
            
            - key: - Índice de acesso à matriz

        ---

        Retorno:
            
            - Union[np.ndarray, np.float64] - Valores contidos nos índices escolhidos.
        '''
        return super().__getitem__(key)
    

    def __add__(self, other: Union['Mat4', Vec4, np.float64]) -> 'Mat4':
        '''
        Soma elemento a elemento de duas matrizes.
        
        Ou soma um número a cada elemento da matriz.

        Ou soma um vetor a cada linha da matriz.

        Exemplo:

        Para soma de matrizes:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> m2 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> print(m1 + m2)
        2.0 4.0 6.0 8.0
        10.0 12.0 14.0 16.0
        18.0 20.0 22.0 24.0
        26.0 28.0 30.0 32.0

        Para soma de um vetor:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> v1 = Vec4([1, 2, 3, 4])
        >>> print(m1 + v1)
        2.0 4.0 6.0 8.0
        6.0 8.0 10.0 12.0
        10.0 12.0 14.0 16.0
        14.0 16.0 18.0 20.0

        Para soma de um número:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> print(m1 + 1)
        2.0 3.0 4.0 5.0
        6.0 7.0 8.0 9.0
        10.0 11.0 12.0 13.0
        14.0 15.0 16.0 17.0

        ---

        Parâmetros:

            - other: Union['Mat4', Vec4, np.float64] - Matriz, vetor ou número a ser somado.
        
        ---

        Retorno:

            - Mat4 - Resultado da soma.
        '''
        return super().__add__(other)
    
    def __sub__(self, other: Union['Mat4', Vec4, np.float64]) -> 'Mat4':
        '''
        Subtrai elemento a elemento de duas matrizes.
        
        Ou subtrai um número a cada elemento da matriz.

        Ou subtrai um vetor a cada linha da matriz.

        Exemplo:

        Para subtração de matrizes:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> m2 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> print(m1 - m2)
        0.0 0.0 0.0 0.0
        0.0 0.0 0.0 0.0
        0.0 0.0 0.0 0.0
        0.0 0.0 0.0 0.0

        Para subtração de um vetor:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> v1 = Vec4([1, 2, 3, 4])
        >>> print(m1 - v1)
        0.0 0.0 0.0 0.0
        4.0 4.0 4.0 4.0
        8.0 8.0 8.0 8.0
        12.0 12.0 12.0 12.0

        Para subtração de um número:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> print(m1 - 1)
        0.0 1.0 2.0 3.0
        4.0 5.0 6.0 7.0
        8.0 9.0 10.0 11.0
        12.0 13.0 14.0 15.0

        ---

        Parâmetros:

            - other: Union['Mat4', Vec4, np.float64] - Matriz, vetor ou número a ser subtraido.
        
        ---

        Retorno:

            - Mat4 - Resultado da subtração.
        '''
        return super().__sub__(other)
    
    def __mul__(self, other: Union['Mat4', Vec4, np.float64]) -> 'Mat4':
        '''
        Multiplica elemento a elemento de duas matrizes.
        
        Ou multiplica um número a cada elemento da matriz.

        Ou multiplica um vetor a cada linha da matriz.

        Exemplo:

        Para multiplicação de matrizes:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> m2 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> print(m1 * m2)
        1.0 4.0 9.0 16.0
        25.0 36.0 49.0 64.0
        81.0 100.0 121.0 144.0
        169.0 196.0 225.0 256.0

        Para multiplicação de um vetor:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> v1 = Vec4([1, 2, 3, 4])
        >>> print(m1 * v1)
        1.0 4.0 9.0 16.0
        5.0 12.0 21.0 32.0
        9.0 20.0 33.0 48.0
        13.0 28.0 45.0 64.0

        Para multiplicação de um número:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> print(m1 * 2)
        2.0 4.0 6.0 8.0
        10.0 12.0 14.0 16.0
        18.0 20.0 22.0 24.0
        26.0 28.0 30.0 32.0
        
        ---

        Parâmetros:

            - other: Union['Mat4', Vec4, np.float64] - Matriz, vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Mat4 - Resultado da multiplicação.
        '''
        return super().__mul__(other)
    
    def __truediv__(self, other: Union['Mat4', Vec4, np.float64]) -> 'Mat4':
        '''
        Divide elemento a elemento de duas matrizes.
        
        Ou Divide um número a cada elemento da matriz.

        Ou Divide um vetor a cada linha da matriz.

        Exemplo:

        Para divisão de matrizes:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> m2 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> print(m1 / m2)
        1.0 1.0 1.0 1.0
        1.0 1.0 1.0 1.0
        1.0 1.0 1.0 1.0
        1.0 1.0 1.0 1.0

        Para divisão de um vetor:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> v1 = Vec4([1, 2, 3, 4])
        >>> print(m1 / v1)
        1.0 1.0 1.0 1.0
        5.0 3.0 2.3 2.0
        9.0 5.0 3.7 3.0
        13.0 7.0 5.0 4.0

        Para divisão de um número:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> print(m1 / 2)
        0.5 1.0 1.5 2.0
        2.5 3.0 3.5 4.0
        4.5 5.0 5.5 6.0
        6.5 7.0 7.5 8.0

        ---

        Parâmetros:

            - other: Union['Mat4', Vec4, np.float64] - Matriz, vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Mat4 - Resultado da divisão.
        '''
        return super().__truediv__(other)


    def __iadd__(self, other: Union['Mat4', Vec4, np.float64]) -> 'Mat4':
        '''
        Soma elemento a elemento de duas matrizes.
        
        Ou soma um número a cada elemento da matriz.

        Ou soma um vetor a cada linha da matriz.

        Exemplo:

        Para soma de matrizes:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> m2 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> m1 += m2
        >>> print(m1)
        2.0 4.0 6.0 8.0
        10.0 12.0 14.0 16.0
        18.0 20.0 22.0 24.0
        26.0 28.0 30.0 32.0

        Para soma de um vetor:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> v1 = Vec4([1, 2, 3, 4])
        >>> m1 += v1
        >>> print(m1)
        2.0 4.0 6.0 8.0
        6.0 8.0 10.0 12.0
        10.0 12.0 14.0 16.0
        14.0 16.0 18.0 20.0

        Para soma de um número:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> m1 += 1
        >>> print(m1)
        2.0 3.0 4.0 5.0
        6.0 7.0 8.0 9.0
        10.0 11.0 12.0 13.0
        14.0 15.0 16.0 17.0

        ---

        Parâmetros:

            - other: Union['Mat4', Vec4, np.float64] - Matriz, vetor ou número a ser somado.
        
        ---

        Retorno:

            - Mat4 - Resultado da soma.

        '''
        return super().__iadd__(other)
    
    def __isub__(self, other: Union['Mat4', Vec4, np.float64]) -> 'Mat4':
        '''
        Subtrai elemento a elemento de duas matrizes.
        
        Ou subtrai um número a cada elemento da matriz.

        Ou subtrai um vetor a cada linha da matriz.

        Exemplo:

        Para subtração de matrizes:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> m2 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> m1 -= m2
        >>> print(m1)
        0.0 0.0 0.0 0.0
        0.0 0.0 0.0 0.0
        0.0 0.0 0.0 0.0
        0.0 0.0 0.0 0.0

        Para subtração de um vetor:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> v1 = Vec4([1, 2, 3, 4])
        >>> m1 -= v1
        >>> print(m1)
        0.0 0.0 0.0 0.0
        4.0 4.0 4.0 4.0
        8.0 8.0 8.0 8.0
        12.0 12.0 12.0 12.0

        Para subtração de um número:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> m1 -= 1
        >>> print(m1)
        0.0 1.0 2.0 3.0
        4.0 5.0 6.0 7.0
        8.0 9.0 10.0 11.0
        12.0 13.0 14.0 15.0

        ---

        Parâmetros:

            - other: Union['Mat4', Vec4, np.float64] - Matriz, vetor ou número a ser subtraido.
        
        ---

        Retorno:

            - Mat4 - Resultado da subtração.
        '''
        return super().__isub__(other)
    
    def __imul__(self, other: Union['Mat4', Vec4, np.float64]) -> 'Mat4':
        '''
        Multiplica elemento a elemento de duas matrizes.
        
        Ou multiplica um número a cada elemento da matriz.

        Ou multiplica um vetor a cada linha da matriz.

        Exemplo:

        Para multiplicação de matrizes:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> m2 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> m1 *= m2
        >>> print(m1)
        1.0 4.0 9.0 16.0
        25.0 36.0 49.0 64.0
        81.0 100.0 121.0 144.0
        169.0 196.0 225.0 256.0

        Para multiplicação de um vetor:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> v1 = Vec4([1, 2, 3, 4])
        >>> m1 *= v1
        >>> print(m1)
        1.0 4.0 9.0 16.0
        5.0 12.0 21.0 32.0
        9.0 20.0 33.0 48.0
        13.0 28.0 45.0 64.0

        Para multiplicação de um número:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> m1 *= 2
        >>> print(m1)
        2.0 4.0 6.0 8.0
        10.0 12.0 14.0 16.0
        18.0 20.0 22.0 24.0
        26.0 28.0 30.0 32.0
        ---

        Parâmetros:

            - other: Union['Mat4', Vec4, np.float64] - Matriz, vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Mat4 - Resultado da multiplicação.
        '''
        return super().__imul__(other)

    def __itruediv__(self, other: Union['Mat4', Vec4, np.float64]) -> 'Mat4':
        '''
        Divide elemento a elemento de duas matrizes.
        
        Ou Divide um número a cada elemento da matriz.

        Ou Divide um vetor a cada linha da matriz.

        Exemplo:

        Para divisão de matrizes:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> m2 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> m1 /= m2
        >>> print(m1)
        1.0 1.0 1.0 1.0
        1.0 1.0 1.0 1.0
        1.0 1.0 1.0 1.0
        1.0 1.0 1.0 1.0
        

        Para divisão de um vetor:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> v1 = Vec4([1, 2, 3, 4])
        >>> m1 /= v1
        >>> print(m1)
        1.0 1.0 1.0 1.0
        5.0 3.0 2.3 2.0
        9.0 5.0 3.7 3.0
        13.0 7.0 5.0 4.0

        Para divisão de um número:
        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> m1 /= 2
        >>> print(m1)
        0.5 1.0 1.5 2.0
        2.5 3.0 3.5 4.0
        4.5 5.0 5.5 6.0
        6.5 7.0 7.5 8.0

        ---

        Parâmetros:

            - other: Union['Mat4', Vec4, np.float64] - Matriz, vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Mat4 - Resultado da divisão.
        '''
        return super().__itruediv__(other)
    
    def __repr__(self) -> str:
        '''
        Retorna uma string representando a matriz.

        Exemplo:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> print(m1)
        1.0 2.0 3.0 4.0
        5.0 6.0 7.0 8.0
        9.0 10.0 11.0 12.0
        13.0 14.0 15.0 16.0

        ---

        Retorno:
            
                - str - String representando a matriz.
        '''
        return super().__repr__()
    
    def dot(self, other: 'Mat4') -> 'Mat4':
        '''
        Retorna o resultado da multiplicação de matrizes.

        Exemplo:

        >>> m1 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> m2 = Mat4(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))
        >>> print(m1.dot(m2))
        90.0 100.0 110.0 120.0
        202.0 228.0 254.0 280.0
        314.0 356.0 398.0 440.0
        426.0 484.0 542.0 600.0

        ---

        Parâmetros:

            - other: Mat4 - Segundo vetor do produto escalar.
        
        ---

        Retorno:
            
            - Mat4 - Resultado do produto escalar.
        '''
        return super().dot(other)
