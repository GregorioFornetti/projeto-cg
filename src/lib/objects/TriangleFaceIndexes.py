
from __future__ import annotations
from typing import Union


class TriangleFaceIndexes:

    def __init__(self, vertexes_indexes: list[int], textures_indexes: list[Union[int, None]] = None, normals_indexes: list[Union[int, None]] = None):
        '''
        Construtor da classe FaceIndex.

        Responsável por armazenar os índices de um vértice, textura e normal de uma face.

        O valor None é utilizado para indicar que o índice não foi especificado.

        OBS: Todas as listas devem ter tamanho 3.

        ---

        Parâmetros:

            - vertexes_indexes: list[int] - Lista com os índices dos vértices da face.

            - textures_indexes: list[Union[int, None]] - Lista com os índices das texturas da face. Pode conter None caso o índice não tenha sido especificado.

            - normals_indexes: list[Union[int, None]] - Lista com os índices das normais da face. Pode conter None caso o índice não tenha sido especificado.
        '''
        if len(vertexes_indexes) != 3:
            raise Exception('vertexes_indexes deve ter tamanho 3')
        
        if len(textures_indexes) != 3:
            raise Exception('textures_indexes deve ter tamanho 3')
        
        if len(normals_indexes) != 3:
            raise Exception('normals_indexes deve ter tamanho 3')

        self.__infos = [
            tuple(vertexes_indexes),
            tuple(textures_indexes),
            tuple(normals_indexes)
        ]
    
    def __getitem__(self, key: int):
        '''
        Retorna o índice especificado. 0 = vertexes_indexes, 1 = textures_indexes, 2 = normals_indexes.

        ---

        Parâmetros:

            - key: int - Chave para especificar o índice a ser retornado. 0 = vertexes_indexes, 1 = textures_indexes, 2 = normals_indexes.

        ---

        Retorno:

            - TriangleFaceIndex
        '''
        return self.__infos[key]
    
    @property
    def vertexes_indexes(self):
        '''
        Retorna uma tupla com os índices dos vértices da face.

        ---

        Retorno:

            - tuple[int] - Tupla com os índices dos vértices da face.
        '''
        return self.__infos[0]
    
    @property
    def textures_indexes(self):
        '''
        Retorna uma tupla com os índices das texturas da face. Pode conter None caso o índice não tenha sido especificado.

        ---

        Retorno:

            - tuple[int, None] - Tupla com os índices das texturas da face. Pode conter None caso o índice não tenha sido especificado.
        '''
        return self.__infos[1]
    
    @property
    def normals_indexes(self):
        '''
        Retorna uma tupla com os índices das normais da face. Pode conter None caso o índice não tenha sido especificado.

        ---

        Retorno:

            - tuple[int, None] - Tupla com os índices das normais da face. Pode conter None caso o índice não tenha sido especificado.
        '''
        return self.__infos[2]
    
    @property
    def vertex_1(self):
        '''
        Retorna o índice do primeiro vértice da face.

        ---

        Retorno:

            - int - Índice do primeiro vértice da face.
        '''
        return self.__infos[0][0]
    
    @property
    def vertex_2(self):
        '''
        Retorna o índice do segundo vértice da face.

        ---

        Retorno:

            - int - Índice do segundo vértice da face.
        '''
        return self.__infos[0][1]
    
    @property
    def vertex_3(self):
        '''
        Retorna o índice do terceiro vértice da face.

        ---

        Retorno:

            - int - Índice do terceiro vértice da face.
        '''
        return self.__infos[0][2]
    
    @property
    def texture_1(self):
        '''
        Retorna o índice da primeira textura da face. Pode ser None caso o índice não tenha sido especificado.

        ---

        Retorno:

            - Union[int, None] - Índice da primeira textura da face. Pode ser None caso o índice não tenha sido especificado.
        '''
        return self.__infos[1][0]
    
    @property
    def texture_2(self):
        '''
        Retorna o índice da segunda textura da face. Pode ser None caso o índice não tenha sido especificado.

        ---

        Retorno:

            - Union[int, None] - Índice da segunda textura da face. Pode ser None caso o índice não tenha sido especificado.
        '''
        return self.__infos[1][1]

    @property
    def texture_3(self):
        '''
        Retorna o índice da terceira textura da face. Pode ser None caso o índice não tenha sido especificado.

        ---

        Retorno:

            - Union[int, None] - Índice da terceira textura da face. Pode ser None caso o índice não tenha sido especificado.
        '''
        return self.__infos[1][2]
    
    @property
    def normal_1(self):
        '''
        Retorna o índice da primeira normal da face. Pode ser None caso o índice não tenha sido especificado.

        ---

        Retorno:

            - Union[int, None] - Índice da primeira normal da face. Pode ser None caso o índice não tenha sido especificado.
        '''
        return self.__infos[2][0]
    
    @property
    def normal_2(self):
        '''
        Retorna o índice da segunda normal da face. Pode ser None caso o índice não tenha sido especificado.

        ---

        Retorno:

            - Union[int, None] - Índice da segunda normal da face. Pode ser None caso o índice não tenha sido especificado.
        '''
        return self.__infos[2][1]
    
    @property
    def normal_3(self):
        '''
        Retorna o índice da terceira normal da face. Pode ser None caso o índice não tenha sido especificado.

        ---

        Retorno:

            - Union[int, None] - Índice da terceira normal da face. Pode ser None caso o índice não tenha sido especificado.
        '''
        return self.__infos[2][2]