#Lug'atlar bilan tanishuv
#21.10.2025
#Asqarov Azizbek

#Car haqida ma'lumot
'''
car = {'model':'bmw', 'rang':'qora'}
print(car['model'])
print(car['rang'])
'''
#Talaba haqida ma'lumot
'''
talaba = {'ism':'aziz','familiya':'asqarov','yosh':'20','yil':2005}
talaba['kurs'] = 3
talaba['fakultet'] = 'DIF'
print(f"{talaba['ism'].title()},\
 {talaba['familiya'].title()},\
 {talaba['yosh']} yoshda,\
 {talaba['yil']} -yilda tug'ilgan" )
print(talaba)'''

#Bo'shlug'at yaratish
'''
talaba_1 = {}
talaba_1['ism'] = 'kamoliddin'
talaba_1['kursi'] = 3
talaba_1['yoshi'] = 19
print(talaba_1)
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kursi']} -kurs")

#Qiymatni o'zgartirish
talaba_1['kursi'] = 4
print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kursi']} -kurs, yoshi {talaba_1['yoshi']} da ")

#Kalit so'z-qiymat juftligini o'chirish
del talaba_1['yoshi']
print(talaba_1)
'''

#Lug'atni qatorlarga bo'lish
'''
telefonlar = {
    'ali':'iphone x',
    'diyor':'samsung s22',
    'sardor':'samsung a51',
    'kamoliddin':'redmi note 13 pro' 
    }  
print(telefonlar)

#get() metodi

phone = telefonlar['ali']
print(f"Alining teleoni {phone}")

#phone = telefonlar.get('hasan','Bunday ism mavjud emas')
phone = telefonlar.get('hasan') #get() metodida 2 chi argumentni taslab ketsak None qaytaradi
print(phone)
'''
#Amaliyot \
#oila a'zolari haqida lug'at yaratish

dadam = {'ism':'jumaboy', 'yili':1957, 'tug`ilgan_joyi':'qaraqalpog`iston'}
print(f"Dadamning ismi {dadam['ism'].title()},\
 {dadam['yili']}-yilda,\
 {dadam['tug`ilgan_joyi'].title()}da tug`ilgan")

#oila a'zolari Yoqtirgan taomlari haqida lug'at yaratish

toamlar = {
    'dadam':'osh', 
    'onam':'beshbarmoq',
    'akam':'tuxum barak',
    'oyapam':'manti',
    'men':'gumma' }
print(f"Akamning sevimli taomi {toamlar['akam'].title()}")
print(f"Onamning sevimli taomi {toamlar['onam'].title()}")
print(f"Dadamning sevimli taomi {toamlar['dadam'].title()}") 

