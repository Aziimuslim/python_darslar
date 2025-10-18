# ro'yxat bilan ishlash

#RO'YXATNI TARTIBLASH
#cars = ["bmw", "mercedes banz", "volvo", "tesla", "audi", "kia"]
#cars.sort() # .sort() metodi ro'yxat ichidagi elemrntlarni alifbo tartibida tartiblash uchun ishlatadi
#print(cars) 
""" 
cars = ["bmw", "mercedes banz", "Volvo", "tesla", "audi", "kia"]
cars.sort(reverse=True) # ro`yxat elementlarini birxil ko`rinishga keltiradi yani orasida katta harfbilan yozilgan bo'la teskari tartibla saqlaydi
print(cars)
 """
# .sort() metodi ro'yxatni tartiblaydi. Ba'zida asl ro'yxat ichidagi elementlarning ketma-ketligini buzmagan holda ro'yxatni tartiblash talab qilinishi mumkin. Buning uchun sorted() funktsiyasidan foydalanamiz:
""" mehmonlar =["Odil", "Hamid", "Temur", "Avazbek", "Farruh", "Sahmsiddin"]
print("sorted() qaytaragan ro'yxat: ", sorted(mehmonlar))
print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)
 """
""" ages = [12, 98, 34, 65, 34, 76, 11]
ages.sort() # tartiblash 
print(ages) 
print(sorted(ages, reverse=True)) # reverse = True teskari trtibda tartibda tartiblash
 """
#RO'YXATNI AYLANTIRISH
#Ba'zida ro'yxatni aylantirish (boshini oxiriga, oxirini boshiga) talab qilinishi mumkin. Buning uchun .reverse() metodidan foydalanamiz.
""" fruits = ['pear', 'banan', 'apple', 'watermelon', 'lemon']
fruits.reverse() # boshini oxiriga oxirini boshiga almashtirish 
print(fruits) """

#RO'YXATNING UZUNLIGINI BILISH
""" fruits = ['pear', 'banan', 'apple', 'watermelon', 'lemon']
print("Elementlar soni:", len(fruits)) # len() ro'yxat uzuligini qaytaradi 

 """
# range() funksiyasi
""" sonlar = list(range(0,20))
print(sonlar) """

#range() yordamida qadamini ham berish mumkin
""" juft_sonlar = list(range(0,20,2)) #0 dan 20 gacha 2 qadam bilan
toq_sonlar = list(range(1,20,2)) # 1 dan 20 gacha 2 qadam bilan
print("Juft sonlar:", juft_sonlar)
print("Toq sonlar: ", toq_sonlar) """

#SONLI RO'YXAT USTIDA SODDA AMALLAR
""" narhlar = [12000, 22500, 12324, 9800, 5600, 17000, 5000]
arzon = min(narhlar) # eng kichigi 
qimmat = max(narhlar) #eng kattasi
jami = sum(narhlar) #yig'indi hisoblash
print ( " Eng arzon narh ", arzon, ". Eng qimmat narh ", qimmat, ". Jami: ", jami)
 """
#RO"YXATNI KESISH
#Ba'zida ro'yxatning ma'lum bir bo'lagini ajratib olish talab qilinishi mumkin, deylik biz quyidagi cars degan ro'yxatdan birinchi 3 ta elementni ajratib olmoqchimiz, buning uchun biz boshlang'ich va oxirgi indekslarni beramiz:
""" 
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
my_cars =cars[0:3]
print(my_cars)
print(cars[:4])
print(cars[2:]) """

#RO'YXATDAN NUSXA OLISH
""" sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
#sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
sonlar2 = sonlar[:] # [:] ro'yxatni to'liq ko'chirib oladi
sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
print("Bu sonlar ro'yxati:", sonlar)
print("Bu sonlar2 ro'yxati:", sonlar2) """

#TUPLES - O'ZGARMAS RO'YXAT
""" tomonlar = (20, 30, 55.2) #tuples da [] lar orniga () lar ishlatiladi.
print(tomonlar)
#qolgan amallar bir hil
toys = ('bus','car','bear','dino','snake','lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5]) """
""" 
toys = ('bus','car','bear','dino','snake','lizard')
toys[3] = 'dragon' #ERROR  beradi
#Demak yuqorida ko'rib turganingiz kabi, bu operatsiya xatolikka olib keldi. Shu kabi ro'yxatdan biror elementni o'chirish yoki yangi element qo'shish ham mumkin emas.
 """
""" toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard') #o'zgarmas ro'yxat
toys = list(toys) #o'zgarmsa ro'yxat oddiy ro'yxatga aylantiramiz
#Ro'yxatga o'zgarishlar kiritamiz
toys.append('dragon')
toys.remove('bus')
toys[1] ='mcqueen'
toys = tuple(toys) # Ro'yxatni qaytatdan o'zgarmas ro'yxatga aylantiramiz
print(toys) """

#Amaliyot
#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring

#davlatlar = ['Fransiya', 'Ispaniya', 'Braziliya', 'Janubiy Karea', 'AQSH', 'Ozbekiston']
#print(davlatlar)
#print(len(davlatlar)) #Ro'yxat uzunlihini toping
#print(sorted(davlatlar)) # sorted() funksiyasi yordamida ro'yxatni tartiblab konsilaga chiqarish 
#print(sorted(davlatlar, reverse=True)) #Teskari tartibda tartiblash 
#print(davlatlar) #Asl ro'yxat
#davlatlar.reverse() # reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
#print(davlatlar)
#davlatlar.sort() #Alifbo tartibda tartiblash
#print(davlatlar)
#print(sorted(davlatlar, reverse=True )) # Alifbo tartibida teskari tartiblash
#sonlar = list(range(120, 1200))
#print(sum(sonlar)) # yig'indisi
#print(max(sonlar) - min(sonlar)) # max va min ayirmasi
#print(len(sonlar)) # elementlar soni
#print(sonlar[:20]) #boshidagi 20 ta son
#print(sonlar[-20:]) #oxiridagi 20 ta son
#print(sonlar[530:550]) #ortasidagi 20 ta
# taomlar = ['osh', "manti", "mastava", "somsa", "tuxum borak"]
#nonushta = taomlar[:]
""" nonushta.append("pitsa")
nonushta.append("tuxum")
nonushta.append("shorva")
print(taomlar)
print(nonushta) """
#nonushta = tuple(nonushta)
#nonushta[0] = "qaymoq av non" #ERROR
