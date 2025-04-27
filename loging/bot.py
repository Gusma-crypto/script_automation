import logging

# Menyiapkan konfigurasi logging
logging.basicConfig(
    level=logging.DEBUG,  # Level log yang dicatat
    format='%(asctime)s - %(levelname)s - %(message)s',  # Format log
    filename='app.log',  # Menyimpan log ke file
    filemode='a',  # Mode penulisan ke file (append)
)

def penjumlahan(a, b):
    # Mencatat nilai input
    logging.info(f'Mulai penjumlahan: {a} + {b}')
    
    try:
        # Proses penjumlahan
        hasil = a + b
        logging.debug(f'Hasil penjumlahan sementara: {hasil}')
        
        # Mencatat hasil
        logging.info(f'Penjumlahan selesai. Hasil: {hasil}')
        return hasil
    except Exception as e:
        logging.error(f'Terjadi kesalahan: {e}')
        return None

# Input angka
try:
    num1 = float(input('Masukkan angka pertama: '))
    num2 = float(input('Masukkan angka kedua: '))
    
    # Menjalankan fungsi penjumlahan
    hasil = penjumlahan(num1, num2)
    
    if hasil is not None:
        print(f'Hasil penjumlahan: {hasil}')
    else:
        print('Terjadi kesalahan dalam perhitungan.')
except ValueError as ve:
    logging.error(f'Input tidak valid: {ve}')
    print('Input tidak valid. Pastikan anda memasukkan angka.')
