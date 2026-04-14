"""
Contoh Kalkulator Sederhana untuk Python
"""

def tambah(a, b):
    """Menjumlahkan dua angka"""
    return a + b

def kurang(a, b):
    """Mengurangkan dua angka"""
    return a - b

def kali(a, b):
    """Mengalikan dua angka"""
    return a * b

def bagi(a, b):
    """Membagi dua angka"""
    if b == 0:
        return "Error: Tidak bisa dibagi dengan 0!"
    return a / b

def kalkulator():
    """Program kalkulator interaktif"""
    print("=" * 40)
    print("    KALKULATOR SEDERHANA")
    print("=" * 40)
    print("Pilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Keluar (exit)")
    print("=" * 40)
    
    while True:
        pilihan = input("\nMasukkan pilihan (1/2/3/4/5): ")
        
        if pilihan == "5":
            print("Terima kasih telah menggunakan kalkulator!")
            break
        
        if pilihan in ["1", "2", "3", "4"]:
            try:
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua: "))
                
                if pilihan == "1":
                    print(f"Hasil: {angka1} + {angka2} = {tambah(angka1, angka2)}")
                elif pilihan == "2":
                    print(f"Hasil: {angka1} - {angka2} = {kurang(angka1, angka2)}")
                elif pilihan == "3":
                    print(f"Hasil: {angka1} * {angka2} = {kali(angka1, angka2)}")
                elif pilihan == "4":
                    hasil = bagi(angka1, angka2)
                    print(f"Hasil: {angka1} / {angka2} = {hasil}")
            
            except ValueError:
                print("Error: Masukkan angka yang valid!")
        else:
            print("Pilihan tidak valid! Masukkan 1, 2, 3, 4, atau 5")

if __name__ == "__main__":
    kalkulator()
