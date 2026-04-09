from fastapi import APIRouter, Response, Query
import io

# Matplotlib
import matplotlib.pyplot as plt

# Ziamath + CairoSVG
import ziamath as zm
import cairosvg

router = APIRouter()

# CONFIGURAÇÃO GLOBAL (você troca aqui)
RENDER_MODE = "ziamath"  # "matplotlib" ou "ziamath"


def render_with_matplotlib(equation: str) -> bytes:
    fig = plt.figure()

    fig.text(
        0.5,
        0.5,
        f"${equation}$",
        horizontalalignment="center",
        verticalalignment="center",
    )

    buffer = io.BytesIO()
    plt.axis("off")
    plt.savefig(buffer, format="png", bbox_inches="tight", dpi=300, transparent=True)
    plt.close(fig)

    buffer.seek(0)
    return buffer.getvalue()


def render_with_ziamath(equation: str) -> bytes:
    svg = zm.Latex(equation).svg()
    png = cairosvg.svg2png(bytestring=svg.encode("utf-8"), dpi=300, scale=10)
    return png


@router.get("/")
def get_math(
    equation: str = Query(...),
    mode: str = Query(None, enum=["matplotlib", "ziamath"])  # opcional via URL
):
    selected_mode = mode or RENDER_MODE

    try:
        if selected_mode == "matplotlib":
            image = render_with_matplotlib(equation)

        elif selected_mode == "ziamath":
            image = render_with_ziamath(equation)

        else:
            raise ValueError("Modo inválido")

        return Response(content=image, media_type="image/png")

    except Exception as e:
        return Response(
            content=f"Erro ao renderizar: {str(e)}",
            media_type="text/plain",
            status_code=400,
        )