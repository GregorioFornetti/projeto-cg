'''
Script para gerar os vídeos a partir dos frames gerados pelo código principal (main.py)
'''


# Código adaptado de: https://stackoverflow.com/a/44948030

import cv2
import os
from resolutions import resolutions


frames_folder = 'animation_frames/'
possible_resolutions = list(resolutions.keys())

for folder_name in possible_resolutions:
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

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

final_video_name = 'animations/final_video.avi'
final_video = cv2.VideoWriter(final_video_name, 0, 24, (1280, 720)) # HD

for folder_name in possible_resolutions:
    image_folder = os.path.join(frames_folder, folder_name)
    if not os.path.exists(image_folder):
        continue

    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort(key= lambda file: int(file.split('_')[1].split('.')[0]))  # Ordenando as imagens pelo número do frame (por padrão, a ordenação por string não dá certo)
    if len(images) == 0:
        continue

    for image in images:
        current_image = cv2.imread(os.path.join(image_folder, image))
        rescaled_image = cv2.resize(current_image, (1280, 720), interpolation=cv2.INTER_AREA)
        final_video.write(rescaled_image)

cv2.destroyAllWindows()
final_video.release()