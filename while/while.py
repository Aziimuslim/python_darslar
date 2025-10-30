#while sikili
#30.10.2025
#Asqarov Azizbek

""" ism = input("Ismingiz nima?")
print(f'Salom, {ism.title()}')

ism = input("Ismingiz nima? ")
savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
yosh = input(savol) """

#Sonlar va input()

""" ism = input("ismingiz nima? ")
savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
yosh = input(savol)
yosh = int(yosh)
height = input("Bo'yingiz necha metr? ")
height = float(height) """

""" son = 1
while son<=5:
    print(son, end=' ')
    son = son + 1
     """

#while va input()
""" print("Kritilgan sonning kvadratini qaytaruvchi dastur. ")
savol = "Istalgan son kiriting "
savol +="(dasturni to'xtatish uchun 'exit' deb yozing): "
qiymat =''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat !='exit':
        print(float(qiymat)**2) """

#Ishora (flag)

""" print("Kritilgan sonning kvadratini qaytaruvchi dastur. ")
savol = "Istalgan son kiriting "
savol +="(dasturni to'xtatish uchun 'exit' deb yozing): "
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat =='exit':
        ishora =False

    else:
        print(float(qiymat)**2) """
        
#BREAK OPERATORI

""" print("Kritilgan sonning kvadratini qaytaruvchi dastur. ")
savol = "Istalgan son kiriting "
savol +="(dasturni to'xtatish uchun 'exit' deb yozing): "

#Break operatori yordamida ma'lum bir shartni tekshirish va while tsikli bajarilishini to'xtatib qo'yish mumkin. 
while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    else:
        print(float(qiymat)**2) """

#Break operatori for tsiklini to'xtatish uchun ham ishlatiladi.
""" sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:
        break
    print(f"{son} ning kvadrati {son**2} ga teng.") """
    
#CONTINUE OPERATORI

#Continue operatori esa aksincha, ma'lum bir shart bajarilganda qadam tashlab o'tish uchun mo'ljallangan.
""" sonlar = list(range(1,11))
for son in sonlar:
    if son ==5:
        continue
    print(f"{son}ning kvadrai {son**2} ga teng. ") """

""" son =0 
while son < 10:
    son +=1
    if son%2!=0:
        continue
    else:
        print(son) """

# infinite loop
""" son = 0
while son<10:
    if son%2!=0:
        continue
    else:
        print(son) """
""" son = 1
while son>0: 
    son += 1
    if son%2!=0:
        continue
    else:
        print(son) """

#Amaliyot 
""" savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng") """

""" savol = "Qaysi kitobni yaxshi korasiz: "
savol +="(Tugagan bolsa, 'stop' deb yozing):"

while True:
    n =input(savol)
    if n == 'stop':
      break
    else:
       print("Yana bormi: ") """

#Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).

while True:
    yosh = input("Yoshingizni kiriting (chiqish uchun 'exit' yoki 'quit' deb yozing): ")

    # chiqish sharti
    if yosh.lower() in ['exit', 'quit']:
        print("Dastur to‘xtatildi.")
        break

    # foydalanuvchi son kiritganini tekshiramiz
    try:
        yosh = int(yosh)
    except ValueError:
        print("Iltimos, butun son kiriting yoki 'exit'/'quit' deb yozing.")
        continue

    # chipta narxini aniqlash
    if yosh < 7:
        narx = 2000
    elif yosh < 18:
        narx = 3000
    elif yosh < 65:
        narx = 10000
    else:
        narx = 0

    # natijani chiqarish
    if narx == 0:
        print("Sizga kirish bepul!")
    else:
        print(f"Sizning chipta narxingiz: {narx} so'm.")

