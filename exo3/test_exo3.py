import unittest

from exo3 import processLines


class TestExo3(unittest.TestCase):
    def test_input_1(self):
        with open("C:\\Users\\windows\\Downloads\\2A\\TDLOG\\clone\\tdlog_exercices\\exo3\\sample\\input1.txt") as input1:
            lines = input1.readlines()

        with open("C:\\Users\\windows\\Downloads\\2A\\TDLOG\\clone\\tdlog_exercices\\exo3\\sample\\output1.txt") as output1:
            expected = output1.read()

        self.assertEqual(expected, processLines(lines))

    def test_input_2(self):
        # Lire les données d'entrée du fichier input2.txt
        with open("C:\\Users\\windows\\Downloads\\2A\\TDLOG\\clone\\tdlog_exercices\\exo3\\sample\\input2.txt") as input2:
            lines = input2.readlines()

        # Lire le résultat attendu du fichier output2.txt
        with open("C:\\Users\\windows\\Downloads\\2A\\TDLOG\\clone\\tdlog_exercices\\exo3\\sample\\output2.txt") as output2:
            expected = output2.read().strip()  # .strip() pour enlever les espaces ou sauts de ligne

        # Vérifier que la sortie du programme est égale au résultat attendu
        self.assertEqual(expected, processLines(lines))

if __name__ == '__main__':
    unittest.main()
