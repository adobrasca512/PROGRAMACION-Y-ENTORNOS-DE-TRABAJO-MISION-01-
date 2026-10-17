import unittest
from src.metricas import contar_aciertos, calcular_precision


class TestMetricas(unittest.TestCase):
    def test_cuenta_aciertos(self):
        self.assertEqual(contar_aciertos([1, 0, 1], [1, 1, 1]), 2)

    def test_rechaza_longitudes_distintas(self):
        with self.assertRaises(ValueError):
            contar_aciertos([1], [1, 0])

    def test_calcula_precision(self):
        self.assertAlmostEqual(calcular_precision([1, 0, 1], [1, 1, 1]), 2/3)

    def test_rechaza_longitudes_distintas_precision(self):
        with self.assertRaises(ValueError):
            calcular_precision([1], [1, 0])

    def test_rechaza_listas_vacias(self):
        with self.assertRaises(ValueError):
            calcular_precision([], [])
if __name__ == "__main__":
    unittest.main()
