import httpx
from app.core.config import settings

class PseudocodeGeneratorService:
    """
    Service class untuk mengelola logika generasi pseudocode.
    """
    def __init__(self):
        self.api_key = settings.OPENROUTER_API_KEY
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY tidak ditemukan.")
        
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.system_prompt = self._get_system_prompt()
    
    def _get_system_prompt(self) -> str:
        """
        Mendefinisikan system prompt yang akan digunakan.
        """
        return """
Anda adalah Pseudofy, AI generator pseudocode berbasis standar industri Indonesia. Tugas Anda: Hasilkan pseudocode yang akurat, terstruktur, dan independen bahasa dari input pengguna (teks deskripsi masalah, kode sederhana, atau contoh soal). Patuhi ketat konvensi berikut, disintesis dari analisis fundamental pseudocode: definisi sebagai representasi informal logika algoritmik, fungsi sebagai alat desain/komunikasi/dokumentasi, dan panduan gaya profesional untuk pelatihan AI.

Aturan Wajib:
- Struktur Pseudocode: 
    - PROGRAM [Nama_Deskriptif]: Judul ringkas dan deskriptif (gunakan PascalCase atau snake_case, ganti spasi dengan _).
    - DEKLARASI: Deklarasikan semua variabel/konstanta dengan tipe data (INTEGER, REAL, STRING, BOOLEAN, ARRAY OF [tipe], CONSTANT).
    - ALGORITMA: Implementasi logika dengan BEGIN...END, urutkan langkah secara sekuensial.
- Kata Kunci: Semua huruf kapital (IF, THEN, ELSE, ENDIF, FOR, TO, STEP, ENDFOR, WHILE, DO, ENDWHILE, REPEAT, UNTIL, SWITCH, CASE, DEFAULT, ENDSWITCH, FUNCTION, PROCEDURE, RETURN, ENDFUNCTION, ENDPROCEDURE, READ, INPUT, PRINT, DISPLAY, WRITE).
- Indentasi: Gunakan 2 atau 4 spasi konsisten untuk blok bersarang (IF, FOR, WHILE, dll.).
- Penamaan: Deskriptif/mnemonic (camelCase atau snake_case untuk variabel, PascalCase untuk program/subrutin).
- Penugasan: Gunakan ← (panah kiri) untuk assign nilai, == untuk kesetaraan.
- Pernyataan: Satu per baris, ringkas, fokus pada logika inti tanpa detail implementasi rendah (abstraksikan kompleksitas).
- Komentar: Opsional, gunakan // untuk penjelasan 'mengapa' jika diperlukan, bukan 'apa'.
- Output: HANYA PSEUDOCODE MURNI DALAM FORMAT TEKS. TANPA NARASI, PENJELASAN, KODE AKTUAL, ATAU TEKS TAMBAHAN APAPUN. Jika input tidak valid (misalnya, bukan deskripsi algoritma), output pseudocode sederhana untuk error handling. Validasi logis: Pastikan pseudocode benar, efisien, dan sesuai prinsip algoritmik (deteksi bug awal, edge cases).
- Normalisasi untuk AI: Hindari 'language shadow' (jangan mirip sintaks spesifik seperti Python/Java); terinspirasi Pascal/Algol untuk eksplisitas dan keterbacaan mesin.

Contoh (dari katalog standar): Untuk 'hitung faktorial iteratif, tolak input negatif':
PROGRAM Hitung_Faktorial_Iteratif
DEKLARASI
    n : INTEGER
    faktorial : INTEGER
    CONSTANT ERROR_MSG : STRING = "Input negatif tidak diizinkan"
ALGORITMA
BEGIN
    READ(n)
    IF n < 0 THEN
        PRINT(ERROR_MSG)
    ELSE
        faktorial ← 1
        FOR i ← 1 TO n STEP 1
            faktorial ← faktorial * i
        ENDFOR
        PRINT(faktorial)
    ENDIF
END
"""

    async def generate_pseudocode(self, user_prompt: str) -> str:
        """
        Metode asinkronus untuk memanggil AI API dan mendapatkan pseudocode.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://127.0.0.1:8000",
            "X-Title": "Pseudofy"
        }

        payload = {
            "model": "qwen/qwen3-coder:free",
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.2,
            "max_tokens": 2048
        }

        async with httpx.AsyncClient(timeout=60.0) as client:
            try:
                response = await client.post(self.api_url, json=payload, headers=headers)
                response.raise_for_status()

                data = response.json()
                if "choices" in data and len(data["choices"]) > 0:
                    content = data["choices"][0]["message"]["content"].strip()
                    if content.startswith("```plaintext"):
                        content = content[len("```plaintext"):].strip()
                    if content.startswith("```"):
                        content = content[len("```"):].strip()
                    if content.endswith("```"):
                        content = content[:-len("```")].strip()
                    return content
                else:
                    raise ValueError("Respons dari API tidak valid atau tidak berisi 'choices'.")
            except httpx.HTTPStatusError as e:
                raise e