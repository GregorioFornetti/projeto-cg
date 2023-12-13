'''
    Funções utilitárias que podem ser necessárias em qualquer parte do código.
'''

from lib.constants import pi
import random


def degrees_to_radians(degrees: float):
    '''
    Converte um ângulo de graus para radianos.

    ---

    Parâmetros:

        - degrees: float - Ângulo em graus.
    
    ---

    Retorno:

        - float - Ângulo em radianos.
    '''
    return degrees * pi / 180.0

def random_double():
    '''
    Gera um número aleatório entre 0 e 1.

    ---

    Retorno:

        - float - Número aleatório entre 0 e 1.
    '''
    return random.random()

def random_double_range(min: float, max: float):
    '''
    Gera um número aleatório entre min e max.

    ---

    Parâmetros:

        - min: float - Valor mínimo.
        - max: float - Valor máximo.
    
    ---

    Retorno:

        - float - Número aleatório entre min e max.
    '''
    return min + (max - min) * random_double()
