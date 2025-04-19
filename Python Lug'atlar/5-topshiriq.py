        #Davlatlar va ularning poytaxtlari lug'atini tuzing.
 #Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida,
 #alifbo ketma-ketligida konsolga chiqaring

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
print("Dunyo davlatlari:")
for i in sorted(Davlatlar):
    print(i.upper())
print("\n Davlatlarning poytaxtlari")
for n in sorted(Davlatlar.values()):
    print(n.lower())
    