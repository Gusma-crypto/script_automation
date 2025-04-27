# Dictionary contoh
mahasiswa = {
    "nama": "Andi",
    "umur": 21,
    "jurusan": "Informatika",
    "IPK": 3.8
}

# Mengambil semua keys
keys = mahasiswa.keys()
print("Keys:", keys)

Value = mahasiswa.values()
print("value :", Value)


item = mahasiswa.items()
print(item)

nama = mahasiswa.get('nama')
print(nama)