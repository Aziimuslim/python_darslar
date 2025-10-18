#FOR TAKRORLASH OPERATORI 
#06.10.2025  Asqarov Azizbek

""" mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim' ]
for mehmon in mehmonlar:
    print ("Salom", mehmon)
    print ("Hayr", mehmon) """
""" 
mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim' ]
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 Dwkabir kuni nahorga oshga taklif qilamiz")
    print("Hurmat bilan Asqarovlar oilasi ") """

""" sonlar = list(range(11))
for son in sonlar:
    print (f"{son} ning kvadrati {son**2} ga teng")
sonlar_kvadrati = []
for son in sonlar:
    sonlar_kvadrati.append(son**2)
print(sonlar)
print(sonlar_kvadrati) """

""" 
dostlar = [] #bosh ro'yxat
print("S ta eng yaqin do'stlar kim?")
for n in range(5):
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
print(dostlar)
 """

#Amaliy mashiq
# 1.Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
""" Ismlar = ['Asat', 'Ali', 'Vali', 'Bob', 'Aziz']
for i in Ismlar:
    print(i)
print('Kod 5 marta takrorlandi')     """

""" 
sonlar = list(range(11, 100, 2))
for kub in sonlar:
    print("kubi", {kub**3}) #soning kubi """
# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang,
# va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
""" 
kinolar =[]
print("Eng sevimli 5 ta kinongiz: ")
for t in range(5):
    kinolar.append(input(f"{t+1}-kino nomini kiriting: "))
print(kinolar) """

# Foydalanuvchidan bugun nechta odam bilan 
# uchrashganini (suhbatlashganini) so'rang, 
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
n_insonlar = int(input("Bugun nechta kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_insonlar):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)
