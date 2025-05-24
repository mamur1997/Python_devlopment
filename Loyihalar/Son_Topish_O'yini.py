import random as r
from pywebio.input import input
from pywebio.output import put_text, popup

def son_top(x):
    Qiymat=True
    while Qiymat:
        #kompyuter son o'ylaydi randint bilan uni chiqaradi
        put_text('\nKeling siz bilan son topish oyinini oynaymiz')
        put_text(f'Men 1 dan {x} gacha son oyladim topa olasizmi?')
        input('Agar boshlashni istasangiz enter bosing: ')
        attempts=0
        kom_soni=r.randint(1, x)
        while True:
            #while sikl ishlaydi u urunishlarni hisoblaydi va qoshib boradi
            attempts+=1
            try:
                taxmin=int(input('\nMen oylagan sonni taxmin qiling: '))
            except ValueError:
                print("\nIltimos butun son kiriting!!!")
                continue
            #if elif operatori siz taxmin qilgan sonni komp soni bilan solishtiradi
            if kom_soni>taxmin:
                put_text("Men o'ylagan son bundan kattaroq\n")
                
            elif kom_soni<taxmin:
                put_text("Men o'ylagan son bundan kichikroq\n")
                
            elif kom_soni==taxmin:
                put_text(f"\nTabriklaymiz siz topdingiz !!!")
                put_text(f"Jami urunishlar {attempts} marta")
                break


        put_text('Endi siz bilan boshqa oyin oynamoqchiman')
        put_text(f"Siz 1 dan {x} gacha son oylaysiz men topaman")
        input('Agar boshlashni istasangiz enter bosing: ')
        attempts1=0
        quyi=1
        yuqori=x

        while True:
            attempts1+=1
            natija=(quyi+yuqori)//2
            put_text(f"Siz oylagan son{natija} ")
            kirgaz=input(f"Agar Siz o'ylagan son meni taxminimdan kattaroq bo'lsa (+), kichikroq bo'lsa (-) va teng bo'lsa (t) bosing: ")       
            if kirgaz=='+':
                quyi=natija+1
            elif kirgaz=='-':
                yuqori=natija-1
            elif kirgaz=='t':
                put_text(f"\nMen topdim siz o'ylagan son {natija} ")
                put_text(f"Jami urunishlar {attempts1} marta")
                break
        if attempts>attempts1:
            put_text(f"Hisob: {attempts}>{attempts1} Sizning urunishlaringiz kamroq")
        elif attempts<attempts1:
            put_text(f"Hisob: {attempts}<{attempts1} Sizning urunishlaringiz ko'proq")
        else:
            put_text(f"Hisob: {attempts}={attempts1} Durrang")
        sorash=input('Yana oynamoqchimisiz? (ha/yoq): ')
        if sorash.lower()=='ha':
            Qiymat=True
        else:
            Qiymat=False
            put_text('Oyin tugadi')
            popup('Oyin tugadi', 'Oyin tugadi')
         
son_top(100)            

print()
