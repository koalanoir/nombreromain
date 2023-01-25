import unittest
from nombreRomain import *

class NombreRomainTest(unittest.TestCase):
    def test1(self):
        #Etant donné le chiffre 1
        nombre=1
        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a I
        self.assertEqual(romain , 'I')

    def test2(self):
        #Etant donné le chiffre 2
        nombre=2
        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a I
        self.assertEqual(romain , 'II')

    def test3(self):
        #Etant donné le chiffre 3
        nombre=3
        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a I
        self.assertEqual(romain , 'III')

if __name__ == '__main__':
    unittest.main()