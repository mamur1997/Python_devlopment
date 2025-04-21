     #Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing.
 #For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.


Adabiyot={'ismi':'Alisher Navoiy',
          't-yil': 1441,
          't-shahri':'Xirot',
          'umri':60,
          'asar':['Hamsa','Lison ut-tayir','Mahbub ul-qulub','Xazoyin ul-ma`oniy']
          }
Ilm_fan={'ismi':'Al-Xorazmiy',
          't-yil': 783,
          't-shahri':'Xiva',
          'umri':67,
          'asar':['Algebra','Astramonica','Al-xitob','Zijji']
          }
Sanat={   'ismi':'Said-Ahmad',
          't-yil': 1920,
          't-shahri':'Toshkent',
          'umri':87,
          'asar':['Ufq','Jimjitlik','Kelinlar qozgoloni','Qoplon']
          }
Internet={'ismi':'Stive Jobs',
          't-yil':1955,
          't-shahri':'America',
          'umri':56,
          'asar':['Iphone1','Iphone2','Iphone3','Iphone4']
    }
Buyuklar=[Adabiyot, Ilm_fan, Sanat, Internet]
for nom in Buyuklar:
        ismlar=nom['ismi']
        asar=nom['asar']
        print(f"\n{ismlar} ning mashxur asarlari: ")
        for i in asar:
            print(f"{i}")


    
    

    
    
    
    
    
    
    
    
    
    
    
    