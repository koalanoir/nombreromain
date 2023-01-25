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

if __name__ == '__main__':
    unittest.main()