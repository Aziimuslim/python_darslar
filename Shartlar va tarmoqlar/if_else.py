#09.10.2025
#Asqarov  Azizbek
""" avtolar =['audi', 'bmw', 'volvo', 'kia', 'merc']

for avto in avtolar:
    if avto == 'bmw':
        print(avto.upper())
    else:
        print(avto.title())
          """
""" ism = input("Ismingiz nima?\n>>>")
if ism.lower() != 'ali':
    print(f"uzur,{ism.title()} biz Alini kutyabmiz")
else:
    print("Salom,Ali")     """
""" javob = float(input("12x6 nechiga teng?>>>"))
if javob !=72:
    print("Javob xato") """
""" 
yosh = int(input("Yoshingiz nechada?>>>"))
if yosh >=18:
    print("Xush kelibsiz")
else:
    print("Kirish mumkin emas!")     """
""" yil = int(input("Tug'ilgan yilingizni kiriting:"))
if 2020-yil<18: # foydalanuvchining yoshini hisoblaymiz
    print(f"Yoshingiz {2020-yil}da ekan.")
    print("Kirish mumkin emas!")
else:
    print("Xush kelibsiz!") """
#Amaliy qism

""" cars = ['li', 'mazda','kia','gm','merc']
for car in cars:
    if car =='gm':
     print(car.upper())
    else:
       print(car.title()) """
""" 
ismlar =['aziz', 'ali', 'temur', 'zakir']
for ism in ismlar:
    if ism == 'ali':
        print(ism.upper())
    else:
       print(ism.title())     """
""" 
davlatlar = ['uzbekiston','aqsh','canada','ispaniya']
for davlat in davlatlar:
    if davlat != 'aqsh':
        print(davlat.title())
    else:
        print(davlat.upper())     """
""" 
login = input("Ismimgiz?:>>>")  
if login == 'admin':
  print("Xush kelibsiz, Admin. Foydalanuvchi ro'yxatini ko'ramizmi?")
else: 
  print("Xush kelibsiz,",login.title())
 """
""" 
son1 = int(input("1-soni kiriting?: "))
son2 =int(input("2-soni kiriting: "))
if son1 == son2 :
    print("Sonlar teng")
else:
    print("Sonlar teng emas")     """
""" 
son = int(input("Istalgan soni kiriting?:"))
if son < 0 :
    print("Manfiy son")
else:
    print("Musbat son")
 """

son =int(input("Son kiriting: "))
if son > 0:
    print(son**(1/2))  
else:
    print("Musbat son kiriting!")
