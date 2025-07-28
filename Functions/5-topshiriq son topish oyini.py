#Funksiyalar yordamida Son topish oyinini yasang unda foydalanuvchi
#Hamda kompyuter son oylasin va ular bir birini taxmin qilib topishsin
 
import random as r
def son_top1(x):
    qiymat=True
    while qiymat:
        print(f"\n1 dan {x} gacha son o'yladim topa olasizmi?")
        qiymat=r.randint(1, x)
        attempts=0
        while True:
            son=int(input("Ixtiyoriy sonni kiritng: "))
            attempts+=1
            if son>qiymat:
                print("\nKichikroq sonni kiriting !!!")
            elif son<qiymat:
                print("\nKattaroq sonni kiriting !!")
            elif son == qiymat:
                print(f"Siz togri topdingiz. ({son}) men oylagan son ")
                print(f"Urunishlaringiz {attempts} marta")
                break
    
        print(f"\n\nKeling endi almashamiz Siz o`ylang men topaman"
            f"\n1 dan {x} gacha son oylang, men taxmin qilib koraman: ")
        input("Boshlash uchun ixtiyoriy tugmani bosing:")
        
        attempts2=0
        past=1
        yuqori=x
        while True:
            attempts2+=1
            n1=(past+yuqori) //2
            kiritish=input(f"\nJavob:{n1} Siz tanlagan son. \nAgarda siz tanlagan son:"
                  f"\n Rost bolsa(R)\n Kattaroq bolsa (+)\n Kichik bolsa(-)"
                  ).lower()
            if kiritish =="+":
                past=n1+1
                
            elif kiritish=="-":
                yuqori=n1-1
                
            elif kiritish=="r":
                print(f"\n{n1} siz o`ylagan son. Men topdim")
                print(f"{attempts2} marta urundim")
                break
        if attempts>attempts2:
            print(f"Hisob: {attempts}-{attempts2} Siz Yutqazdingiz")
        elif attempts<attempts2:
            print(f"Hisob: {attempts}-{attempts2} Siz Yutdingiz")
        else:
            print(f"Hisob: {attempts}-{attempts2} Durrang") 
        sorash=input("Oyinni davom ettirasizmi ha/yoq: ").lower()
        if sorash=='yoq':
             qiymat=False
    return None
son_top1(100)            
            
            
            
            
            
            
            
            
            
            
            
            
            
            