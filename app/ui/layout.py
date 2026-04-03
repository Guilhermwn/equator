from htpy import html, head, meta, link, body, div, script
from typing import Any
from app.ui.scripts import mount_script

from app.ui.components.vuetify import VUETIFY_CSS, VUETIFY_JS, VUE_JS

def base_layout(content: Any) -> str:
    page = html[
        head[
            meta(charset="utf-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            link(rel="stylesheet", href=VUETIFY_CSS),
        ],
        body[
            div(id="app")[content],
            script(src=VUE_JS),
            script(src=VUETIFY_JS),
            script[mount_script()],
        ],
    ]
    return str(page)