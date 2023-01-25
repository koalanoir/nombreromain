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

    def test4(self):
        #Etant donné le chiffre 4
        nombre=4
        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a I
        self.assertEqual(romain , 'IV')  

    def test5(self):
        #Etant donné le chiffre 5
        nombre=5
        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a I
        self.assertEqual(romain , 'V')

    def test6(self):
        #Etant donné le chiffre 6
        nombre=6
        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a I
        self.assertEqual(romain , 'VI')

    def test7(self):
        #Etant donné le chiffre 7
        nombre=7
        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a I
        self.assertEqual(romain , 'VII')
    
    def test8(self):
        #Etant donné le chiffre 8
        nombre=8
        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a I
        self.assertEqual(romain , 'VIII')
        
if __name__ == '__main__':
    unittest.main()