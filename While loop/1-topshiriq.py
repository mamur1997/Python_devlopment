          #Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq:
    #7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm,
    #18-65 gacha 10000 so'm, 65 dan kattalarga bepul.
    #Shunday while tsikl yozingki, dastur foydalanuvchi yoshini
    #so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki
    #quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).

print('Chiptalar narxi: \n 0-7: 10000 so`m,\n 7-18 20000 so`m,\n'
      ' 18-65: 300000 so`m \n 65+ : Tekin'
      )
savol= "Yoshingizni kiriting: "
qiymat=True
while qiymat:
    qiymat=input(savol)
    if qiymat =='exit' or qiymat== 'quit':
        qiymat=False
    natija=int(qiymat)
    if natija <= 7:
        print("Sizga bilet narxi- 10000 so`m")
        print("Dasturni to`xtatish uchun exit ni kiriting\n")
    elif natija <=18:
        print("Sizga bilet narxi- 20000 so`m")
        print("Dasturni to`xtatish uchun exit ni kiriting\n")
    elif natija <=65:
        print("Sizga bilet narxi- 30000 so`m")
        print("Dasturni to`xtatish uchun exit ni kiriting\n")
    elif natija >65:
        print("Sizga tekin")
        print("Dasturni to`xtatish uchun exit ni kiriting\n")

