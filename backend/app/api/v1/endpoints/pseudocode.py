from fastapi import APIRouter, HTTPException, status
from app.schemas.pseudocode import PseudocodeRequest, PseudocodeResponse
from app.services.ai_service import PseudocodeGeneratorService

router = APIRouter()
ai_service = PseudocodeGeneratorService()

@router.post(
    "/generate",
    response_model=PseudocodeResponse,
    summary="Generate Pseudocode",
    description="Menerima deskripsi masalah dan menghasilkan pseudocode yang terstruktur."
)
async def generate_pseudocode_endpoint(request: PseudocodeRequest):
    """
    Endpoint untuk memproses permintaan pembuatan pseudocode.
    Ini adalah fungsi asinkronus yang menangani request HTTP.
    """
    try:
        generated_code = await ai_service.generate_pseudocode(request.prompt)
        return PseudocodeResponse(pseudocode=generated_code)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Gagal menghasilkan pseudocode: {str(e)}"
        )