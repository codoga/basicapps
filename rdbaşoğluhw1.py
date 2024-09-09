# -*- coding: utf-8 -*-
"""RDBaşoğluHW1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J0SJUB4EPnfjHt9J3nkQnD2KoI11IiIU

Task-1
Dörtgen, üçgen veya  dairenin  Alan hesabı. Kullanıcıdan en boy değerleri alınacak ve alan hesaplanacak.
"""

soru= input("Neyin alanını ölçmek istiyorsunuz?(Dörtgen=1,Üçgen=2,Daire=3) ")
if soru == "1":
  taban = float(input("Dörtgen taban uzunluğu kaç cm? "))
  yükseklik = float(input("Dörtgen yüksekliği kaç cm? "))
  alandörtgen= taban*yükseklik
  print("Dörtgenin alanı " + str(alandörtgen) + "cm\u00B2 ölçülmüştür."  )
if soru == "2":
  taban = float(input("Üçgen taban uzunluğu kaç cm? "))
  yükseklik = float(input("Üçgen yüksekliği kaç cm? "))
  alanüçgen= taban*yükseklik/2
  print("Üçgenin alanı " + str(alanüçgen) + "cm\u00B2 ölçülmüştür."  )
if soru == "3":
  yarıçap = float(input("Dairenin yarıçapı kaç cm? " ))
  alandaire= (yarıçap**2)*3.14
  print("Dairenin alanı " + str(alandaire) + "cm\u00B2 ölçülmüştür."  )
#cm\u00B2 ifadesiyle santimetrekare çıktısı alınabiliyor olmasını araştırdım.

"""Task-2 Girilen "gün", "saat", "dakika" ve "saniye" değerine göre, toplam saniyeyi hesaplayan bir uygulama yapınız."""

gün= int(input("Hesaplamak istediğiniz sürenin gün sayısını yazın: "))
saat= int(input("Hesaplamak istediğiniz sürenin saat sayısını yazın: "))
dakika= int(input("Hesaplamak istediğiniz sürenin dakika sayısını yazın: "))
saniye= int(input("Hesaplamak istediğiniz sürenin saniye sayısını yazın: "))
print("Toplam süre= " + str( int(gün*86400) + int(saat*3600) + int(dakika*60) + int(saniye)) + " saniye.")

"""Task-3 Vücut Kitle Endeksini hesaplayan uygulamayı yapın (ağırlığın(kg) boyun karesine (m)bölümü)"""

ağırlık = float(input("Lütfen kilonuzu kg cinsinden giriniz: "))
boy = float(input("Lütfen boyunuzu metre cinsinen giriniz: "))
vke = ağırlık / (boy ** 2)
print("Vücut Kitle Endeksiniz= " + str(vke))
if vke < 18.5:
    print("Zayıfsınız")
elif 18.5 <= vke < 24.9:
    print("Normal kilolusunuz")
elif 25 <= vke < 29.9:
    print("Fazla kilolusunuz")
else:
    print("Obezsiniz")

"""Task-4 Restoran. Kullanıcı "pizza", "burger" veya "salata" seçeneklerinden birini seçecek. seçtiği menünün fiyatını bir değişkene atayacak.
Bu fiyata %15 vergi oranı uygulayacak, %10 bahşiş ekleyecek ve toplam fiyat yazdırılacak.
"""

pizza,burger,salata = 100,120,60
seçim = input("Lütfen bir menü seçin: pizza, burger veya salata: ")
if seçim == "pizza":
  print("Toplam Fiyat= " + str(pizza*1.15*1.1) + " TL")
elif seçim == "burger":
  print("Toplam Fiyat= " + str(burger*1.15*1.1) + " TL")
elif seçim == "salata":
  print("Toplam Fiyat= " + str(salata*1.15*1.1) + " TL")
else:
  print("Yanlış seçim yaptınız.")

"""Task-5 feet'i inch, yard, mil e çevirin."""

feet = float(input("Lütfen feet değerini girin: "))
inch = feet * 12
yard = feet * 0.3
mil = feet * 0.0002
print(str(feet) + "feet " + str(inch) + ("inch,"),str(yard) + ("yard, "),str(mil) + ("mil") + "'e eşittir.,")

"""Task-6 Kullanıcı bir kelime girecek, bu kelime "tr" ifadesi içeriyorsa "kelime tr ifadesi içeriyor" mesajı, içermiyorsa "tr ifadesi içermiyor" mesajı versin.

"""

