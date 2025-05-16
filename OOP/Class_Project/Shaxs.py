class Shaxs:
    def __init__(self, name, surname, year, profession=None, boyligi=0):
        self.name=name
        self.surname=surname
        self.born=year
        self.profession=profession
        self.__wealth=boyligi
    
    def get_info(self):
        info=f"{self.name} {self.surname} {self.born}-yil"
        info+=f" Boyligi:{self.__wealth}mln so'm"
        
        if self.profession:
            info+=f" Kasbi:{self.profession}"
        return info
    def add_wealth(self, money):
        if money>=0:
            self.__wealth+=money
        else:
            raise ValueError('Musbat kiriting chunki qarzdor emas')
    
    def set_profession(self, profess):
        self.profession=profess
        
    def get_wealth(self):
        return self.__wealth
            
people=Shaxs('Mamur', 'Zokirov', 1997)
people.add_wealth(50)
people.set_profession('Dasturchi')

#print(people.get_info())
        