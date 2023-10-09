from naipe import Naipe

class Carta:
    AS = 1
    VALETE = 11
    RAINHA = 12
    REI = 13
    
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor
        self.nome = self._get_nome()

    def _get_nome(self):
        match self.valor:
            case 1:
                return "Ás"
            case x if 2 <= x <= 10:
                return str(self.valor)
            case 11:
                return "Valete"
            case 12:
                return "Rainha"
            case 13:
                return "Rei"
            case _:
                raise ValueError("valor inválido")
            
    def __str__(self):
        return f'{self.nome} de {self.naipe.name.title()}'
    
    def __repr__(self):
        return f'Carta({self})'
    
    def __lt__(self, outra_carta: 'Carta') -> bool:
        return self.valor < outra_carta.valor
    
    def __eq__(self, outra_carta: 'Carta') -> bool:
        return self.valor == outra_carta.valor


