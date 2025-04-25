  #Doiraning radiusini foydalanuvchidan sorang va uni radiusi diametri,
 #uzunligi va yuzini lugat qilib qaytaruvchi funcksiya yasang
 
def Aylana ():
    P=float(3.14)
    radius=float(input("Aylana radiusini kiriting: "))
    Diametri=float( 2*radius)
    Uzunligi= float(2*P*radius)
    Yuzi= float(P*(radius**2))
    Circle={"Aylana_radiusi":radius,
            "Aylana_diametri":Diametri,
            "Aylana_Uzunligi":Uzunligi,
            "Aylana_Yuzi":Yuzi
            }
    return Circle
print(Aylana())
