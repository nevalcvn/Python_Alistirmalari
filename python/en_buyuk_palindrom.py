#İki tane 3 basamaklı sayının çarpımı olan en büyük palindromu bul.

en_buyuk_palindrom=0
sayi1=0
sayi1=0
for i in range(999,99,-1):
  for j in range(i,99,-1):
    carpim=i*j
    
    if carpim<=en_buyuk_palindrom:
      break

    carpim_str=str(carpim)
    if carpim_str==carpim_str[::-1]:
      en_buyuk_palindrom=carpim
      sayi1=i
      sayi2=j

print(f"En büyük palindrom: {en_buyuk_palindrom}")
print(f"Çarpanlar: {sayi1} x {sayi2}")
