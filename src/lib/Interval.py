
class Interval:
    """
    .. automethod:: __contains__
    """

    def __init__(self, min: float, max: float):
        '''
        Construtor de um intervalo. Delimita um intervalo de valores possíveis.

        ---

        Parâmetros:

            - min: float - Valor mínimo do intervalo. Para estar dentro do intervalo, o valor deve ser maior ou igual a esse valor.

            - max: float - Valor máximo do intervalo. Para estar dentro do intervalo, o valor deve ser menor ou igual a esse valor.
        '''
        self.__min = min
        self.__max = max
    
    @property
    def min(self):
        '''
        Valor mínimo do intervalo. Para estar dentro do intervalo, o valor deve ser maior ou igual a esse valor.
        '''
        return self.__min
    
    @property
    def max(self):
        '''
        Valor máximo do intervalo. Para estar dentro do intervalo, o valor deve ser menor ou igual a esse valor.
        '''
        return self.__max

    def __contains__(self, value: float):
        '''
        Verifica se o valor está dentro do intervalo.

        Exemplo:

        >>> interval = Interval(0, 10)
        >>> 5 in interval  # 0 <= 5 <= 10
        True
        >>> 15 in interval # 15 > 19
        False
        >>> -1 in interval # -1 < 0
        False
        >>> 0 in interval  # 0 <= 0 <= 10
        True

        ---

        Parâmetros:

            - value: float - Valor a ser verificado.
        
        ---

        Retorno:
            
            - bool - True se o valor está dentro do intervalo, False caso contrário.
        '''
        return self.min <= value <= self.max
    
    def surrounds(self, value: float):
        '''
        Verifica se o valor está dentro do intervalo.

        Exemplo:

        >>> interval = Interval(0, 10)
        >>> interval.surrounds(5)  # 0 <= 5 <= 10
        True
        >>> interval.surrounds(15)
        False
        >>> interval.surrounds(-1)
        False
        >>> interval.surrounds(0)
        True

        ---

        Parâmetros:

            - value: float - Valor a ser verificado.
        
        ---

        Retorno:

            - bool - True se o valor está dentro do intervalo, False caso contrário.
        '''
        return self.min <= value <= self.max
    
    def clamp(self, value: float):
        '''
        Retorna o valor se ele estiver dentro do intervalo, ou o valor mínimo ou máximo caso contrário.

        Exemplo:

        >>> interval = Interval(0, 10)
        >>> interval.clamp(5)
        5

        >>> interval.clamp(15)
        10

        >>> interval.clamp(-1)
        0

        >>> interval.clamp(0)
        0

        ---

        Parâmetros:
            
                - value: float - Valor a ser verificado.

        ---

        Retorno:

            - float - O valor se ele estiver dentro do intervalo, ou o valor mínimo ou máximo caso contrário.
        '''
        if value < self.min:
            return self.min
        if value > self.max:
            return self.max
        return value