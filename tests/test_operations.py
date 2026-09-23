
import unittest
import operations

class TestOperations(unittest.TestCase):

    #Operations simples

    def test_addition(self):
        resultat = operations.addition(2, 3)
        self.assertEqual(resultat, 5)

    def test_soustraction(self):
            resultat = operations.soustraction(5, 3)
            self.assertEqual(resultat, 2)

    def test_multiplication(self):
            resultat = operations.multiplication(2, 3)
            self.assertEqual(resultat, 6)

    def test_division(self):
            resultat = operations.division(10, 2)
            self.assertEqual(resultat, 5)

    def test_modulo(self):
            resultat = operations.modulo(10, 2)
            self.assertEqual(resultat, 0)

    def test_puissance(self):
            resultat = operations.puissance(2, 3)
            self.assertEqual(resultat, 8)

    def test_division_par_zero(self):
           with self.assertRaises(ValueError):
                operations.division(10, 0)

    #operations complexes
    def test_racine(self):
          self.assertEqual(operations.racine_carre(25), 5)

    def test_valeur_absolue(self):
          self.assertEqual(operations.valeur_absolue(-12), 12)

    def test_pourcentage(self):
          self.assertEqual(operations.pourcentage(100, 20), 20)

    def test_augmentation(self):
          self.assertEqual(operations.augmentation(100, 20), 120)

    def test_reduction(self):
          self.assertEqual(operations.reduction(100, 20), 80)

    def test_factorielle(self):
          self.assertEqual(operations.factorielle(3), 6)

    def test_cosinus(self):
          self.assertEqual(operations.cosinus(0), 1)

    def test_sinus(self):
          self.assertEqual(operations.sinus(90), 1)

    def test_tangente(self):
          self.assertEqual(operations.tangente(0), 0)

    def test_logarithme(self):
          self.assertEqual(operations.logarithme(10), 1)

    def test_logarithme_neperien(self):
          self.assertEqual(operations.logarithme_neperien(1), 0)

    def test_exponentielle(self):
          self.assertEqual(operations.exponentielle(0), 1)


     

if __name__ == "__main__":
    unittest.main()

