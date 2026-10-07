#needle metni haystack içinde ilk nerede geçiyorsa o indeksi döndür,yoksa -1.
#örneğin s1="uwefjıksadhusnmkd984"
#s2="sad" ise s1'i al,üçerli parçalara bölü.s2'de isteneni bulabilirsen,bulduğun ifadenin ilk geçmeye başladığı yerin indeksini döndür.

s1=input("Büyük metni (haystack) giriniz:")
s2=input("Aranacak ifadeyi (needle) giriniz:")
k=len(s2)
bulunan_indeks=-1

if k==0:
  bulunan_indeks=0
else:
  for i in range(len(s1)-k+1):
    parca=s1[i:i+k]
    if parca==s2:
      bulunan_indeks=i
      break


print(f"Sonuç indeksi: {bulunan_indeks}")
