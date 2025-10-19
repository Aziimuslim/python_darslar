#if elif else
#15.10.2025
#Asqarov Azizbek
""" yosh = int (input("Yoshingiz nechida?: "))
if yosh<=4:
    print("Sizga[ kirish bepul")
elif yosh<=10:
    print("Sizga kirish 56000 so'm")
elif yosh<=18:
    print("Sizga kirish 100000 so'm")
else:
    print("Sizga kirish 150000 so'm") 

yosh = int (input("Yoshingiz nechida?: "))
if yosh<=4:
    narh=10000
elif yosh<=10:
   narh=20000
elif yosh<=18:
   narh=40000
else:
  narh=100000
print(f"Sizga kirish {narh} so'm") """
""" 
kun = input("Bugungi kun nima?:")
if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
    print("Bugun dam olish")
else:
    print("Bugun ish")    #or operatori yordamida ikki shattni tekshirish 
    harorat = float(input("Havo harorati qanday?:"))
if kun.lower() == 'yakshanba' and harorat > 35:
    print("Cho'milishga ketdik")
elif kun.lower() == 'yakshanba'  and harorat < 30:
    print("Uydan chiqmaymiz")
else:
 print("Bilmayman")    """  #and operatiri yordamida ikki shart tekshirishimiz mumkin    
# faqat ikki shart ham to'g'ri bo'lsa bajariladi
""" 
narh = 20000
choy = True
salat = False

if choy and salat:
    narh = narh + 10000
elif choy or salat:
    narh = narh +5000
print(f"Jami {narh} so'm")        
 """
""" choy = True
salat = False
non = True
kompot = 0
assorti = 1
narh = 0
if choy:
    print ("Mijoz choy oldi.")
    narh = narh +3000
if salat:
  print ("Mijoz salat oldi.")
  narh = narh + 5000
if non:
   print ("Mijoz non oldi.")
   narh = narh + 2000
if kompot:     
   print("Mijoz kompot oldi.")
   narh = narh + 1000
if assorti:
   print("Mijoz assorti oldi.")
   narh = narh + 15000
print (f"Jami {narh} so'm")
 """
""" 
menu = ['osh','qazonkabob','shashlik', 'norin', 'somsa']
#print('manti' in menu) # in orqali ichida bormi tekshiramiz
ovqat = input("Nima ovqat yeysiz?:")
if ovqat.lower() in menu: #in orqali ichida borligini tekshiramiz
    print("Buyurtma qabul qilindi.")
else:
    print("Afsuski bizda bunday ovqat yo'q.")
print("osh" not in menu)  #not in orqali ichida yo'qligini tekshiramiz
       """
""" 
menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else: # agar ro'yxat bo'sh bo'lsa
    print("Savatchangiz bo'sh!")  """      
# AMALIYOT
""" 
son = int(input("Juft son kiriting:"))
if son % 2 != 0:
    print("Bu son juft emas!")
else:
    print("Rahmat")
    
 yosh = int(input("Yoshingiz nechida:"))
if yosh < 4 or yosh > 60:
    narh = 0 
elif yosh < 18:
    narh =10000
else:
    narh = 20000
print(narh)    
"""
# Ikkita sonni solishtirish 
""" son1 = int(input("Son kiriting: "))
son2 = int(input("Son kiriting: "))
if son1 > son2:
       print(f"Javob: {son1} > {son2}")
else:
   print(f"Javob: {son1} < {son2}") """
# Maxsulotlar mavjudligini tekshirish
""" mahsulotlar = ['go`sht','un', 'yog', 'sovun', 'tuxum', 'piyoz', 'kartoshka', 'olma','non', 'guruch',] 
savat =[]
bor_mahsulotlar = [] 
mavjud_emas = []
for n in range(5):
    savat.append(input(f"Savatga {n+1} -maxsulotni qo`shing: "))
      
for mahsulot in savat:
   
   if mahsulot in mahsulotlar:
        print(f"{mahsulot} mahsulot do'konimizda bor ")
   else:
        print(f"{mahsulot} Uzur, bu mahsulot do`konimizda yo`q ")    

 """
#Maxsulotlarni bor va mavjud emasligini alohida ro'yxatga yozish
""" mahsulotlar = ['go`sht','un', 'yog', 'sovun', 'tuxum', 'piyoz', 'kartoshka', 'olma','non', 'guruch',] 
savat =[]
bor_mahsulotlar = [] 
mavjud_emas = []
for n in range(5):
    savat.append(input(f"Savatga {n+1} -maxsulotni qo`shing: "))
      
for mahsulot in savat:
   
   if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
   else:
        mavjud_emas.append(mahsulot) 
print(f"Do'konda bor mahsulotlar: {bor_mahsulotlar}")
print(f"Do'konda mavjud emas; {mavjud_emas}")         
 """

# Foydalanuvchidan login so'rash va tekshirish
""" foydalanuvchilar = [ 'asqarov','ali','admin','azizbek','lisa']
login = input("Foydalanuvchi login kiriting: ")
if login.lower() in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print("Xush kelibsiz!")     """\

# istalgan son so'rang va kiritgan son 2 dan 10 gacha bo'lgan istalgan songa qoldiqsiz bo'linsin
son = int(input("Istalgan son kiriting: "))
for n  in range(2,11):
    if son%n == 0:
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi.")
    
        
