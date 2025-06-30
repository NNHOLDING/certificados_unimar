import streamlit as st
from datetime import date

# 🎨 CSS personalizado
estilos = """
<style>
body {
    background-color: #1B8FFE;
    font-family: 'Roboto', sans-serif;
    color: white;
    text-align: center;
}
h1, h2 {
    color: white;
}
div.stForm {
    background-color: white;
    border-radius: 10px;
    padding: 20px;
    color: #2c3e50;
}
button[kind="primary"] {
    background-color: #27ae60;
    color: white;
    font-size: 18px;
    border: none;
    border-radius: 5px;
}
button[kind="primary"]:hover {
    background-color: #2ecc71;
}
footer {
    margin-top: 30px;
    padding: 10px;
    background-color: #0A6ACF;
    color: white;
    font-size: 14px;
    border-radius: 5px;
}
</style>
"""

# 🖌️ Inyectar estilos
st.markdown(estilos, unsafe_allow_html=True)

# 🧾 Encabezado
st.set_page_config(page_title="Certificados Unimar", layout="centered")
st.title("Certificados Unimar")
st.subheader("SMART INTELLIGENCE TOOLS")

# 📋 Formulario
with st.form("certificado_formulario"):
    fecha = st.date_input("📅 Fecha", value=date.today())
    orden = st.text_input("🧾 Orden")
    placa = st.text_input("🚛 Placa")
    codigo = st.text_input("🔢 Código producto")
    cantidad = st.number_input("📦 Cantidad", min_value=0, step=1)
    lote = st.text_input("🔖 Lote")
    vencimiento = st.date_input("📅 Fecha de vencimiento")
    enviado = st.form_submit_button("Guardar")

    if enviado:
        st.success("✅ Registro guardado exitosamente")
        st.write("### 📦 Datos capturados:")
        st.write(f"Fecha: {fecha}")
        st.write(f"Orden: {orden}")
        st.write(f"Placa: {placa}")
        st.write(f"Código producto: {codigo}")
        st.write(f"Cantidad: {cantidad}")
        st.write(f"Lote: {lote}")
        st.write(f"Fecha de vencimiento: {vencimiento}")

# 🧾 Footer simulado
st.markdown("""
<footer>
NN Holding Solutions Ever Be Better© Todos los derechos reservados, 2025
</footer>
""", unsafe_allow_html=True)