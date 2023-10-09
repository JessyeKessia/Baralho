import random
from carta import Carta
from naipe import Naipe
class Baralho:
    
    def __init__(self):
        self._criar_cartas()
        self._embaralhar()
    
    def __len__(self):
        return len(self.cartas)
    
    def _criar_cartas(self):
        self.cartas = []
        for naipe in Naipe:
            for valor in range(1, 14):
                self.cartas.append(
                    Carta(valor=valor, naipe=naipe)
                )
    
    def _embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir(self, *jogadores):
        if not 1 <= len(jogadores) <= 4:
            raise NumJogadoresInvalido(f'Valor={len(jogadores)}')

        quantidade = len(self) // len(jogadores)
        for i in range(len(jogadores)):
            jogadores[i].adicionar_cartas( 
                self.cartas[i * quantidade: (i + 1) * quantidade] 
            )