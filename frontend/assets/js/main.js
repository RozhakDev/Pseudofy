document.addEventListener('DOMContentLoaded', () => {

    const generateBtn = document.getElementById('generate-btn');
    const loader = document.getElementById('loader');
    const resultElement = document.getElementById('result')?.querySelector('code');
    const inputElement = document.getElementById('pseudocode-input');

    if (!generateBtn || !loader || !resultElement || !inputElement) {
        console.error("Inisialisasi gagal: Satu atau lebih elemen UI penting tidak ditemukan pada DOM.");
        return;
    }

    const handleGenerate = () => {
        const input = inputElement.value.trim();

        if (!input) {
            alert('Mohon masukkan deskripsi terlebih dahulu.');
            return;
        }

        loader.style.display = 'flex';
        resultElement.textContent = '';
        resultElement.style.color = '';

        fetch('http://127.0.0.1:8000/api/v1/pseudocode/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({ prompt: input })
        })
        .then(async response => {
            if (!response.ok) {
                const error = new Error(`Error HTTP! Status: ${response.status}`);
                try {
                    error.data = await response.json();
                } catch (e) {
                    error.data = { detail: 'Tidak dapat membaca respons error dari server.' };
                }
                throw error;
            }
            return response.json();
        })
        .then(data => {
            resultElement.textContent = data.pseudocode;
            
            if (window.hljs && typeof window.hljs.highlightElement === 'function') {
                hljs.highlightElement(resultElement);
            }
            if (window.pseudofyUI && typeof window.pseudofyUI.saveToHistory === 'function') {
                window.pseudofyUI.saveToHistory(input, data.pseudocode);
            }
        })
        .catch(error => {
            console.error('Error Fetch:', error);
            resultElement.style.color = '#f87171';

            let pesanError = `Terjadi kesalahan.\n\nDetail: ${error.message}`;

            if (error.data && error.data.detail) {
                if (Array.isArray(error.data.detail)) {
                    const validationErrors = error.data.detail.map(err => 
                        `- Lokasi: ${err.loc.join(' -> ')}\n  Kesalahan: ${err.msg}`
                    ).join('\n\n');
                    pesanError = `Error Validasi Backend (422):\nData yang dikirim tidak valid.\n\n${validationErrors}`;
                } else {
                    pesanError = `Kesalahan Backend:\n${error.data.detail}`;
                }
            }
            
            resultElement.textContent = pesanError;
        })
        .finally(() => {
            loader.style.display = 'none';
        });
    };

    generateBtn.addEventListener('click', handleGenerate);
});