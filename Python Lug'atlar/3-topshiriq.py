    #Python dasturlash tilida ozingiz bilgan 8 ta atama yarating
#(Lug`at tipida) va Ularni manosini kiriting masalan:('for':'Sikl opereatori')
#foydalanuvchidan Kalit soz kiritishni sorang? va uni lugatdan tekshiring
#Agar foydalanuvchi kiritgan soz lug`atda mavjud bolsa Lug`atdan topib
#console ga chiqaring aks holda Mavjud emas deb chiqaring


Atamalar={'string':'Matn',
          'integer':'Butun son',
          'float':'Bolak son',
          'list':'Royhat',
          'massive':'Toplam',
          'if':'Shart operator',
          'for':'Sikl operator',
          'range':'listga royhat qoshish'
          }
Kalit=input('Kalit sozni kiriting: ')
print(Atamalar.get(Kalit,"Mavjud emas"))

