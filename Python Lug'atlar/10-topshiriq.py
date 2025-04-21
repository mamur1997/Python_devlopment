        #foydalanuvchi so'ragan davlat haqida ma'lumot bering.
     #Agar davlat sizning lug'atingizda mavjud bo'lmasa, 
    #"Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.

Davlatlar={'Uzbekiston':{'Poytaxti':'Tashkent',
                         'Hududi':448978,
                         'Aholisi':'37 mln',
                         'Pul birligi':'sum'},
           'Rossiya':{'Poytaxti':'Moskva',
                      'Hududi':17892334,
                      'Aholisi':'144 mln',
                      'Pul birligi':'Rubl'},
           'America' :{'Poytaxti':'Vashington',
                    'Hududi':9823534,
                    'Aholisi':15030539,
                    'Pul birligi':'Dollor $$$'},
           'Malayziya':{'Poytaxti':'Kuala-Lumpur',
                        'Hududi':3431535,
                        'Aholisi':2345514,
                        'Pul birligi':'rinngit'}
           }
kirit=input("Davlat nomini kiriting: ").capitalize()  
if kirit in Davlatlar:
    info=Davlatlar[kirit]
    print(f"{kirit} ning poytaxti: {info['Poytaxti']} ")
    print(f"Hududi: {info['Hududi']}"
          f"\nAholisi: {info['Aholisi']}"
          f"\nPul birligi: {info['Pul birligi']}")
else:print(f"Bizda {kirit} davlati mavju emas")       



        