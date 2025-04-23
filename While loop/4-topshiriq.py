 #Shunday dastur tuzingki 1- bolib sizdan E_bozor uchun mavjud
#mahsulotlarni kiritishni so'rasin. Undan kegin sizdan Buyurtma uchun
#mahsulotlarni so`rasin va agar buyurtma qilgan mahsulotlaringiz E_bozor
#uchun yozilgan lugatlarda bolsa. Unda lug'atda bor royhatlarni
#narxi bilan aks holda mavjud emas deb mavjud emaslarni chiqaring

print("\nBozor uchun dastur")
E_Bozor={}
n=0
Qiymat=True
while Qiymat:
        Items=input(f"{n+1}-mahsulot nomini kiriting: ").title()
        Price=int(input("Mahsulotni narxini kirgazing: "))
        E_Bozor[Items]=Price
        n+=1
        asking=input("\nDastur ni ishlatishni xoxlysizmi Ha/Yoq: \n").lower()
        if asking != 'ha':
            break
print("\nE_Bozor uchun royhatlar: \n")
print(E_Bozor)
        
print("\nBuyurtma uchun dastur")
Recieve=[]
n=0
while True:
        Items=input(f"{n+1}- Mahsulot nomini kiriting: ")
        Recieve.append(Items.title())
        n+=1
        Repeat=input("Dasturni davom ettirish uchun (Ha)" 
                 "aks xolda (Yoq) ni kiriting: ").lower()
        if Repeat == 'yoq':
            break
              
print("Buyurtma uchun mahsulotlaringiz: ")
for i in Recieve:
        print(i.title())  
print("\nE_Bozorda bor mahsulotlar\n")
for i,n in E_Bozor.items():
    if i in Recieve:
        print(f"{i} - {n} so`m")
print("\nE_Bozorda yoq mahsulotlar: \n")
for i in Recieve:
    if i not in E_Bozor.keys():
        print(i)
    
        
        