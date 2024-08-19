
import random

def tas_kagit_makas_ADINIZ_SOYADINIZ():
    print("Taş, Kağıt, Makas Oyununa Hoş Geldiniz!")
    print("Oyunun kuralları: Taş makası yener, makas kağıdı yener, kağıt taşı yener.")
    print("İlk iki turu kazanan oyunun galibi olacaktır.")
    print("Oyundan çıkmak için 'çıkış' yazabilirsiniz.")

    secenekler = ["taş", "kağıt", "makas"]
    
    while True:
        oyuncu_galibiyetleri = 0
        bilgisayar_galibiyetleri = 0
        tur_sayisi = 0

        while oyuncu_galibiyetleri < 2 and bilgisayar_galibiyetleri < 2:
            print(f"\nTur {tur_sayisi + 1}")
            oyuncu_secimi = input("Taş, kağıt veya makas seçin: ").lower()

            if oyuncu_secimi == "çıkış":
                print("Oyun bitti. Teşekkürler!")
                return

            if oyuncu_secimi not in secenekler:
                print("Geçersiz seçim! Lütfen taş, kağıt veya makas seçin.")
                continue

            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

            if oyuncu_secimi == bilgisayar_secimi:
                print("Berabere!")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                 (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                print("Bu turu kazandınız!")
                oyuncu_galibiyetleri += 1
            else:
                print("Bu turu bilgisayar kazandı!")
                bilgisayar_galibiyetleri += 1

            tur_sayisi += 1

        if oyuncu_galibiyetleri == 2:
            print("\nTebrikler, oyunu kazandınız!")
        else:
            print("\nMaalesef, oyunu bilgisayar kazandı.")

        tekrar_oyna = input("\nBaşka bir oyun oynamak ister misiniz? (Evet/Hayır): ").lower()
        if tekrar_oyna != "evet":
            print("Oyun bitti. Teşekkürler!")
            break

        bilgisayar_tekrar = random.choice(["evet", "hayır"])
        print(f"Bilgisayar {'oynamak istiyor.' if bilgisayar_tekrar == 'evet' else 'oynamak istemiyor.'}")
        if bilgisayar_tekrar != "evet":
            print("Bilgisayar oynamak istemediği için oyun bitti. Teşekkürler!")
            break

tas_kagit_makas_ADINIZ_SOYADINIZ()

