#Classlar yordamida obyektlar hosil qiling va ularni boshqaring

class Avtolar:
    def __init__(self, model,rang,karobka,narx,yil):
        self.model=model
        self.color=rang
        self.technical=karobka
        self.price=narx
        self.year=yil
        self.km=0
    def get_model(self):
        return self.model
    def get_color(self):
        return self.color
    def get_technical(self):
        return self.technical
    def get_price(self):
        return self.price
    def get_year(self):
        return self.year
    def newyear(self, newyil):
        self.year=newyil
    def new_km(self):
        self.km+=100
    def full_info(self):
        return f"Mashina modeli:{self.model} Mashina rangi:{self.color}"
        f" Mashina carobkasi: {self.technical}"
        f"Mashina narxi:{self.price}$ Mashina yili:{self.year}-yil Mashina probegi: {self.km}km"
class Avtosalon:
    def __init__(self, salon_nomi):
        self.name=salon_nomi
        self.sotilgan_avto=0
        self.jami_avtolar=[]
        
    def add_car(self,newcar):
        self.jami_avtolar.append(newcar)
        self.sotilgan_avto+=1
    def get_cars(self):
        return [newcar.full_info() for newcar in self.jami_avtolar]

avto1=Avtolar('bmw', 'white', 'automatic', 70000, 2025)
avto2=Avtolar('ferrari', 'red', 'mechanic', 170000, 2024)
avto3=Avtolar('lamborghini', 'titanium', 'automatic', 270000, 2023)
avto4=Avtolar('gentra', 'black', 'mechanic', 15000, 2022)

car1=Avtosalon('Yangi mashina bozori')
car1.add_car(avto1)
car1.add_car(avto2)
car1.add_car(avto3)
car1.add_car(avto4)

print(car1.get_cars())











