kendaraan = ["sepeda", "motor", "becak", "mobil", "pesawat"]
warna = ["merah", "kuning", "putih", "hijau"]

print("==== Program Pilihan Kendaraan ========")
print("1. Sepeda")
print("2. Becak")
print("3. Motor")
print("4. Mobil")
print("5. Pesawat")

# Meminta input pilihan kendaraan
pilihan_kendaraan = int(input("Silakan masukkan pilihan kendaraan (1-5): "))

# Meminta input pilihan warna
print("\nPilih warna:")
print("1. Merah")
print("2. Kuning")
print("3. Putih")
print("4. Hijau")
pilihan_warna = int(input("Silakan masukkan pilihan warna (1-4): "))

# Validasi input pilihan kendaraan dan warna
if 1 <= pilihan_kendaraan <= 5 and 1 <= pilihan_warna <= 4:
    kendaraan_terpilih = kendaraan[pilihan_kendaraan - 1]  # Menyesuaikan index
    warna_terpilih = warna[pilihan_warna - 1]  # Menyesuaikan index
    
    print(f"\nKendaraan yang Anda pilih adalah {kendaraan_terpilih} dengan warna {warna_terpilih}.")
else:
    print("\nPilihan tidak valid! Pastikan memasukkan angka yang sesuai.")
