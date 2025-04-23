    #Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing.
 #Mahsulotlar nomini birma-bir qabul qilib, 
 #yangi ro'yxatga joylang.

print("Buyurtmalarni qabul qiluvchi dastur")
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
print("Sizning Mahsulotlaringiz: ")
for i in Recieve:
        print(i.title())