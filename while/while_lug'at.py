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

print("Do'stingiz yoshini saqlaymiz. ")
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

