urun_isim = []
print('Lütfen tüm ürünlerin adını aralarında boşluk olacak şekilde yazınız : ')

# Kullanıcı satırı boş atlamadığı sürece sürekli devam edecek bir döngü kuruyoruz.
# Her defasında satırı listeye append() fonksiyonu yardımı ile ekliyoruz.
while True:
    satir = input()
    if satir:
        urun_isim.append(satir)
    else:
        break


# Listedeki bütün veriyi string bir ifadeye dönüştürüyoruz.
isimler = '\n'.join(Urun_isim)
# Bu string ifadeyi boşluklar dikkate alınacak şekilde split() fonksiyonu ile parçalara ayırıyoruz.
isimler = urun_isim.split()
# Bu parçaların kaç tane olduğunu len() fonksiyonu ile buluyoruz.
length = len(isimler)
print("\n")
print("Ürün İsimleri : ")

# Bir döngü yardımı ile her isim ayrı ayrı olacak şekilde yazdırıyoruz.
for i in range(length):
    print(isimler[i])
    print('-----------')
