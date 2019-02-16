from django.test import TestCase

# Create your tests here.
from .regras import Desempenho


class DesempenhoTests(TestCase):

    def test_pontuar_desempenho_0_primeiro_sobre_segundo(self):
        d = Desempenho (0, 1, 2)
        self.assertIs(d.pontuar_a(), 26)

    def test_pontuar_desempenho_0_primeiro_sobre_terceiro(self):
        d = Desempenho (0, 1, 3)
        self.assertIs(d.pontuar_a(), 25)

    def test_pontuar_desempenho_0_primeiro_sobre_quarto(self):
        d = Desempenho (0, 1, 4)
        self.assertIs(d.pontuar_a(), 24)

    def test_pontuar_desempenho_0_primeiro_sobre_quinto(self):
        d = Desempenho (0, 1, 5)
        self.assertIs(d.pontuar_a(), 23)

    def test_pontuar_desempenho_0_primeiro_sobre_vigesimo(self):
        d = Desempenho (0, 1, 20)
        self.assertIs(d.pontuar_a(), 20)

    def test_pontuar_desempenho_1_primeiro_sobre_segundo(self):
        d = Desempenho (1, 1, 2)
        self.assertIs(d.pontuar_a(), 23)

    def test_pontuar_desempenho_0_primeiro_sobre_segundo_b(self):
        d = Desempenho (0, 1, 2)
        self.assertIs(d.pontuar_b(), 13)

    def test_pontuar_desempenho_0_primeiro_sobre_terceiro_b(self):
        d = Desempenho (0, 2, 3)
        self.assertIs(d.pontuar_b(), 12)

    def test_pontuar_desempenho_1_primeiro_sobre_segundo_b(self):
        d = Desempenho (1, 1, 2)
        self.assertIs(d.pontuar_b(), 16)
