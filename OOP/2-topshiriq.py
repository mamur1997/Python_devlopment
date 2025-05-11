class Talaba:
    def __init__(self, ism,familiya,kurs,yonalish,):
        self.name=ism
        self.surname=familiya
        self.level=kurs
        self.yonalish=yonalish
        
    def __repr__(self):
        return f"{self.name} {self.surname} {self.level}-bosqich {self.yonalish} talabasi"

class Fan:
    def __init__(self):
        self.fanga_oid_talabalar=[]
    
    def __repr__(self):
        return f"{self.fanga_oid_talabalar}"
    
    def add_student(self, *qiymat):
        for n in qiymat:
            if isinstance(n, Talaba):
                self.fanga_oid_talabalar.append(n)
            else:print("faqat talaba sinfigi oid obyekt kirgazing")
            
    def __getitem__(self,index):
        return self.fanga_oid_talabalar[index]
    
    def __setitem__(self,index,value):
        self.fanga_oid_talabalar[index]=value
    
    def __len__(self):
        return len(self.fanga_oid_talabalar)
    

    def __call__(self,*param):
        if param:
            self.add_student(*param)
        else:
            return self.fanga_oid_talabalar
       
    
t1=Talaba('Mamur', 'Zakirov', 4, 'Telekom')
t2=Talaba('Qodir', 'Tolipov', 3, 'KIF')
t3=Talaba('Sobir', 'Rahimov', 2, 'AX')
t4=Talaba('Bobir', 'Xoliqov', 1, 'DIF')
t5=Talaba('John','Cena','Magistr','AI-Data-science')

fan=Fan()
fan.add_student(t1,t2,t3,t4) #// add_student metodi bilan qoshish

print(fan[1])    #//__get__item metodi

change=fan[0]=t5
print (fan[0])    #// __setitem__metodi

print(len(fan))   #//__len__ metodi

print(fan())      #// __call__ metodi


















