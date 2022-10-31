import random

print("hoşeldin!")
oynamak_istiyor_musun=input("Oynamak ister misin")

while oynamak_istiyor_musun == "Evet":
    cevap = random.randint(1, 100)
    tahmin = int(input("1 ile 100 arasında bir sayı bul!"))

    while tahmin != cevap:
        if tahmin > cevap:
            print("Yanlış, bir dahakine daha küçük bir sayı tahmin et!")
        if tahmin < cevap:
            print("daha büyük bir sayı bul!")
        tahmin = int(input("1 ile 100 arasındaki sayıyı tahmin et!"))


    oynamak_istiyor_musun = input("Doğru!!!!   Evet yeni oyun? 'Evet', 'Hayır' \n")
