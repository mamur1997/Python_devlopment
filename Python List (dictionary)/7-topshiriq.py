    #Restoran menusi lug'atini tuzing (kamida 7 ta taom-narh juftligini kiriting).
 #Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang.
 #Foydalanuvchi kiritgan taomlarni menu bilan solishtiring,
 #agar taom menuda bo'lsa narhini ko'rsating,
 #aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
    
Taomlar={'Osh': 25000,
         'Mastava':30000,
         'Chuchvara':28000,
         'Manti':5000,
         'Lagmon':32000,
         'Norin':40000,
         'Makaron':18000
         }
print('3 ta taom buyurtma qiling:')
buyurtma=[]
for n in range(3):
    buyurtma.append(input(f"{n+1}- taom: "))
for i in buyurtma:
    if i in Taomlar:
        print(f"{i.capitalize()} {Taomlar[i]}- so`m ")
    else:print(f"Kechirasiz bizda {i} mavjud emas")
    