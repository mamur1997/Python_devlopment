  #Shunday funksiya yasangki unga 2 ta oraliq qiymat bering
 #funksiya oraliqdagi tub sonlarni qaytarsin 

def tubsonlar (min,max):
    tubson=[]
    for i in range(min,max+1):
        tub=True
        if i == 1:
            tub=False
        elif i == 2:
            tub=True
        else:
            for n in range(2,int(i**0.5)+1):
                if i % n == 0:
                    tub=False
                    break
        if tub:
            tubson.append(i)
    return tubson
print(tubsonlar(5, 100))