#class Desempenho(placar_jogador_b, ranking_jogador_a, ranking_jogador_b, mesma_classe):
class Placar:
    primeiro_set_a = 0
    primeiro_set_b = 0
    segundo_set_a = 0
    segundo_set_b = 0
    terceiro_set_a = 0
    terceiro_set_b = 0

    def __init__(self, pontos_1a, pontos_1b, pontos_2a, pontos_2b, pontos_3a = 0, pontos_3b = 0):
        self.pontos_1a = pontos_1a
        self.pontos_1b = pontos_1b
        self.pontos_2a = pontos_2a
        self.pontos_2b = pontos_2b
        self.pontos_3a = pontos_3a
        self.pontos_3b = pontos_3b

        if 5 < self.pontos_1a:
            if self.pontos_1b < self.pontos_1a:
                self.primeiro_set_a = 1
                self.primeiro_set_b = 0
        else:
            if 5 < self.pontos_1b:
                self.primeiro_set_a = 0
                self.primeiro_set_b = 1

        if 5 < self.pontos_2a:
            if self.pontos_2b < self.pontos_2a:
                self.segundo_set_a = 1
                self.segundo_set_b = 0
        else:
            if 5 < pontos_2b:
                self.segundo_set_a = 0
                self.segundo_set_b = 1

        if self.pontos_3b < self.pontos_3a:
            if 9 < self.pontos_3a:
                self.terceiro_set_a = 1
                self.terceiro_set_b = 0
        else:
            if 9 < self.pontos_3b:
                self.terceiro_set_a = 0
                self.terceiro_set_b = 1

    def resultado(self):
        res_a = 0
        res_a = self.primeiro_set_a + self.segundo_set_a
        if res_a == 2:
            return 2
        elif res_a == 1:
            if res_a + self.terceiro_set_a == 2:
                return 1
            else:
                return -1
        else:
            return -2




class Desempenho:
    pontos_conquistados_a = 0
    pontos_conquistados_b = 0
    pontos_bonus_a = 0
    pontos_bonus_b = 0
    pontos_totais_a = 0
    pontos_totais_b = 0

    def __init__(self, placar_jogador_b, ranking_jogador_a, ranking_jogador_b):
        self.placar_jogador_b = placar_jogador_b
        self.ranking_jogador_a = ranking_jogador_a
        self.ranking_jogador_b = ranking_jogador_b

        if self.ranking_jogador_a > self.ranking_jogador_b:
            if self.placar_jogador_b == 0:
                self.pontos_conquistados_a = 16
                self.pontos_conquistados_b = 1
            else:
                self.pontos_conquistados_a = 13
                self.pontos_conquistados_b = 4

        if self.ranking_jogador_a == self.ranking_jogador_b:
            if self.placar_jogador_b == 0:
                self.pontos_conquistados_a = 15
                self.pontos_conquistados_b = 2
            else:
                self.pontos_conquistados_a = 12
                self.pontos_conquistados_b = 5

        if self.ranking_jogador_a < self.ranking_jogador_b:
            if self.placar_jogador_b == 0:
                self.pontos_conquistados_a = 14
                self.pontos_conquistados_b = 3
            else:
                self.pontos_conquistados_a = 11
                self.pontos_conquistados_b = 6

        if self.ranking_jogador_b == 1:
            self.pontos_bonus_a = 14

        elif self.ranking_jogador_b == 2:
            self.pontos_bonus_a = 12

        elif self.ranking_jogador_b == 3:
            self.pontos_bonus_a = 11

        elif self.ranking_jogador_b == 4:
            self.pontos_bonus_a = 10

        elif 4 < self.ranking_jogador_b < 9:
            self.pontos_bonus_a = 9

        elif 8 < self.ranking_jogador_b < 13:
            self.pontos_bonus_a = 8

        elif 12 < self.ranking_jogador_b < 17:
            self.pontos_bonus_a = 7

        elif 16 < self.ranking_jogador_b < 21:
            self.pontos_bonus_a = 6

        elif 20 < self.ranking_jogador_b < 27:
            self.pontos_bonus_a = 5

        else:
            self.pontos_bonus_a = 4

        self.pontos_totais_a = self.pontos_conquistados_a + self.pontos_bonus_a

        if self.ranking_jogador_a == 1:
            self.pontos_bonus_b = 10

        elif self.ranking_jogador_a == 2:
            self.pontos_bonus_b = 9

        elif self.ranking_jogador_a == 3:
            self.pontos_bonus_b = 8

        elif self.ranking_jogador_a == 4:
            self.pontos_bonus_b = 7

        elif 4 < self.ranking_jogador_a < 9:
            self.pontos_bonus_b = 6

        elif 8 < self.ranking_jogador_a < 13:
            self.pontos_bonus_b = 5

        elif 12 < self.ranking_jogador_a < 17:
            self.pontos_bonus_b = 4

        elif 16 < self.ranking_jogador_a < 21:
            self.pontos_bonus_b = 3

        elif 20 < self.ranking_jogador_a < 27:
            self.pontos_bonus_b = 2

        else:
            self.pontos_bonus_b = 1

        self.pontos_totais_b = self.pontos_conquistados_b + self.pontos_bonus_b

    def pontuar_a(self):
        return self.pontos_totais_a

    def pontuar_b(self):
        return self.pontos_totais_b
