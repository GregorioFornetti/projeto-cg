
from typing import Union
import numpy as np 
import PIL.Image
from lib.Image import Image


class ImageWriter:

    def __init__(self, image: Union[np.ndarray, PIL.Image.Image, Image]):
        '''
        Construtor da classe ImageWriter. Recebe um objeto ou uma matriz representando uma imagem, para ser posteriormente salva ou visualizada.

        --- 

        Parâmetros:

            - image: Union[np.ndarray, Image, Image.Image] - Imagem a ser salva ou visualizada. Pode ser um objeto PIL.Image ou uma matriz numpy. A matriz numpy pode possuir valores entre 0 e 1 e ser do tipo float ou ser uma matriz do tipo uint8. Pode ser também um objeto Image, que é uma classe definida no arquivo Image.py.
        '''
        if not isinstance(image, np.ndarray) and not isinstance(image, PIL.Image.Image) and not isinstance(image, Image):
            raise TypeError('A imagem precisa ser uma matriz numpy, um objeto PIL.Image ou um objeto Image.')
        
        if isinstance(image, np.ndarray):
            # Faz as conversões necessárias para que a imagem seja convertida para um objeto PIL.Image
            # Como o PIL não trabalho com floats entre 0 e 1, é preciso converter para inteiro, caso necessário
            if image.dtype != np.uint8:
                image = (image * 255).astype(np.uint8)
            self.image = PIL.Image.fromarray(image)
        elif isinstance(image, Image):
            if not image.all_pixels_set:
                raise ValueError('A imagem precisa ter todos os pixels definidos.')
            self.image = PIL.Image.fromarray(image.to_uint8_matrix())
        else:
            # Já é um objeto PIL.Image, não precisa fazer nenhum tratamento
            self.image = image
    
    def save(self, path: str, format: Union[str, None] = None):
        '''
        Salva a imagem em um arquivo.

        ---

        Parâmetros:
    
                - path: str - Caminho do arquivo a ser salvo.
    
                - format: Union[str, None] - Formato do arquivo a ser salvo. Se não for especificado, o formato será inferido a partir da extensão do arquivo.
        '''
        self.image.save(fp=path, format=format)
    
    def save_as_ppm(self, path: str):
        '''
        Salva a imagem em um arquivo PPM. Utiliza o algoritmo aprendido no tutorial para salvar o arquivo

        ---

        Parâmetros:
            
                - path: str - Caminho do arquivo a ser salvo.
        '''
        img_matrix = np.asarray(self.image)
        img_height, img_width, _ = img_matrix.shape

        with open(path, 'w') as img_file:
            # Cabeçalho do arquivo PPM
            img_file.write('P3\n')
            img_file.write(f'{img_width} {img_height}\n')
            img_file.write('255\n')

            # Corpo do arquivo PPM
            for i in range(img_height):
                for j in range(img_width):
                    ir = int(255.999 * img_matrix[i, j, 0])
                    ig = int(255.999 * img_matrix[i, j, 1])
                    ib = int(255.999 * img_matrix[i, j, 2])

                    img_file.write(f'{ir} {ig} {ib}\n')
        
    def display(self):
        '''
        Mostra a imagem na tela.
        '''
        self.image.show()


class ImageReader:
    
    def read_as_float_matrix(self, path: str) -> np.ndarray:
        '''
        Lê o arquivo de imagem e retorna uma matriz numpy representando a imagem.
        
        ---

        Parâmetros:

                - path: str - Caminho do arquivo a ser lido.

        ---

        Retorno:

                - np.ndarray - Matriz numpy representando a imagem. A matriz possui valores entre 0 e 1 e é do tipo float.
        '''
        img = PIL.Image.open(path)
        img_matrix = np.asarray(img)
        img_matrix = img_matrix / 255.0
        return img_matrix
    
    def read_as_uint8_matrix(self, path: str) -> np.ndarray:
        '''
        Lê o arquivo de imagem e retorna uma matriz numpy representando a imagem.
        
        ---

        Parâmetros:

                - path: str - Caminho do arquivo a ser lido.

        ---

        Retorno:

                - np.ndarray - Matriz numpy representando a imagem. A matriz possui valores entre 0 e 255 e é do tipo uint8.
        '''
        img = PIL.Image.open(path)
        img_matrix = np.asarray(img)
        img_matrix = img_matrix.astype(np.uint8)
        return img_matrix
        
    def read_as_pil_image(self, path: str) -> PIL.Image.Image:
        '''
        Lê o arquivo de imagem e retorna um objeto PIL.Image representando a imagem.
        
        ---

        Parâmetros:

                - path: str - Caminho do arquivo a ser lido.

        ---

        Retorno:

                - Image - Objeto PIL.Image representando a imagem.
        '''
        img = PIL.Image.open(path)
        return img