import unittest
from main.nombreRomain import *

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

        # On a II
        self.assertEqual(romain , 'II')

    def test3(self):
        #Etant donné le chiffre 3
        nombre=3
        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a III
        self.assertEqual(romain , 'III')

    def test4(self):
        #Etant donné le chiffre 4
        nombre=4
        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a IV
        self.assertEqual(romain , 'IV')  

    def test5(self):
        #Etant donné le chiffre 5
        nombre=5
        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a V
        self.assertEqual(romain , 'V')

    def test6(self):
        #Etant donné le chiffre 6
        nombre=6
        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a VI
        self.assertEqual(romain , 'VI')

    def test7(self):
        #Etant donné le chiffre 7
        nombre=7
        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a VII
        self.assertEqual(romain , 'VII')
    
    def test8(self):
        #Etant donné le chiffre 8
        nombre=8
        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a VIII
        self.assertEqual(romain , 'VIII')

    def test9(self):
        #Etant donné le chiffre 9
        nombre=9
        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a IX
        self.assertEqual(romain , 'IX')

    def test10(self):
        #Etant donné le chiffre 10
        nombre=10
        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a X
        self.assertEqual(romain , 'X')

    def test11(self):
        #Etant donné le chiffre 11
        nombre=11
        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a XI
        self.assertEqual(romain , 'XI')

    def test12(self):
        #Etant donné le chiffre 12
        nombre=12
        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a XII
        self.assertEqual(romain , 'XII')

    def test13(self):
        #Etant donné le chiffre 13
        nombre=13

        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a XII
        self.assertEqual(romain , 'XIII')
 
    def test14(self):
        #Etant donné le chiffre 14
        nombre=14

        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a XIV
        self.assertEqual(romain , 'XIV')

    def test15(self):
        #Etant donné le chiffre 15
        nombre=15

        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a XV
        self.assertEqual(romain , 'XV')

    def test16(self):
        #Etant donné le chiffre 16
        nombre=16

        #quand on le converti en chiffre Romain
        romain=NombreRomain.convert(nombre)

        # On a XVI
        self.assertEqual(romain , 'XVI')
       
if __name__ == '__main__':
    unittest.main()