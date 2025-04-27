# Format Pesan Log dengan logging
- Beberapa format placeholder yang umum digunakan untuk menyesuaikan format pesan log adalah:

- **%(asctime)s:** Menampilkan waktu ketika log dicatat (format default: YYYY-MM-DD HH:MM:SS,mmm).

- **%(levelname)s:** Menampilkan level log (seperti DEBUG, INFO, WARNING, ERROR, atau CRITICAL).

- **%(message)s:** Menampilkan pesan log yang ditulis.

- **%(name)s:** Menampilkan nama logger (jika ada).

- **%(module)s:** Menampilkan nama modul yang menulis log.

- **%(filename)s:** Menampilkan nama file yang menulis log.

- **%(lineno)s:** Menampilkan nomor baris tempat log dicatat.

- **%(funcName)s:** Menampilkan nama fungsi tempat log dicatat.

- **%(thread)s:** Menampilkan ID thread tempat log dicatat (berguna untuk aplikasi multithreading).

- **%(process)s:** Menampilkan ID proses tempat log dicatat.