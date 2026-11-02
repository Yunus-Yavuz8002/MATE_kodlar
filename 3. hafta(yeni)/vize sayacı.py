from datetime import datetime
vize=input("Vize tarihi ve saati(Gün-Ay-Yıl Saat:Dakika):")
simdiki_zaman=datetime.now()
vize_zamanı=datetime.strptime(vize,"%d-%m-%Y %H:%M")
ne_kadar_kaldı=vize_zamanı-simdiki_zaman
gun = ne_kadar_kaldı.days
kalan_saniye = ne_kadar_kaldı.seconds
saat =kalan_saniye// 3600
dakika = (kalan_saniye% 3600) // 60
        
print(f"\nSınava Kalan Süre: {gun} gün, {saat} saat, {dakika} dakika.")
