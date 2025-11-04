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

'''
def salom_ber(ism):
    """Fodyalanuvchi ismini qabul qilib, 
        unga salom beruvchi funksiya"""   #docstring  deyiladi. funksiyaga malumot yozish.
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")

salom_ber('aziz')

print(salom_ber.__doc__) #docstring konsilga chiqarish. 
'''

#ARGUMENT VA PARAMETER
'''Funksiya yaratishda, qavs ichida berilgan, funksiya to'g'ri ishlashi uchun uzatiladigan qiymat parameter deb ataladi. 
   Yuqoridagi misolda ism bu salom_ber funksiyasining parametri.'''
'''Foydalanuvchi funksiyaga murojat qilishda funksiyaga uzatgan qiymat esa argument deb ataladi.
    salom_ber('hasan') kodida 'hasan' bu argument.'''

#FUNKSIYAGA BIR NECHTA ARGUMENT UZATISH

#TO'G'RI TARTIBDA UZATISH
'''
def toliq_ism(ism,familiya):
    """Fodalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")

toliq_ism('sardor', 'aliyev') '''


def yosh_hisobla(ism, tugilgan_yil):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{ism.title()} {2025-tugilgan_yil} yoshda")
#yosh_hisobla('sardor', 2005)    

#KALIT SO'Z BILAN UZATISH
yosh_hisobla(tugilgan_yil=2005, ism='sador')
