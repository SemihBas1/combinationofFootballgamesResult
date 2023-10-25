import os
from itertools import product

def main():
    n = int(input("Kaç maç gireceksiniz? "))

    maclar = {}

    for i in range(n):
        mac_adi = input(f"{i + 1}. maçın adını girin: ")
        sonuclar = ['alt', 'üst']  
        maclar[mac_adi] = sonuclar

    
    kombinasyonlar = list(product(*maclar.values()))

    
    with open(os.path.expanduser("~/Desktop/mac_kombinasyonlari.txt"), "w", encoding="utf-8") as dosya:
        dosya.write("Olası Tüm Kombinasyonlar:\n")
        for i, kombinasyon in enumerate(kombinasyonlar, 1):
            dosya.write(f"{i}. Olasılık: ")
            for j, mac_adi in enumerate(maclar.keys()):
                dosya.write(f"{mac_adi}: {kombinasyon[j]}\t")
            dosya.write('\n')

if __name__ == "__main__":
    main()
3
