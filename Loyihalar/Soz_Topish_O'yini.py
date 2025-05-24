from uzwords import words
import random as r
def Soz_top():
    
    matn=r.choice(words)
    uzunlik=len(matn)
    print(f"Men {uzunlik} harfli so'z oyladm topa alsizmi")
    chiziq=["-"] * uzunlik
    Get_Harf=[]
    attempts=0
    while "-" in chiziq:
        print("".join(chiziq))
        Harf=input("\nBironta Harf kirgazing: ").lower()
        attempts+=1
        if not Harf.isalpha():
            print('\nFaqat harf kiriting!!!')
            continue
        if len(Harf) !=1:
            print("\nIltimos faqat bitta harf kiriting!")
            continue
        if Harf in Get_Harf:
            print("\nBu harfni oldin kirgazgansiz! boshqa harf kirgazing... ")
            continue
        Get_Harf.append(Harf)
        if Harf in matn:
            for i in range(uzunlik):
                if matn[i]==Harf:
                    print(f"\n{Harf} harfi tog'ri")
                    chiziq[i]=Harf       
            
        else:

            print(f"\n{Harf}  Harf mavjud emas")
        print(f"Kiritilgan harflar: {''.join(Get_Harf).upper()} ")

    print(f"\nTabriklaymiz Siz topdingiz so'z: {matn.upper()}  \n{attempts} marta urundingiz  ")

Soz_top()


