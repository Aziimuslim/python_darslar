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
