# Listlar bilan ishalash 
""" 
mevalar = ['olma', 'anjir', 'shaftoli', 'o`rik']
narhlar = [ 10000, 20000, 15000, 18000 ]
sonlar = ['bir', 'ikki', 3, 4]
ismlar= [ ] #bo`sh ro`yxat """
# print(mevalar[0].upper())
#print(narhlar[0] + narhlar[2])
# mevalar.append('tarvuz') # royxatga element qo`shish oxiridanqo'ashdi
""" mevalar.insert(2,'banan') # istalgan joydan qo`shish`
print(mevalar) """
""" ismlar.append('sardor')
ismlar.append('Aziz')
ismlar.append('diyor')
ismlar.append('sardor')
#del ismlar[1]
ismlar.insert(0,'Kamollidin')
ismlar.remove('sardor')
##ismlar.remove('sardor')
print(ismlar) """
""" 
bozorlik = ["yog'", "un", "piyoz", "banan", "go'sht"]
#mahsulot = bozorlik.pop(3)
#print(bozorlik)
#print("Men " + mahsulot + " sotib oldim")
#print("Sotib olinmagan mahsulot: ", bozorlik)
mahsulot = bozorlik.pop()
print(mahsulot) """

""" ism = ['Zafar', 'Asat', 'Nurbek']
print(ism)
savol = ism.pop(0)
savol1 = ism.pop(1)
print("Salom " + savol +" bugun dars bormi?")
print(savol1 + ", chayxonaga boramizmi ?") """

sonlar = [ 1, 2, -10, 2.5, 100, -0.3, 8]
""" print(sonlar[0] + sonlar[3])
print(sonlar[3] - sonlar[6] * sonlar[4]) """
""" sonlar[0] = 12
sonlar[-4] = 17 """
""" sonlar.append(13)
sonlar.insert(0, '16') """
# print(sonlar)
""" t_shaxslar = ["Amir Temur", "Alisher Navoyi", "Abu Bakir"]
z_shaxslar = ["Abdukodir Husanov", "Cristiano Ranoldu"]

t_ism = t_shaxslar.pop(0)
z_ism = z_shaxslar.pop(1)
print("Men tarixiy shaxslardan "+t_ism + " bilan," +"zamonaviy shaxslardan esa " + z_ism + " bilan suhbat qilishni istar edim.")
 """
friends = [ ]
friends.append("Doniyor")
friends.append("Hakimjon")
friends.append("Shaxruh")
friends.append("Otabek")
friends.append("og'abek")
#friends.remove("Shaxruh")
#friends.append("Kamoliddin")
#friends.insert(2, "Diyor")
#friends.insert(0, "Sardor")
#print(friends)
#mehmonlar =[]
mehmonlar = friends.pop(1)
mehmonlar = friends.pop(0)
mehmonlar = friends.pop(2)
#ehmonlar = friends.pop(4)
print(mehmonlar)