import unittest
from Shaxs import Shaxs
from Talaba import Talaba
class Test_Shaxs(unittest.TestCase):
    #Shaxs uchun SetUp
    def setUp(self):
        name='Qodir'
        surname='Tolipov'
        born=2000
        self.profession='Bloger'
        self.boyligi=20
        self.shaxs1= Shaxs(name, surname, born)
        self.shaxs2= Shaxs(name, surname, born, profession=self.profession) 
        
    def test_shaxs(self):
        self.assertIsNotNone(self.shaxs1.name)
        self.assertIsNotNone(self.shaxs1.surname)
        self.assertIsNotNone(self.shaxs1.born)
        
    def test_profession(self):
        self.shaxs1.set_profession(self.profession)
        self.assertEqual(self.profession, self.shaxs1.profession)
        
    def test_set_Wealth(self):
        self.shaxs1.add_wealth(20)
        self.assertEqual(self.boyligi, self.shaxs1.get_wealth())
        
    def test_get_info(self):
        self.shaxs1.set_profession(self.profession)
        self.shaxs1.add_wealth(self.boyligi)
        set_name1="Qodir Tolipov 2000-yil Boyligi:20mln so'm Kasbi:Bloger"
        self.assertEqual(set_name1, self.shaxs1.get_info())
      
class Test_Talaba(unittest.TestCase):
        #Talaba uchun SetUp   
    def setUp(self):
        tname='Mamur'
        viloyati='Namangan'
        kontrakt=18
        yonalish='AX'
        kontrakt=17
        self.course=4
        self.jins='Female'
        self.talaba1 = Talaba(tname, yonalish, kontrakt, viloyati)
        
    def test_talaba(self):
         self.assertIsNotNone(self.talaba1.viloyati)
         self.assertIsNotNone(self.talaba1.tname)
         self.assertIsNotNone(self.talaba1.yonalish)
         self.assertIsNotNone(self.talaba1.kontrakt)
         
    def test_course(self):
        self.talaba1.set_course(self.course)
        self.assertEqual(self.course, self.talaba1.course)
        
    def test_jins(self):
        self.assertEqual(self.jins, self.talaba1.set_jins(self.jins))
        
    def test_get_info(self):
        talaba_Full_name="Mamur 0-bosqich AX talabasi Viloyat:Namangan Kontrakt:17mln so'm Jinsi:Female"
        self.talaba1.set_jins(self.jins)
        self.assertEqual(talaba_Full_name, self.talaba1.get_info())

unittest.main()
 
