import random
from enum import Enum

class BaralhoException(Exception):
    pass

class NumJogadoresInvalido(BaralhoException):
    pass

class Naipe(Enum):
    OUROS = 1
    PAUS = 2
    COPAS = 3
    ESPADAS = 4

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


class Jogo:

    def __init__(self, nome_jogador_1: str, nome_jogador_2: str):
        self.baralho = Baralho()
        self.montante = []
        self.jogador_1 = Jogador(nome_jogador_1)
        self.jogador_2 = Jogador(nome_jogador_2)
        self.baralho.distribuir(self.jogador_1, self.jogador_2)
        self.numero_maximo_jogadas = 10
        self.numero_jogada = 0

    @property
    def acabou_por_cartas(self):
        return self.jogador_1.sem_cartas or self.jogador_2.sem_cartas
    
    @property
    def acabou_por_jogadas(self):
        return self.numero_jogada >= self.numero_maximo_jogadas
    
    @property
    def jogo_acabou(self):
        return self.acabou_por_cartas or self.acabou_por_jogadas
    
    def receber_montante(self, jogador: Jogador):
        if self.montante:
            jogador.adicionar_cartas(self.montante)
            self.montante = []
    
    def jogar(self):
        while not self.jogo_acabou:
            self.numero_jogada += 1
            # input()
            print(f"Rodada #{self.numero_jogada}")
            print(f"Placar {self.jogador_1}={len(self.jogador_1.deck)} vs {self.jogador_2}={len(self.jogador_2.deck)}")
            carta_1 = self.jogador_1.pegar_carta()
            print(f'{self.jogador_1} pegou {carta_1}')
            carta_2 = self.jogador_2.pegar_carta()
            print(f'{self.jogador_2} pegou {carta_2}')

            self.montante.extend([carta_2, carta_1])

            vencedor_rodada = None
            if carta_1 > carta_2:
                vencedor_rodada = self.jogador_1
            elif carta_2 > carta_1:
                vencedor_rodada = self.jogador_2
            else:
                continue

            if vencedor_rodada:
                self.receber_montante(vencedor_rodada)
                print(f"{vencedor_rodada} ganhou a rodada.")


        if len(self.jogador_1.deck) > len(self.jogador_2.deck):
            vencedor = self.jogador_1
        else:
            vencedor = self.jogador_2

        print(f"Jogador {vencedor} ganhou o jogo.")



jogo = Jogo("Rodrigo", "Pinheiro")
jogo.jogar()