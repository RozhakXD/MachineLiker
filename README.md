# MachineLiker 🚀

![Machine-Liker Logo](https://github.com/user-attachments/assets/ffc96ae2-d721-469f-9aa6-43b969337136)
> 📂 **Arsip Proyek** (Tidak Aktif Sejak 2025)

## 📝 Deskripsi
Proyek ini adalah alat CLI (*Command Line Interface*) untuk mengirim Like/Reaksi otomatis ke postingan Facebook menggunakan integrasi dengan situs *machine-likers.com*. Dibuat pada **30 November 2022**, alat ini sudah tidak berfungsi lagi sejak tahun 2025 karena perubahan sistem keamanan Cloudflare di situs tujuan. Projek ini diarsipkan sebagai referensi historis dan pembelajaran.

## ✨ Fitur
- 🚀 Pengiriman *batch* Like (+50) ke tautan postingan target.
- 🔄 Sistem loop dengan jeda 30 menit antar-eksekusi.
- 🎨 Antarmuka CLI interaktif menggunakan library `rich`.
- 🔑 Login menggunakan **cookies Facebook**.
- ⚠️ **Peringatan**: Tidak kompatibel dengan akun Facebook resmi (disarankan akun palsu/baru).

## 🛠️ Prasyarat
- Python 3.12+
- Modul Python:
    - `requests`
    - `rich`

## ⚙️ Instalasi
```bash
$ pkg update -y && pkg upgrade -y
$ pkg install python-pip git
$ git clone https://github.com/RozhakXD/MachineLiker.git
$ cd MachineLiker
$ pip install -r requirements.txt
$ python Run.py
```

## 🖥️ Penggunaan (Contoh)
- Masukkan cookies Facebook (harus mengandung `c_user` dan `xs`).
- Masukkan tautan postingan target.
- Sistem akan mengirim Like secara otomatis setiap 30 menit (10x loop maksimal).

## ⚠️ Catatan Penting
- Proyek ini diarsipkan dan tidak akan diperbarui.
- Penggunaan cookies Facebook berisiko terhadap kebijakan keamanan Meta. Gunakan akun dummy!
- Error Cloudflare tidak dapat diatasi karena perubahan sistem di [machine-likers.com](https://machine-likers.com/).

## 📜 Lisensi
Proyek ini bersifat opensource untuk tujuan edukasi. Dilarang menyalahgunakan untuk aktivitas ilegal.
