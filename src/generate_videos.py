'''
Script para gerar os vídeos a partir dos frames gerados pelo código principal (main.py)
'''


# Código adaptado de: https://stackoverflow.com/a/44948030

import cv2
import os

# Set the directory path
frames_folder = 'animation_frames/' 

for folder_name in os.listdir(frames_folder):
    image_folder = os.path.join(frames_folder, folder_name)
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