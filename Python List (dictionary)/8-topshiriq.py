 #Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur
 #shaxslar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. 
 #Lug'atlarni bitta ro'yxatga joylang, 
 #va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.

Adabiyot={'ismi':'Alisher Navoiy',
          't-yil': 1441,
          't-shahri':'Xirot',
          'umri':60
          }
Ilm_fan={'ismi':'Al-Xorazmiy',
          't-yil': 783,
          't-shahri':'Xiva',
          'umri':67
          }
Sanat={   'ismi':'Said-Ahmad',
          't-yil': 1920,
          't-shahri':'Toshkent',
          'umri':87
          }
Internet={'ismi':'Stive Jobs',
          't-yil':1955,
          't-shahri':'America',
          'umri':56
    }
Buyuklar=[Adabiyot, Ilm_fan, Sanat, Internet]
for nom in Buyuklar:
    print(f"{nom['ismi']} {nom['t-yil']}-yilda {nom['t-shahri']}"
          f"da tavallud topgan. {nom['umri']}-yil umr korgan"
          ) 
    