#Nesting
#26.10.2005
#Asqarov Azizbek

#Avtomabillar 
car0 ={
    'model':'lasetti',
    'rang':'oq',
    'yil':'2018',
    'narh':'13000',
    'km':'50000',
    'karobka':'avtomat'
}

car1 ={
    'model':'cobalt',
    'rang':'sariq',
    'yil':'2020',
    'narh':'15000',
    'km':'30000',
    'karobka':'avtomat'
}

car2 ={
    'model':'gentra',
    'rang':'qora',
    'yil':'2019',
    'narh':'16000',
    'km':'20000',
    'karobka':'mexanika'
}
'''
car = car0
print(f"{car['model'].title()},
    {car['rang']} rang,
    {car['yil']}-yil,{car['narh']}$")

car = car1
print(f"{car['model'].title()},
    {car['rang']} rang,
    {car['yil']}-yil,{car['narh']}$")

car = car2
print(f"{car['model'].title()},
    {car['rang']} rang,
    {car['yil']}-yil,{car['narh']}$")'''

#tsikli yordamida chiqarish
'''cars =[car0,car1,car2]
for car in cars:
    print(f"{car['model'].title()},"
        f"{car['rang']} rang",
        f"{car['yil']}-yil, {car['narh']}$")

print(cars[0]['model']) '''

'''
bmws=[]
for n in range(10):
    new_car = {
        'model':'bmw',
        'rang':None,
        'yil':'2026',
        'narh':None,
        'km':0,
        'korobka':'avto'
      }
    bmws.append(new_car)

for  bmw in bmws[:3]:
    bmw['rang']='qizil'

for bmw in bmws[3:6]:
    bmw['rang']='qora'
for bmw in bmws[6:]:
    bmw['korobka']='mexanik'

for bmw in bmws:
    if bmw['korobka']=='avto':
        bmw['narh']=40000
    else:
        bmw['narh']=35000

print(f"{bmws}")     '''

dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'sardor':['php','sql'],
    'aziz':['python','php'],
    'hasan':['c++','c#']
}

#har bir matindan keyin yangi qator tashlab yozadi.
'''for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())'''

#print()funktsiyasi har bir matn so'ng yangiqator tashlash oldini olish.
'''for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quiydagi dasturlash tillarini biladi: ", end='')
    for til in tillar:
        print(f'{til.upper()}', end='')'''

#LUG'AT ICHIDA LUG'AT
'''
hamkasblar ={
    'sardor':{
    'familiya':'qaxramonov',
    'tyil':2006,
    'malumot':'orta-mahsus',
    'tillar':['c++','python']
    },
    
    'kamoliddin':{
        'familiya':'rahimjanov',
        'tyil':2005,
        'malumot':'mahsus',
        'tillar':['python','nodejs','html']
    },

    'diyor':{
        'familiya':'salimov',
        'tyil':2006,
        'malumot':'orta',
        'tillar':['c++','html']
    }

}

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
        f"{info['tyil']}-yilda tug'olgan. "
        f"Ma`lumoti: {info['malumot']}. \n"
        "Quyidagi dasaturlash tillarini biladi:")
    
    for til in info['tillar']:
        print(til.upper())   '''

#Amaliyot






        