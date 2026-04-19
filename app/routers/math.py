from fastapi import APIRouter, Response, Query
from typing import List
import ziamath as zm
import zipfile
import io

router = APIRouter()

def render_svg(equation: str) -> str:
    return zm.Latex(equation).svg()

@router.get("/")
def get_math(equation: str = Query(...)):
    try:
        svg = render_svg(equation)
        return Response(content=svg, media_type="image/svg+xml")
    except Exception as e:
        return Response(content=f"Erro ao renderizar: {str(e)}",
                        media_type="text/plain", status_code=400)

@router.get("/batch")
def get_math_batch(equations: List[str] = Query(...)):
    """
    Recebe várias equações e retorna um .zip com um SVG por equação.
    Exemplo de chamada:
      GET /batch?equations=x^2&equations=\frac{1}{2}&equations=\sqrt{x}
    """
    buffer = io.BytesIO()

    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zf:
        for i, eq in enumerate(equations, start=1):
            try:
                svg = render_svg(eq)
                zf.writestr(f"equacao-{i}.svg", svg)
            except Exception as e:
                # salva um .txt de erro no lugar do SVG
                zf.writestr(f"equacao-{i}-erro.txt", str(e))

    buffer.seek(0)
    return Response(
        content=buffer.read(),
        media_type="application/zip",
        headers={"Content-Disposition": "attachment; filename=equacoes.zip"}
    )