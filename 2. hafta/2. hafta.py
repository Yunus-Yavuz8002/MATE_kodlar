# #1.görev
# ad = input("Adınızı girin: ")
# soyad = input("Soyadınızı girin: ")
# sehir = input("Yaşadığınız şehri girin: ")

# print(f"{ad} {soyad} isimli şahıs,{sehir} adlı şehirde çalışıyor")

# #2. görev
# def indirim_hesapla(tutar, indirim_yuzdesi):
#     son_fiyat = tutar*(100-indirim_yuzdesi)/100
#     return son_fiyat

# # Kullanım örneği
# print(indirim_hesapla(300,45))

# #3. görev
# dogum_yili = int(input("Doğum yılınızı girin: "))
# mevcut_yil = 2026
# yas = mevcut_yil - dogum_yili
# if yas >= 18:
#     print("Ehliyet alabilirsiniz.")
# else:
#     print(f"Ehliyet alamazsınız.")

# #4. görev
# def harf_notu_hesapla(vize, final):
#     ortalama = (vize * 0.40) + (final * 0.60)
    
#     if ortalama >= 90:
#         harf = "AA"
#     elif ortalama >= 85:
#         harf = "BA"
#     elif ortalama >= 80:
#         harf = "BB"
#     elif ortalama >= 75:
#         harf = "CB"
#     elif ortalama >= 70:
#         harf = "CC"
#     elif ortalama >= 65:
#         harf = "DC"
#     elif ortalama >= 60:
#         harf = "DD"
#     elif ortalama >= 50:
#         harf = "FD"
#     else:
#         harf = "FF"
        
#     return ortalama, harf

# # Kullanım örneği
# vize_notu = float(input("Vize notunuzu girin: "))
# final_notu = float(input("Final notunuzu girin: "))

# ort, harf = harf_notu_hesapla(vize_notu, final_notu)
# print(f"Ortalamanız: {ort}")
# print(f"Harf Notunuz: {harf}")