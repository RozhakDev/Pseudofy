# Pseudofy - Alat Pembuat Pseudocode Berbasis AI

![Pseudofy Logo](https://github.com/user-attachments/assets/987fbe02-538c-43a3-bb0b-6ffd31ffbc9f)

**Pseudofy** adalah _developer_ tool berbasis AI yang dirancang untuk mengubah deskripsi masalah, algoritma, atau bahkan potongan kode menjadi pseudocode yang terstruktur, rapi, dan sesuai dengan standar industri. Dibangun untuk mahasiswa, pengajar, dan developer, Pseudofy bertujuan untuk mempercepat alur kerja perencanaan, dokumentasi, dan pembelajaran konsep-konsep algoritmik.

Proyek ini dibangun dengan arsitektur modern yang memisahkan antara backend (API) dan frontend (antarmuka pengguna), memastikan skalabilitas dan kemudahan dalam pengembangan.

## 🚀 Fitur Utama

* **Inti AI Canggih:** Memanfaatkan model bahasa termutakhir yang diinstruksikan secara spesifik (`system prompt`) untuk memahami konteks dan menghasilkan pseudocode yang sangat akurat dan relevan.
* **Riwayat Lokal:** Semua hasil generasi disimpan secara otomatis di _local storage browser_, memungkinkan Anda untuk meninjau dan menggunakan kembali hasil sebelumnya kapan saja tanpa perlu registrasi.
* **Backend Performa Tinggi:** Dibangun di atas **FastAPI** dan **Uvicorn**, memberikan performa asinkronus yang cepat dan responsif.
* **Input Fleksibel:** Mampu menerjemahkan dari berbagai jenis input, mulai dari deskripsi naratif hingga soal-soal pemrograman.

## 🛠️ Tumpukan Teknologi

Arsitektur Pseudofy dirancang secara _decoupled_ untuk skalabilitas dan pemeliharaan yang optimal.

* **Backend:**
  * **Bahasa:** Python 3.11+
  * **Framework:** FastAPI
  * **Server:** Uvicorn
  * **Validasi Data:** Pydantic
  * **HTTP Client:** HTTPX (untuk komunikasi asinkronus dengan AI service)
* Frontend:
  * **Markup:** HTML5
  * **Styling:** Tailwind CSS
  * **Scripting:** Vanilla JavaScript (ES6+)
  * **Ikon:** Feather Icons
  * **Syntax Highlighting:** highlight.js

## ⚙️ Instalasi dan Penggunaan

Untuk menjalankan proyek ini di lingkungan lokal Anda, ikuti langkah-langkah berikut:

### Prasyarat

- Python 3.10 atau yang lebih baru
- `pip` dan `venv`
- Editor kode (seperti VS Code) dengan ekstensi **Live Server**

### 1. Clone Repository

```bash
git clone https://github.com/RozhakDev/Pseudofy.git
cd Pseudofy
```

### 2. Konfigurasi Backend

1. **Pindah ke direktori backend:**
   
   ```bash
   cd backend
   ```

2. **Install dependensi Python:**
   
   ```bash
   pip install -r requirements.txt
   ```

3. **Buat file `.env`:**
    Buat file bernama `.env` di dalam folder `backend`. Salin konten dari `.env.example` (jika ada) atau tulis langsung:
   
   ```bash
   OPENROUTER_API_KEY="ganti_dengan_api_key_openrouter_anda"
   ```

4. **Jalankan server backend:**
   
   ```bash
   python run.py
   ```
   
    Server akan berjalan di `http://127.0.0.1:8000`.

### 3. Menjalankan Frontend

1. Buka folder proyek `Pseudofy` di VS Code.
2. Klik kanan pada file `frontend/index.html`.
3. Pilih "**Open** with **Live Server**".
4. Browser akan otomatis terbuka dan menampilkan antarmuka Pseudofy. Aplikasi siap digunakan!

## 🤝 Kontribusi

Kontribusi sangat kami harapkan! Jika Anda memiliki ide untuk fitur baru, perbaikan bug, atau peningkatan lainnya, silakan buka issue atau ajukan pull request.

## 📝 Lisensi

Proyek ini dilisensikan di bawah **MIT License**. Lihat file `LICENSE` untuk detail lebih lanjut.