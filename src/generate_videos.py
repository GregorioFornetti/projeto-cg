'''
Script para gerar os vídeos a partir dos frames gerados pelo código principal (main.py)
'''

import cv2
import os
from resolutions import resolutions
from tqdm import tqdm


frames_folder = 'animation_frames/'
possible_resolutions = list(resolutions.keys())

for folder_name in possible_resolutions:
    # Código adaptado de: https://stackoverflow.com/a/44948030

    image_folder = os.path.join(frames_folder, folder_name)
    if not os.path.exists(image_folder):
        continue

    video_name = f'animations/{folder_name}.avi'
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort(key= lambda file: int(file.split('_')[1].split('.')[0]))  # Ordenando as imagens pelo número do frame (por padrão, a ordenação por string não dá certo)
    if len(images) == 0:
        continue
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 24, (width,height))

    print(f'Gerando vídeo para a animação {folder_name}')
    for image in tqdm(images):
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()
    print(f'Vídeo gerado para a animação {folder_name}\n\n')

final_video_name = 'animations/final_video.avi'
final_video = cv2.VideoWriter(final_video_name, 0, 24, (1280, 720)) # HD

print('Gerando vídeo final...')
for folder_name in tqdm(possible_resolutions):
    image_folder = os.path.join(frames_folder, folder_name)
    if not os.path.exists(image_folder):
        continue

    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort(key= lambda file: int(file.split('_')[1].split('.')[0]))  # Ordenando as imagens pelo número do frame (por padrão, a ordenação por string não dá certo)
    if len(images) == 0:
        continue

    for image in images:
        current_image = cv2.imread(os.path.join(image_folder, image))
        height, width = current_image.shape[:2]
        width = current_image.shape[1]
        rescaled_image = cv2.resize(current_image, (1280, 720), interpolation=cv2.INTER_AREA)

        text_color = (0, 0, 0)
        # Write folder_name in the top left corner
        cv2.putText(rescaled_image, folder_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)
        # Write configuration in the top right corner
        cv2.putText(rescaled_image, f'Largura: {width}', (700, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)
        cv2.putText(rescaled_image, f'Altura: {height}', (700, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)
        cv2.putText(rescaled_image, f'Raios por pixel: {resolutions[folder_name]["samples_per_pixel"]}', (950, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)
        cv2.putText(rescaled_image, f'Profundidade: {resolutions[folder_name]["max_depth"]}', (950, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)
        final_video.write(rescaled_image)

cv2.destroyAllWindows()
final_video.release()

print('Vídeo final gerado.')