kelime = input("Kelimeyi girin: ")
if "tr" in kelime:
  print("Kelime tr ifadesi içeriyor.")
else:
  print("Kelime tr ifadesi içermiyor.")

"""Task-7 Kullanıcıdan iki kelime girdisi isteyeceksiniz. ikisinin aynı kelime olup olmadığını kıyaslayacaksınız.
(kullanıcı ister büyük harfle girsin ister küçük. -lower)
"""

kelime1 = input("Birinci kelimeyi girin: ")
kelime2 = input("İkinci kelimeyi girin: ")
if kelime1.lower() == kelime2.lower():
  print("Kelimeler aynıdır.")
else:
  print("Kelimeler farklıdır.")

"""Task-8 Herhangi  bir sayı girsin. Girdiği sayının 100 den büyük, küçük veya eşit olduğu mesajı verilsin. (tiplere dikkat)

"""

sayı = int(input("Bir sayı girin: "))
if sayı > 100:
  print("Girdiğiniz sayı 100'den büyüktür.")
elif sayı < 100:
  print("Girdiğiniz sayı 100'den küçüktür.")
else:
  print("Girdiğiniz sayı 100'e eşittir.")

"""Task-9 Kullanıcı yaşını girecek, 12 yaşa kadar- Çocuk, 13-19 yaş - Ergen, 20-30 yaş Genç yetişkin, 30-64 yaş Yetişkin, 64 yaş üzeri olgun."""

yaş = int(input("Yaşınızı girin: "))
if yaş <= 12:
  print("Çocuk")
elif 13 <= yaş <= 19:
  print("Ergen")
elif 20 <= yaş <= 30:
  print("Genç yetişkin")
elif 31 <= yaş <= 64:
  print("Yetişkin")
elif yaş >= 65:
  print("Olgun")
else:
  print("Geçersiz")

"""Task-10 Kullanıcı bir kelime girecek, sonu "miş" le mi bitiyor kontrol edilecek. mesaj yazdıracaksınız."""

kelime = input("Bir kelime girin: ")
if kelime.endswith("miş"):
  print("Kelime 'miş' ile bitiyor.")
else:
  print("Kelime 'miş' ile bitmiyor.")

"""Task-11 Hesap makinesi. Kullanıcıdan hangi işlemi yapmak istediği metin olarak alınacak. "bol" "carp" gibi."""

islem = input("Hangi işlemi yapmak istersiniz? (topla, cikar, carp, bol): ")
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
if islem == "topla":
  sonuc = sayi1 + sayi2
  print("Sonuç= ", str(sonuc))
elif islem == "cikar":
  sonuc = sayi1 - sayi2
  print("Sonuç= ", str(sonuc))
elif islem == "carp":
  sonuc = sayi1 * sayi2
  print("Sonuç= ", str(sonuc))
elif islem == "bol":
  sonuc = sayi1 / sayi2
  print("Sonuç= ", str(sonuc))
else:
  print("Lütfen geçerli bir işlem adı girin.")

"""Task-12 Aslandan kaçma oyunu
Bir aslanla karşılaştınız ne yapardınız?
1-Kaçardım
2-Ağaca tırmanırdım

1 seçeneği seçilirse
    1-Nehire doğru
    2-Otoyola doğru
eğer burda 1 seçilirse aslana yakalanacak, 2 seçilirse aslandan kaçabilecek.

2 seçeneği seçilirse
    1-En yakın
    2-Biraz daha uzak ama daha uzun
eğer burada 1 seçeneği seçilirse aslan sizi yakalayacak.
"""

secenek1 = str(input("Bir aslanla karşılaşsanız ne yapardınız? (1= Kaçardım, 2= Ağaca tırmanırdım) Lütfen 1 veya 2 girin : "))
if secenek1 == "1":
  secenek2 = str(input("Nereye doğru kaçardınız? 1= Nehire doğru 2= Otoyola doğru : "))
  if secenek2 == "1":
    print("Üzgünüm aslan sizi yakaladı...")
  elif secenek2 == "2":
    print("Tebrikler, aslandan kaçmayı başardınız.")
if secenek1 == "2":
  secenek2 = str(input("Hangi ağaca tırmanırdınız? 1= En yakın 2= Biraz daha uzak ama daha uzun : "))
  if secenek2 == "1":
    print("Üzgünüm aslan sizi yakaladı...")
  elif secenek2 == "2":
    print("Tebrikler, aslandan kaçmayı başardınız.")