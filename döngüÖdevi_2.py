"""Problem 2
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4"""

sayi = int(input("Bir sayı giriniz : "))
basamak_sayisi = ((len(str(sayi))))
arrayN = [x for i in str(sayi) for x in i]

arrayU = [int(x)** (len(str(sayi))) for x in (arrayN)]

toplam = 0

for i in arrayU :
    toplam +=i
if toplam== sayi :
    print("Girilen Sayı 'Armstrong' Sayıdır")
else:
    print("Girilen Sayı 'Armstrong' Sayı Değildir")