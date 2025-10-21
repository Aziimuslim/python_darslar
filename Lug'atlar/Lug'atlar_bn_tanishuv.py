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
