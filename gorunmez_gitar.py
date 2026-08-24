#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GÖRÜNMEZ GİTAR ÜSTASI EĞİTİM SİSTEMİ
Ciddi Bilimsel Eğitim Yazılımı v1.0

Bu kod, görünmez gitar çalma sanatını öğretmek için tasarlanmıştır.
Lütfen gözlerinizi kapatarak kullanın.
"""

import random
import time
import sys

# Gizli sabitler - dokunmayın
CUMHURIYET_YILI = 1923  # Bu sadece bir sayı, başka bir anlamı yok
OZEL_KATSAYI = 19  # Mayıs ayı ile alakası yoktur

class GorunmezGitarUstasi:
    def __init__(self):
        self.seviye = 1
        self.ilerleme = 0.0
        self.toplam_pratik = 0
        self.unvanlar = [
            "Acemi Görünmez Çırak",
            "Hayali Tel Hissettirici",
            "Sessiz Akor Ustası",
            "Kuantum Solo Çırak",
            "Görünmez Ritim Lordu",
            "Efsanevi Hayal Maestro",
            "Evrenin Görünmez Bestecisi"
        ]
        self.dersler = [
            "Görünmez telleri havada hissetme egzersizi",
            "Hayali akor basma (parmaklar boşlukta)",
            "Sessiz solo - kimse duymasın diye",
            "Kuantum dolaşıklık ile nota üretme",
            "Komşuyu etkilemeden performans",
            "Gözler kapalıyken tempo tutma",
            "Evrenin frekansına uyum sağlama"
        ]

    def selamla(self):
        print("=" * 60)
        print("  GÖRÜNMEZ GİTAR ÜSTASI EĞİTİM SİSTEMİ")
        print("  Resmi ve Son Derece Ciddi Eğitim Platformu")
        print("=" * 60)
        print()
        print("Hoş geldiniz, geleceğin görünmez gitar ustası.")
        print("Bu sistem sizi sıradanlıktan kurtaracak.")
        print()

    def durum_goster(self):
        unvan = self.unvanlar[min(self.seviye - 1, len(self.unvanlar) - 1)]
        print(f"\n--- Mevcut Durum ---")
        print(f"Seviye     : {self.seviye}")
        print(f"Unvan      : {unvan}")
        print(f"İlerleme   : %{self.ilerleme:.1f}")
        print(f"Toplam Pratik: {self.toplam_pratik} dakika (hayali)")
        print("-" * 30)

    def pratik_yap(self):
        print("\nPratik başlıyor...")
        print("Gözlerinizi kapatın. Parmaklarınızı havada hareket ettirin.")
        time.sleep(1.5)
        
        # Rastgele "nota" üret
        notalar = ["do", "re", "mi", "fa", "sol", "la", "si", "... (görünmez)"]
        for _ in range(5):
            nota = random.choice(notalar)
            print(f"  ♪ {nota} ", end="", flush=True)
            time.sleep(0.4)
        print("\n")

        # İlerleme rastgele
        artis = random.uniform(-5, 15)
        self.ilerleme += artis
        self.toplam_pratik += random.randint(3, 12)

        if self.ilerleme >= 100:
            self.ilerleme = 0
            self.seviye += 1
            if self.seviye > len(self.unvanlar):
                self.seviye = len(self.unvanlar)
            print("*** SEVİYE ATLADI! ***")
            print(f"Yeni unvanınız: {self.unvanlar[min(self.seviye-1, len(self.unvanlar)-1)]}")
        elif artis < 0:
            print("(Evren bugün size karşı. İlerleme geriledi. Bu normaldir.)")
        else:
            print(f"İlerleme kaydedildi: +{artis:.1f}%")

        # Gizli referans - hiçbir şey ifade etmez
        if self.seviye == 3 and random.random() < 0.3:
            print("(Sistem notu: Bazı frekanslar 19 Mayıs'ta daha güçlü hissedilir.)")

    def ders_al(self):
        ders = random.choice(self.dersler)
        print(f"\nBugünün dersi: {ders}")
        print("Lütfen talimatları takip edin (talimat yoktur, hayal edin).")
        time.sleep(1)
        print("Ders tamamlandı. Zihniniz genişledi.")

    def performans_degerlendir(self):
        puan = random.randint(40, 100)
        yorumlar = [
            "Muhteşem! Kimse duymadı ama herkes etkilendi.",
            "Teknik olarak mükemmel. Görünmezlik seviyesi yüksek.",
            "Biraz daha pratik lazım. Teller biraz görünür olmuş gibi.",
            "Efsanevi! Komşular bile alkışladı (hayali olarak).",
            "Ortalama. Ama görünmez gitar için ortalama bile efsane.",
            "Bu bir sanat eseri. Sessizlik içinde fısıldıyor."
        ]
        print(f"\nPerformans Puanı: {puan}/100")
        print(f"Değerlendirme: {random.choice(yorumlar)}")

    def menu(self):
        while True:
            self.durum_goster()
            print("\nSeçenekler:")
            print("1. Pratik Yap (Gözler kapalı önerilir)")
            print("2. Ders Al")
            print("3. Performans Değerlendir")
            print("4. Çıkış (Görünmezliğe geri dön)")
            
            secim = input("\nSeçiminiz (1-4): ").strip()
            
            if secim == "1":
                self.pratik_yap()
            elif secim == "2":
                self.ders_al()
            elif secim == "3":
                self.performans_degerlendir()
            elif secim == "4":
                print("\nSistem kapatılıyor...")
                print("Görünmez gitarınız sizi bekliyor olacak.")
                print("Hoşça kalın, usta.")
                break
            else:
                print("Geçersiz seçim. Görünmez menüde sadece 1-4 vardır.")

def main():
    sistem = GorunmezGitarUstasi()
    sistem.selamla()
    
    # Gizli başlangıç mesajı
    if CUMHURIYET_YILI > 1900:
        print("(Sistem hazır. Enerji seviyesi stabil.)\n")
    
    sistem.menu()

if __name__ == "__main__":
    main()
