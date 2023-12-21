'''
Código para verificar quais frames estão faltando nas animações
'''

import os
from resolutions import resolutions

frames_per_animation = 120
frames_folder = 'animation_frames/'
possible_resolutions = list(resolutions.keys())

for folder_name in possible_resolutions:
    image_folder = os.path.join(frames_folder, folder_name)
    if not os.path.exists(image_folder):
        os.mkdir(image_folder)

    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

    missing_frames = []
    for i in range(frames_per_animation):
        if f'frame_{i}.png' not in images:
            missing_frames.append(i)
    
    print(f'Progresso da animação {folder_name}: {len(images)/frames_per_animation * 100:.2f} %')

    if len(missing_frames) > 0:
        print(f'Faltam os seguintes frames para a animação {folder_name}:')
        print(missing_frames)
        print('\n')