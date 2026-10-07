#Klavyeden kullanıcı istediği kadar sayi girebilecek.Kullanıcının girdiği son sayi palindrom ise o ana kadar girilen sayıların çarpımlarının yarısını bu sayi ile bölecek
#Çıkan sonucu ekrana yazdıracak programı yazınız
carpim=1
while True:
  giris=input("Bir sayi girin (Çıkmak için 'q'): ")
  if giris.lower()=='q':
    print("Islem Sonlandirildi")
    break

  if not giris.isdigit():
    print("Lutfen gecerli bir tam sayi degeri girin.")
    continue

  sayi=int(giris)
  carpim *=sayi

  if giris==giris[::-1]:
    print(f"\n-> Palindrom sayı tespit edildi: {sayi}")

    sonuc=(carpim/2)/sayi
    print(f"O ana dek olan carpim:{carpim}")
    print(f"Islem Sonucu [(Carpim/2)/Palindrom Sayi]:{sonuc}\n")
    break
