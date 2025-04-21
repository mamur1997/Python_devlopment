
    #Foydalanuvchidan istalgan davlatni kiritishni so'rang
 #va shu davlatning poytaxtini konsolga chiqaring.
 #Agar foydalanuvchi lug'atda yo'q davlatni kiritsa,
 #"Bizda bunday ma'lumot yo'q" degan xabarni chiqaring

Davlatlar={'Uzbekiston':'Tashkent',
          'Angliya':'London',
          'Fransiya':'Parij',
          'Germaniya':'Berlin',
          'Canada':'Ottava',
          'Rossiya':'Moskva',
          'Qatar':'Doha',
          'Sauida':'Al-riyadh',
          'Ispaniya':'Madrid'
          }
NewInput=input("Qaysi davlatni poytaxtini bilishni istaysiz: ")
nomlash=Davlatlar.get(NewInput.capitalize())
if nomlash==None:
   print(f"{NewInput.capitalize()} davlatining poytaxti mavjud emas") 
else:print(f"{NewInput.capitalize()} ning poytaxti: {nomlash.capitalize()} shahri")

