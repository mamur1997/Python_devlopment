

print('Chiptalar narxi: \n 0-7: 2000 so`m,\n 7-18 3000 so`m,\n'
      ' 18-65: 10000 so`m \n 65+ : Tekin'
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

