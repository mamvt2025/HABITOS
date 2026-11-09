import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="UN NUEVO ESTILO D VIDA, CONTROLANDO TU SHABITOS",
    page_icon="🌟",
    layout="wide"
)

# CSS personalizado
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #667eea, #764ba2, #6dd5ed);
}

h1, h2, h3 {
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("🌟 Tracker de Hábitos Semanal")

# Días
dias = [
    "Lunes",
    "Martes",
    "Miércoles",
    "Jueves",
    "Viernes",
    "Sábado",
    "Domingo"
]

# Inicializar datos
if "habitos" not in st.session_state:
    st.session_state.habitos = {
        dia: [] for dia in dias
    }

# Agregar hábito
st.subheader("➕ Agregar nuevo hábito")

nombre = st.text_input("Nombre del hábito")
dia_seleccionado = st.selectbox(
    "Selecciona un día",
    dias
)

if st.button("Agregar hábito"):
    if nombre.strip():
        st.session_state.habitos[dia_seleccionado].append({
            "nombre": nombre,
            "completado": False
        })
        st.success("✅ Hábito agregado")

st.markdown("---")

# Crear pestañas
tabs = st.tabs(dias)

for i, dia in enumerate(dias):

    with tabs[i]:

        st.subheader(f"📅 {dia}")

        if len(st.session_state.habitos[dia]) == 0:
            st.info("No hay hábitos para este día.")

        for j, habito in enumerate(st.session_state.habitos[dia]):

            completado = st.checkbox(
                habito["nombre"],
                value=habito["completado"],
                key=f"{dia}_{j}"
            )

            st.session_state.habitos[dia][j]["completado"] = completado

            if completado:
                st.success(
                    f"✅ {habito['nombre']} completado"
                )

# Resumen
st.markdown("---")
st.subheader("📊 Progreso General")

total = 0
hechos = 0

for dia in dias:

    for habito in st.session_state.habitos[dia]:

        total += 1

        if habito["completado"]:
            hechos += 1

if total > 0:

    porcentaje = hechos / total

    st.progress(porcentaje)

    st.metric(
        "Progreso Total",
        f"{porcentaje * 100:.0f}%"
    )

else:
    st.info("Agrega hábitos para comenzar.")