from pydantic import BaseModel, Field

class PseudocodeRequest(BaseModel):
    """
    Model untuk request body yang dikirim dari frontend.
    """
    prompt: str = Field(
        ...,
        title="User Input",
        description="Deskripsi masalah, kode, atau soal dari pengguna.",
        max_length=2000,
        min_length=10
    )

class PseudocodeResponse(BaseModel):
    """
    Model untuk response body yang dikirim kembali ke frontend.
    """
    pseudocode: str = Field(
        ...,
        title="Generated Pseudocode",
        description="Hasil pseudocode yang dihasilkan oleh AI."
    )
    error: str | None = Field(None, title="Error Message", description="Pesan error jika terjadi kegagalan.")