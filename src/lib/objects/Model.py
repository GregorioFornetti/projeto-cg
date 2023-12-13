
from lib.vec.Vec3 import Vec3
from lib.objects.Triangle import Triangle
from lib.objects.TriangleFaceIndexes import TriangleFaceIndexes
from lib.materials.Material import Material
import re

class Model:

    def __init__(self, file_path: str, material: Material):
        '''
        Construtor da classe Model. Recebe o caminho do arquivo .obj e o lê, armazenando os vértices e faces do modelo.

        Atualmente, o modelo só suporta faces com 3 vértices (triângulos), gerando erro caso o arquivo .obj contenha faces com mais de 3 vértices.

        Ainda não há suporte para faces com texturas ou normais (elas são ignoradas, não gerando erro caso o arquivo .obj contenha essas informações).

        Definição de formato definida em: https://en.wikipedia.org/wiki/Wavefront_.obj_file

        ---

        Parâmetros:

            - file_path: str - Caminho do arquivo .obj a ser lido.
        '''
        self.__vertexes: list[Vec3] = []
        self.__normals: list[Vec3] = []
        self.__faces: list[Triangle] = []
        self.__faces_indexes: list[TriangleFaceIndexes] = []
        self.material = material

        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file):
                if line.startswith('v '):
                    # Lendo novos vértices
                    
                    line_values_str = line.replace('v ', '')
                    current_vertex_coordinates = [float(coordinate) for coordinate in line_values_str.split()]

                    if len(current_vertex_coordinates) == 3:
                        self.__vertexes.append(Vec3(current_vertex_coordinates))
                    elif len(current_vertex_coordinates) == 4:
                        self.__vertexes.append(Vec3(current_vertex_coordinates[:-1]))  # A ultima coordenada é ignorada
                    else:
                        raise ValueError(f'Modelo com número de coordenadas inválido para um vértice: {len(current_vertex_coordinates)}. Deve ser apenas 3 ou 4.\nO erro ocorreu na linha {line_num + 1}:\n{line}')
                elif line.startswith('vn '):
                    # Lendo novas normais

                    line_values_str = line.replace('vn ', '')
                    current_normal_coordinates = [float(coordinate) for coordinate in line_values_str.split()]

                    if len(current_normal_coordinates) != 3:
                        raise ValueError(f'Modelo com número de coordenadas inválido para uma normal: {len(current_normal_coordinates)}. Deve ser apenas 3.\nO erro ocorreu na linha {line_num + 1}:\n{line}')
                    
                    self.__normals.append(Vec3(current_normal_coordinates))
                elif line.startswith('f '):
                    # Lendo novas faces

                    line_values_str = line.replace('f ', '')
                    current_faces_str = line_values_str.split()

                    if len(current_faces_str) != 3:
                        raise ValueError(f'Modelo com número de faces inválido: {len(current_faces_str)}. Deve ser apenas 3.\nO erro ocorreu na linha {line_num + 1}:\n{line}')
                    
                    vertexes_indexes = []
                    textures_indexes = []
                    normals_indexes = []

                    for face_str in current_faces_str:
                        current_face_index = [int(index) - 1 if index != '' else None for index in face_str.split('/')]
                        have_normals = False
                        
                        if re.search(r'^\d+$', face_str):
                            # Apenas os índices dos vértices foram especificados
                            vertexes_indexes.append(current_face_index[0])
                            textures_indexes.append(None)
                            normals_indexes.append(None)
                        
                        elif re.search(r'^\d+/\d+$', face_str):
                            # Os índices dos vértices e das texturas foram especificados
                            vertexes_indexes.append(current_face_index[0])
                            textures_indexes.append(current_face_index[1])
                            normals_indexes.append(None)

                        elif re.search(r'^\d+//\d+$', face_str):
                            # Os índices dos vértices e das normais foram especificados
                            vertexes_indexes.append(current_face_index[0])
                            textures_indexes.append(None)
                            normals_indexes.append(current_face_index[2])
                            have_normals = True
                        
                        elif re.search(r'^\d+/\d+/\d+$', face_str):
                            # Os índices dos vértices, das texturas e das normais foram especificados
                            vertexes_indexes.append(current_face_index[0])
                            textures_indexes.append(current_face_index[1])
                            normals_indexes.append(current_face_index[2])
                            have_normals = True

                        else:
                            raise ValueError(f'Modelo com número de índices inválido para uma face: {len(current_face_index)}. Deve ser apenas 1, 2 ou 3.\nO erro ocorreu na linha {line_num + 1}:\n{line}')

                    current_face_indexes = TriangleFaceIndexes(vertexes_indexes, textures_indexes, normals_indexes)
                    self.__faces_indexes.append(TriangleFaceIndexes(vertexes_indexes, textures_indexes, normals_indexes))
                    try:
                        normals = None
                        if have_normals:
                            normals = [self.__normals[index] for index in current_face_indexes[2]]
                        self.__faces.append(
                            Triangle(
                                self.__vertexes[current_face_indexes[0][0]],
                                self.__vertexes[current_face_indexes[0][1]],
                                self.__vertexes[current_face_indexes[0][2]], 
                                material=self.material, normals=normals
                            )
                        )
                    except Exception as e:
                        raise ValueError(f'Erro ao criar face com os índices especificados (algum índice de vértice é maior que o número de vértices). O erro ocorreu na linha {line_num + 1}:\n{line}') from e
    
        x_min = None
        x_max = None
        y_min = None
        y_max = None
        z_min = None
        z_max = None
        x_mean = 0
        y_mean = 0
        z_mean = 0

        for vertex in self.__vertexes:
            if x_min is None or vertex.x < x_min:
                x_min = vertex.x
            if x_max is None or vertex.x > x_max:
                x_max = vertex.x
            
            if y_min is None or vertex.y < y_min:
                y_min = vertex.y
            if y_max is None or vertex.y > y_max:
                y_max = vertex.y
            
            if z_min is None or vertex.z < z_min:
                z_min = vertex.z
            if z_max is None or vertex.z > z_max:
                z_max = vertex.z
            
            x_mean += vertex.x
            y_mean += vertex.y
            z_mean += vertex.z

        x_mean /= len(self.__vertexes)
        y_mean /= len(self.__vertexes)
        z_mean /= len(self.__vertexes)
        mass_center = Vec3([x_mean, y_mean, z_mean])

        # Delta x, y, z para fazer possivel futura escala do modelo
        delta_x = x_max - x_min
        delta_y = y_max - y_min
        delta_z = z_max - z_min

        # Posicionando o modelo no centro do mundo (0, 0, 0)
        self.translate(-mass_center)
        

    @property
    def vertexes(self):
        '''
        Retorna os vértices do modelo.

        ---

        Retorno:

            - list[Vec3] - Lista de vértices do modelo.
        '''
        return self.__vertexes
    
    @property
    def faces(self):
        '''
        Retorna as faces do modelo.

        Atualmente, cada triângulo é representado apenas pelos seus vértices, sem informações de textura ou normais.

        ---

        Retorno:

            - list[Triangle] - Lista de faces do modelo.
        '''
        return self.__faces
    
    @property
    def faces_indexes(self):
        '''
        Retorna os índices das faces do modelo.

        ---

        Retorno:

            - list[TriangleFaceIndexes] - Lista de índices das faces do modelo.
        '''
        return self.__faces_indexes

    def scale(self, scale_factor: float):
        '''
        Escala o modelo.

        ---

        Parâmetros:

            - scale_factor: float - Fator de escala.
        '''
        for vertex in self.__vertexes:
            vertex *= scale_factor
    
    def translate(self, translation_vector: Vec3):
        '''
        Translada o modelo.

        ---

        Parâmetros:

            - translation_vector: Vec3 - Vetor de translação.
        '''
        for vertex in self.__vertexes:
            vertex += translation_vector