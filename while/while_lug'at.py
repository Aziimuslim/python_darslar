#18 WHILE, RO'YXATLAR VA LUG'ATLAR
#03.11.2025
#Asqarov Azizbek

#While yordamida  ro'yxatni to'dirish

#Yaqin do'stlaringiz ro'yxatini tuzamiz

'''ismlar =[]

print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
n=1
while True:
    savol =f"{n}-do'stingiz ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana ism qo'shasizmi? (ha/yo'q) ")
    if javob == 'ha':
        n+=1
        continue
    else:
        break

print("Do'stlaringiz ro'yxati: ")
for ism in ismlar:
    print(ism.title()) 
'''
#WHILE YORDAMIDA LUG'ATNI TO'LDIRISH

''''print("Do'stingiz yoshini saqlaymiz. ")
dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stingiz ismini kiriting: ")
    yosh = input(f"{ism.title()}ning yoshinin kiriting: ")
    dostlar[ism] = int(yosh)

    javob = input("Yana ma'lumot kiritasizmi: (ha/yo'q)")
    if javob == "yo'q":
        ishora = False

for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")
'''

#RO'YXAT ELEMENTLARINI O'CHIRISH

'''cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'audi', 'malibu', 'nexia']
while 'nexia' in cars:
    cars.remove('nexia')
print(cars) '''

#RO'YXATDAN RO'YXATGA ELEMENT KO'CHIRISH
'''talabalar = ['hasan','husan', 'olim', 'botir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho =input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi.")
    baholangan_talabalar[talaba] = baho
'''

#Amaliyot
#Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
'''
mahsulotar =[]
print("Mahsulot sotib olish: ")
n = 1
while True:
    savol =f"{n}-sotib oladigan mahsulot nomini kiriting: "
    mahsulot = input(savol)
    mahsulotar.append(mahsulot)
    javob =  input("Yana mahsulot qo'shasizmi? (ha/yoq)")
    if javob =='ha':
        n+=1
        continue
    else:
        break

print("Mahsulotlar ro'yxati: ")
for mahsulot in mahsulotar:
    print(mahsulot.title())    '''
'''
print("e-bozor uchun mahsulotlar narxhini saqlaymiz: ")
mahsulotar ={}
ishora =True
while ishora:
    mahsulot = input("Mahsulot nomini kiriting: ")
    narx = input(f"{mahsulot.title()}ning narxini kiriting: ")
    mahsulotar[mahsulot]= int(narx)

    javob = input("Yana mahsulot qo'shasizmi? (ha/yoq) ")
    if javob == "yoq":
        ishora = False

for mahsulot, narx in mahsulotar.items():
    print(f"{mahsulot.title()} {narx} yoshda")
'''

#Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.

# E-bozor mahsulotlari (tayyor ro‘yxat)
bozor = {
    'olma': 12000,
    'banan': 18000,
    'apelsin': 15000,
    'non': 4000,
    'sut': 9000,
    'tuxum': 1500
}

# Foydalanuvchi buyurtmasi
buyurtma = ['olma', 'tuxum', 'kofe', 'non']

# Har bir mahsulotni tekshirish
for mahsulot in buyurtma:
    if mahsulot in bozor:
        print(f"{mahsulot.capitalize()} narxi: {bozor[mahsulot]} so'm")
    else:
        print(f"Bizda {mahsulot} yo'q.")

