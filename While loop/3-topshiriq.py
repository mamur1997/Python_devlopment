    #E-bozor uchun mahsulotlar va ularning narhlari lug'atini
  #shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga bir nechta
  #elementlar (mahsulot va uning narhi) kiritishni so'rang.
  
print("Bozor uchun dastur")
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
print("E_Bozor uchun royhatlar: ")
print(E_Bozor)    