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

'''
def yosh_hisobla(ism, tugilgan_yil):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{ism.title()} {2025-tugilgan_yil} yoshda")
#yosh_hisobla('sardor', 2005)    

#KALIT SO'Z BILAN UZATISH
yosh_hisobla(tugilgan_yil=2005, ism='sador') '''

#STANDART QIYMAT
'''
def yosh_hisobla(tugilgan_yil, joriy_yil=2025):
    """Foydalanuvchi tug'ilgan yilidanuning yoshini hisoblaydi."""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz.")

#yosh_hisobla(2000,2025)
yosh_hisobla(2000) # faqat bitta argument bilan chaqirish
'''
#AMALIYOT
#Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
'''
def ism_yosh(ism,yosh):
    """Tug'ilgan yilini hisoblash"""
    print(f"Siz {2025-yosh}-yilsiz.")

ism_yosh('aziz',20) '''

#Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
'''
def kub_kv(son):
    "Sonning kubi va kvadratini chiqarish"
    print(f"Soning kubi: {son**2} va kvadrati: {son**3}")

kub_kv(2)
kub_kv(4) '''

#Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
'''
def juft_toq(son):
    """Juft va Toqlika tekshirish."""
    print(f"Son juft {son%2==0}\n"
          f"Son toq {son%2!=0}")
    
juft_toq(2)    
juft_toq(5) '''

#Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
'''
def katta_sonni_top():
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting: "))
    
    if a > b:
        print(f"Katta son: {a}")
    elif b > a:
        print(f"Katta son: {b}")
    else:
        print("Sonlar teng")

# Funksiyani chaqirish
katta_sonni_top()
'''
#Foydalanuvchidan x va y sonlarini olib, xy ni konsolga chiqaruvchi funksiya yozing
'''
def x_y(x,y):
    """x ning y darajasini hisoblash."""
    print(f"x ning y darajasi {x**y}")

x_y(2,3)    
x_y(5,2)  '''
'''
#Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
def x_y(x,y=2):
    print(x**y)

x_y(4,2)
x_y(5)
x_y(6)  '''

def bolishni_tekshirish():
    son = int(input("Sonni kiriting: "))

    for i in range(2,11):
        if son % i == 0:
            print(f"{son} {i} ga qoldiqsiz bo'linadi.")
             
        else:
            print(f"{son} {i} ga qoldiqsiz bo'lnmaydi.")     


bolishni_tekshirish()