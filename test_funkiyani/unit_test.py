# Funksiyani test qilish 
#Asqarov Azizbek 01.10.2025-yil

import unittest
from name import get_full_name
class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        name = get_full_name('azizbek','asqarov')
        self.assertEqual(name,'Azizbek Asqarov')

unittest.main()