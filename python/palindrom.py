#Kullanıcıdan bir sayı girmesini isteyiniz.Bu sayının palindrom olup olmadığını ekrana yazdırınız.

sayi=input("Bir sayı giriniz:")
palindrom_mu=True
for i,karakter in enumerate (sayi):
  if karakter !=sayi[len(sayi)-1-i]:
    palindrom_mu=False
    break
if palindrom_mu:
  print("Sayi palindromdur.")
else:
  print("Sayi palindrom değildir.")
