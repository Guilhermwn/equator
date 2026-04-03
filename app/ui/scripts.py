from markupsafe import Markup

# ── Vue state ────────────────────────────────────────────────────────────────

_REFS = """
    const items   = ref([])
    const loading = ref(true)
    const error   = ref(null)
    const newId   = ref('')
    const newName = ref('')
"""

# ── API calls ─────────────────────────────────────────────────────────────────

_FETCH_ITEMS = """
    const fetchItems = async () => {
        loading.value = true
        error.value   = null
        try {
            const res   = await fetch('/items/')
            items.value = await res.json()
        } catch (e) {
            error.value = 'Erro ao buscar items.'
            console.error(e)
        } finally {
            loading.value = false
        }
    }
"""

_ADD_ITEM = """
    const addItem = async () => {
        error.value = null
        if (!newId.value || !newName.value) {
            error.value = 'Preencha o ID e o Nome.'
            return
        }
        try {
            const res = await fetch('/items/', {
                method:  'POST',
                headers: { 'Content-Type': 'application/json' },
                body:    JSON.stringify({
                    id:   parseInt(newId.value),
                    name: newName.value,
                }),
            })
            if (!res.ok) {
                const data  = await res.json()
                error.value = data.detail || 'Erro ao adicionar item.'
                return
            }
            newId.value   = ''
            newName.value = ''
            await fetchItems()
        } catch (e) {
            error.value = 'Erro ao conectar com a API.'
            console.error(e)
        }
    }
"""

# ── Setup return ──────────────────────────────────────────────────────────────

_SETUP_RETURN = """
    return { items, loading, error, newId, newName, addItem }
"""

# ── Vuetify bootstrap ─────────────────────────────────────────────────────────

_VUETIFY_INIT = """
    const { createApp, ref, onMounted } = Vue
    const { createVuetify, blueprints: { md3 } } = Vuetify

    const vuetify = createVuetify({
        blueprint: md3,
    })
"""

_MOUNT = """
    app.use(vuetify).mount('#app')
"""

# ── Compose ───────────────────────────────────────────────────────────────────

def _setup() -> str:
    return (
        "setup() {"
        + _REFS
        + _FETCH_ITEMS
        + _ADD_ITEM
        + "onMounted(fetchItems)"
        + _SETUP_RETURN
        + "}"
    )

def mount_script() -> Markup:
    return Markup(
        _VUETIFY_INIT
        + "const app = createApp({ " + _setup() + " })"
        + _MOUNT
    )