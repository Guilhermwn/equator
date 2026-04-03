from markupsafe import Markup
from app.ui.layout import base_layout
from app.ui.components.vuetify import (
    v_app,
    v_container,
    v_row,
    v_col,
    v_card,
    v_card_title,
    v_card_subtitle,
    v_progress_circular,
    v_text_field,
    v_btn,
)

def home_page() -> str:
    content = v_app[
        v_container[
            # formulário de adição
            v_row[
                v_col(cols="12", sm="4")[
                    v_text_field(
                        {"v-model": "newId"},
                        label="ID",
                        type="number",
                        variant="outlined",
                    ),
                ],
                v_col(cols="12", sm="6")[
                    v_text_field(
                        {"v-model": "newName"},
                        label="Nome",
                        variant="outlined",
                    ),
                ],
                v_col(cols="12", sm="2")[
                    v_btn(
                        {"@click": "addItem"},
                        color="primary",
                        size="large",
                        block=True,
                    )[
                        Markup("Adicionar")
                    ],
                ],
            ],
            # erro
            v_row({"v-if": "error"})[
                v_col[
                    Markup('<v-alert type="error">{{ error }}</v-alert>')
                ]
            ],
            # loading spinner
            v_row({"v-if": "loading"}, justify="center")[
                v_col(cols="auto")[
                    v_progress_circular(indeterminate=True, color="primary"),
                ]
            ],
            # lista de cards
            v_row({"v-else": True})[
                v_col(
                    {"v-for": "item in items", ":key": "item.id"},
                    cols="12",
                    sm="6",
                    md="4",
                )[
                    v_card(elevation="2")[
                        v_card_title[Markup("{{ item.name }}")],
                        v_card_subtitle[Markup("ID: {{ item.id }}")],
                    ]
                ]
            ],
        ]
    ]
    return base_layout(content)