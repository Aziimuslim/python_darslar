#20 QIYMAT QAYTARUVCHI FUNKSIYA
#04.11.2025
#Asqarov Azizbek

#FUNKSIYADAN ODDIY QIYMAT QAYTARISH
def toliq_ism_yasa(ism, familiya):
    """Toliq isma qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism # qiymat qaytarish uchun return operatorini ishlatamiz

talaba1 = toliq_ism_yasa('olim','hakimov')
talaba2 = toliq_ism_yasa('hakim','olimov')

print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")