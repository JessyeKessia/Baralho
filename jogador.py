from carta import Carta
class Jogador:
    
    def __init__(self, nome):
        self.nome = nome
        self.deck = []

    def __repr__(self):
        return f'Jogador({self.nome})'
    
    def adicionar_cartas(self, cartas):
        self.deck.extend(cartas)

    def adicionar_carta(self, carta: Carta):
        self.deck.append(carta)

    def pegar_carta(self) -> Carta:
        return self.deck.pop(0)
    
    @property
    def sem_cartas(self):
        return len(self.deck) == 0