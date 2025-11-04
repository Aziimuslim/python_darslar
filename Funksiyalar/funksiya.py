#19 FUNKSIYA
#03.11.2025
#Asqarov Azizbek

#FUNKSIYA YARATAMIZ
#salom ber degan funksiya yaratamiz
'''def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu alekum")

salom_ber() #Funksiyani chaqirish'''

#FUNKSIYAGA QIYMAT UZATISH
'''
def salom_ber(ism):
     """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")

salom_ber('aziz')   '''

def salom_ber(ism):
    """Fodyalanuvchi ismini qabul qilib, 
        unga salom beruvchi funksiya"""   #docstring  deyiladi. funksiyaga malumot yozish.
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")

salom_ber('aziz')

print(salom_ber.__doc__) #docstring konsilga chiqarish. 
