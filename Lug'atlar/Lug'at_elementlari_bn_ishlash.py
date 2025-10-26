#Lug'at elementlari bilan ishlash
#22.10.2025
#Asqarov Azizbek

#.items() metodi
'''
talaba = {
    'ism':'azizbek',
    'familiya':'asqarov',
    'yosh':20,
    'universitet':'TUIT',
    'fakultet':'DIF',
    'kurs':3
}

#print(talaba.items()) #lug'at elementlarini juftlik ko'rinishida qaytaradi

#for tsikli ordamida tushunarli shakilda chiqarsak bo'ladi
for kalit, qiymat in talaba.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat}\n")'''
'''
telefonlar = {
    'ali':'iphone x',
    'diyor':'samsung s22',
    'sardor':'samsung a51',
    'kamoliddin':'redmi note 13 pro' } 

for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q.title()}")'''

#.keys() metodi 
'''
mahsulotlar = { #Do'kon mahsulotlari lug'ati
    'olma':10000,
    'anor':20000,
    'uzum':15000,
    'banan':18000, 
    'shaftoli':25000  }

#print(mahsulotlar.keys()) #Lug'at kalitlarini qaytaradi
#print("Do'konimizdagi mahsulotlar:")
#for mahsulot in mahsulotlar.keys():
#    print(mahsulot.title())

bozorlik = ['anor','uzum','non','olma']

for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

#Do'konda yo'q mahsulotlarni tekshirish
for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Kechirasiz, do'konimizda {buyum} yo`q")'''

#.values()metodi
""" telefonlar = { 'iphone':'iphone 13 pro', 'samsung' : 'samsung 22', 'mi' : 'redmi note 13 pro', 'vivo' : 'vivo s12'}
#print(telefonlar.values())

print('Foydalanuvchi quyidagi telefonlar ni ishlatadi: ') 
for tel in telefonlar.values():
    print(tel)
 """
""" telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }
#print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi: ")
#for tel in telefonlar.values():
#    print(tel)

#set() funksiyani orqali takrorlangan bir hil elementlar faqat bittasi olinadi
print("Foydalanuvchilar quyidagi telefoonlarni ishladadi: ")
for tel in set(telefonlar.values()):
    print(tel)
     """

#Amaliyot

""" py_lugat = {
    'Boolean':'Mantiqiy qiymat', 
    'Float':'o`nlik son',
    'For':'Biror amalni qayta-qayta bajarish tsikili',
    'If':'Shartlarni tekshirish operatiri',
    'Integer':'Butun son'
    }

for idx, q in enumerate(sorted(py_lugat.keys()), start=1):
    ta_rif = py_lugat[q]
    print(f'{idx}){q} - {ta_rif}') """
""" 
davlatlar = {
    'Davlatlar':'Poytaxtlar',
    'AQSH':'Washington',
    'Italiya':'Rim',
    'Rossiya':'Maskva',
    'Uzbakiston':'Toshkent'
}
print("Davlatlar: ")
for davlat in sorted(davlatlar.keys()):
    print(f"-{davlat}")

print("Poytaxtlar: ")
for poytaxt in sorted(davlatlar.values()):
    print(f"- {poytaxt}") """

""" 
davlatlar = {
    "O'zbekiston": "Toshkent",
    "AQSh": "Vashington",
    "Rossiya": "Moskva",
    "Yaponiya": "Tokio",
    "Germaniya": "Berlin",
    "Xitoy": "Pekin",
    "Fransiya": "Parij",
    "Hindiston": "Dehli",
    "Qozog'iston": "Astana",
    "Turkiya": "Anqara"
}
davlat =input("Qaysi davlat poytaxtini bilishni istaysiz: ")
if davlat in davlatlar:
    print(f"{davlat}ning poytaxti {davlatlar[davlat]}") 
else:
    print("Kechirasiz, bizda malumot yo'q.")   """   

menu = {
    "osh": 25000,
    "norin": 22000,
    "shashlik": 15000,
    "lavash": 20000,
    "somsa": 8000,
    "manti": 18000,
    "lag'mon": 21000,
    "choy": 5000,
    "kola": 10000,
    "hot-dog": 12000
}

buyurtmalar = []
print("3 ta taom buyirtma bering: ")

for i in range(3):
    taom = input(f"{i+1}-ta taom: ").lower()
    buyurtmalar.append(taom)

print("Buyurtma natijasi: ")

for taom in buyurtmalar:
    if taom in menu:
        print(f"{taom.title()} - {menu[taom]} so'm")
    else:
        print(f"Bizda biunday taom yo'q: {taom.title()}")    