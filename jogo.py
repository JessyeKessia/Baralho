from jogador import Jogador
from baralho import Baralho
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