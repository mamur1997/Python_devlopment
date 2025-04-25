    #Funksiya yarating uni ichida malumotlar kiritish degan obyekt yarating
 # malumotlarni kiriting va ushbu funksiyani while sikli bilan ham 
 #qoshimcha malumotlar kiritishni hosil qiling
 
def getname (ismi, familiyasi, tugulgan_yili, tugulgan_joyi, email, telefon):
    Obyekt={'Ismi':ismi,
           'Familiyasi':familiyasi,
           'TugulganYili':tugulgan_yili,
           'TugulganJoyi':tugulgan_joyi,
           'Emaili':email,
           'Telefoni':telefon
           }
    return Obyekt
newget=[]
while True:
    print('Quyidagi malumotlarni kirgazing!!!')
    ismi=input("Ismingiz: ")
    familiyasi=input('Familiyangiz: ')
    tugulgan_yili=input('Tugulgan yilingiz: ')
    tugulgan_joyi=input('Tugulgan joyingiz: ')
    email=input('Emailingiz: ')
    telefon=input('Telefoningiz: ')
    newget.append(getname(ismi, familiyasi, tugulgan_yili, tugulgan_joyi, email, telefon))
    asking=input('Yana malumot kiritasizmi? yes/no:  ')
    if asking == 'no':
        break
print(newget)
    