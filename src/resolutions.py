'''
Configurações de resolução de animações disponíveis no sistema.
'''

resolutions = {
    'test': {
        'image_width': 100,
        'samples_per_pixel': 1,
        'max_depth': 5
    },
    'very-very-low': {
        'image_width': 100,
        'samples_per_pixel': 5,
        'max_depth': 10
    },
    'very-low': {
        'image_width': 200,
        'samples_per_pixel': 5,
        'max_depth': 10
    },
    'low': {
        'image_width': 200,
        'samples_per_pixel': 10,
        'max_depth': 10
    },
    'medium-low': {
        'image_width': 200,
        'samples_per_pixel': 50,
        'max_depth': 20
    },
    'medium-low+': {
        'image_width': 400,
        'samples_per_pixel': 50,
        'max_depth': 20
    },
    'medium': {
        'image_width': 400,
        'samples_per_pixel': 100,
        'max_depth': 50
    },
    'high': {
        'image_width': 1280,  # HD - 720p
        'samples_per_pixel': 20,
        'max_depth': 50
    }
}