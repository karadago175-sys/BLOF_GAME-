import random


class OyunDurumu:
    def __init__(self):
        self.puan = 100
        self.can = 3
        self.tur = 1

    def durum_goster(self):
        print("\n--------------------")
        print("TUR:", self.tur)
        print("Puan:", self.puan)
        print("Can:", self.can)


oyun = OyunDurumu()

kart_turleri = ["As", "Papaz", "Kız", "Vale"]

print("=== BLOF OYUNU ===")
print("Baslangıç puan:", oyun.puan)
print("Can hakkı:", oyun.can)

while oyun.can > 0:

    oyun.durum_goster()

    # Her tur 4 kart dagitilir
    oyuncu_kartları = random.choices(kart_turleri, k=4)
    bilgisayar_kartları = random.choices(kart_turleri, k=4)

    hedef = random.choice(kart_turleri)

    print("\nElindeki kartlar:")
    for i in range(4):
        print(i + 1, "-", oyuncu_kartları[i])

    print("\nBu turun hedef kartı:", hedef)

    print("\n1 - Kart oyna")
    print("2 - Turu pas gec")
    print("3 - Oyundan cık")

    secim = input("Secimin: ")

    if secim == "1":

        try:
            adet = int(input("Kac kart oynayacaksın (1-4): "))
        except ValueError:
            adet = 0

        if adet >= 1 and adet <= 4:

            oynanan = []

            for i in range(adet):
                kart = oyuncu_kartları[i]
                oynanan.append(kart)

            print("\n", adet, "kart oynadın.")
            print("Bu kartların", hedef, "oldugunu soyledın.")

            blof = False

            for kart in oynanan:
                if kart != hedef:
                    blof = True

            bilgisayar_kararı = random.randint(1, 2)

            if bilgisayar_kararı == 1:
                print("Bilgisayar inandı!")
                oyun.puan += 10

            else:
                print("Bilgisayar BLOF dedi!")

                if blof == True:
                    print("BLOFUN YAKALANDI!")
                    oyun.can -= 1
                    oyun.puan -= 20

                else:
                    print("BLOF YAPMAMISTIN!")
                    print("Bilgisayar yanıldı.")
                    oyun.puan += 20

        else:
            print("1 ile 4 arasında kart secmelisin!")

    elif secim == "2":
        print("Turu pas gectin.")
        oyun.puan -= 5

    elif secim == "3":
        print("Oyundan ayrıldın.")
        break

    else:
        print("Gecersiz secim!")
        oyun.puan -= 10

    # Bilgisayarin sirasi
    if oyun.can > 0:

        print("\nBilgisayarın sırası!")

        bilgisayar_adet = random.randint(1, 4)

        oynanan_bilgisayar = bilgisayar_kartları[:bilgisayar_adet]

        print("Bilgisayar", bilgisayar_adet, "kart oynadı.")
        print("Kartlarin", hedef, "oldugunu iddia ediyor.")

        print("\n1 - Inan")
        print("2 - BLOF de")

        karar = input("Kararın: ")

        bilgisayar_blof = False

        for kart in oynanan_bilgisayar:
            if kart != hedef:
                bilgisayar_blof = True

        if karar == "1":

            if bilgisayar_blof == True:
                print("Bilgisayar yalan soyledı!")
                oyun.puan -= 10

            else:
                print("Bilgisayar dogru soyluyordu.")
                oyun.puan += 10

        elif karar == "2":

            print("Bilgisayarın kartları:", oynanan_bilgisayar)

            if bilgisayar_blof == True:
                print("TEBRIKLER! BLOFU YAKALADIN!")
                oyun.puan += 30

            else:
                print("YANILDIN! Bilgisayar dogru soyluyordu.")
                oyun.can -= 1
                oyun.puan -= 20

        else:
            print("Gecersiz karar!")
            oyun.puan -= 10

    # PUAN KISMI
    if oyun.puan >= 200:
        print("\n200 PUANA ULASTIN!")
        print("OYUNU KAZANDIN!")
        break

    elif oyun.puan <= 0:
        print("\nPuanın sıfırlandı!")
        print("OYUNU KAYBETTIN!")
        break

    elif oyun.can == 1:
        print("\nDIKKAT! TEK CANIN KALDI!")

    else:
        print("\nYeni tura geciliyor...")

    oyun.tur += 1

print("\n=== OYUN SONU ===")
print("Toplam puan:", oyun.puan)
print("Kalan can:", oyun.can)
print("Oynanan tur:", oyun.tur)

if oyun.can <= 0:
    print("Tum canlarını kaybettın!")

elif oyun.puan >= 200:
    print("YALANCI SENİ!")

elif oyun.puan >= 100:
    print("eh işte!")

else:
    print("Bir dahaki sefere dikkatli oyna!")