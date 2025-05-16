class Talaba:
    def __init__(self,tname,yonalish, kontrakt, viloyati, jinsi=None, kursi=0,):
        self.tname=tname
        self.kursi=kursi
        self.yonalish=yonalish
        self.kontrakt=kontrakt
        self.viloyati=viloyati
        self.jinsi=jinsi
    
    def get_info(self):
        info=f"{self.tname} {self.kursi}-bosqich {self.yonalish} talabasi"
        info+=f" Viloyat:{self.viloyati} Kontrakt:{self.kontrakt}mln so'm"
        if self.jinsi:
            info+=f" Jinsi:{self.jinsi}"
        else:
            raise ValueError('Jinsi nomalum shaxs')
        return info
    
    def set_course(self, course):
        self.course=course
        
    def get_contract(self):
        return self.contract
    def set_jins(self, newjins):
        self.jinsi=newjins
        return newjins
student=Talaba('Mamura Zakirovo', 'AX', 15, 'Namangan','Male')
student.set_course(3)
#print(student.get_info())
                       
        
        