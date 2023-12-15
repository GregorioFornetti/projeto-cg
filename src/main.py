
from Animation import Animation

possible_configs = {
    'low': {
        'image_width': 200,
        'samples_per_pixel': 10,
        'max_depth': 10
    },
    'medium': {
        'image_width': 400,
        'samples_per_pixel': 100,
        'max_depth': 50
    },
    'high': {
        'image_width': 1280,  # HD - 720p
        'samples_per_pixel': 100,
        'max_depth': 50
    }
}
possible_configs_keys = list(possible_configs.keys())

for i in range(len(possible_configs_keys)):
    print(f'[{i}] - {possible_configs_keys[i]}: {possible_configs[possible_configs_keys[i]]}')

config_index = int(input('Escolha uma configuração: '))

config = possible_configs[possible_configs_keys[config_index]]

animation = Animation(
    image_width=config['image_width'],
    samples_per_pixel=config['samples_per_pixel'],
    max_depth=config['max_depth']
)

start_frame = int(input('Digite o frame inicial: '))
end_frame = int(input('Digite o frame final: '))

for i in range(start_frame, end_frame + 1):
    print(f'Gerando frame {i}...')
    animation.generate_frame(i, f'frames/frame_{i}.png')