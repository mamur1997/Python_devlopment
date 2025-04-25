   #3 ta sonni kirtuvchi funksiya yozing qachonki kiritgan sonlaringiz
#dan eng kattasini qaytarsin masalan (51 55 89) Katta son: 89    

def getnumber ():
    num1=int(input('1-sonni kiriting: '))
    num2=int(input('2-sonni kiriting: '))
    num3=int(input('3-sonni kiriting: '))
    
    if num1>=num2 and num1>=num3:
        katta=num1
    elif num2>=num1 and num2>=num3:
        katta=num2
    else:
        katta=num3
    print(f"Katta son: {katta}")
    return num1,num2,num3
kirit1=getnumber()
print(kirit1)