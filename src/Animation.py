from lib.HittableList import HittableList
from lib.objects.Model import Model
from lib.objects.Sphere import Sphere
from lib.materials.Metal import Metal
from lib.materials.Lambertian import Lambertian
from lib.vec.Vec3 import Vec3, Point3, Color
from lib.Camera import Camera

class Animation:

    def __init__(self, image_width: int, samples_per_pixel: int, max_depth: int):
        '''
        Construtor da animação. A animação consiste em um cubo metálico (reflexivo) no centro (0,0,0) e ao redor dele terão duas esferas difusas que giram em torno do cubo. A câmera também gira em torno do cubo.

        ---

        Parâmetros:

            - image_width: int - Largura da imagem em pixels.

            - samples_per_pixel: int - Quantidade de amostras (raios) por pixel.

            - max_depth: int - Quantidade máxima de reflexões/refrações de um raio.
        '''
        self.image_width = image_width
        self.samples_per_pixel = samples_per_pixel
        self.max_depth = max_depth
        
        # Configurações da animação:
        self.FRAMES_PER_SECOND = 24
        self.ANIMATION_DURATION = 5  # Em segundos
        self.SPHERES_ROTATION_SPEED = 2 / 5  # A cada 5 segundos, as esferas dão 2 voltas
        self.CAMERA_ROTATION_SPEED = 1 / 5  # A cada 5 segundos, a câmera se move 1 

        # Construindo a cena inicial:
        self.cube = Model("objs/Cube.obj", Metal(Color([0.7, 0.7, 0.7]), 0.0))

        self.first_sphere = Sphere(
            Point3([-2, 0, 0]),
            0.5,
            Lambertian(Color([0.9, 0.3, 0.3]))
        )
        self.second_sphere = Sphere(
            Point3([2, 0, 0]),
            0.5,
            Lambertian(Color([0.3, 0.3, 0.9]))
        )
        self.floor = Sphere(
            Point3([0, -100.5, -1]), 
            100,
            Lambertian(Color([0.5, 1, 0.5]))
        )

        self.camera_initial_position = Point3([0, 2, 5])

        self.camera = Camera(
            image_width=self.image_width,
            samples_per_pixel=self.samples_per_pixel,
            max_depth=self.max_depth,
            vfov=40,
            lookfrom=self.camera_initial_position,
            lookat=Point3([0, 0, 0]),
            vup=Vec3([0, 1, 0])
        )
    
    def generate_frame(self, frame_number: int, save_path: str):
        '''
        Gera um frame da animação.

        ---

        Parâmetros:

            - frame_number: int - Número do frame atual.

            - save_path: str - Caminho para salvar a imagem.
        '''
        # Calculando o tempo atual da animação:
        current_time = frame_number / self.FRAMES_PER_SECOND

        # Atualizando posição da camera
        self.camera.lookfrom = self.camera_initial_position.rotate(
            'y', current_time * self.CAMERA_ROTATION_SPEED * 360
        )

        # Atualizando posição das esferas
        new_first_sphere = self.first_sphere.rotate(
            'y', current_time * self.SPHERES_ROTATION_SPEED * 360
        )

        new_second_sphere = self.second_sphere.rotate(
            'y', current_time * self.SPHERES_ROTATION_SPEED * 360
        )

        # Criando a cena
        world = HittableList()
        world.add(self.cube)
        world.add(new_first_sphere)
        world.add(new_second_sphere)
        world.add(self.floor)

        # Renderizando a imagem
        self.camera.render(world, save_path)

