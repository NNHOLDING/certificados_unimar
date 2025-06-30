import streamlit as st
from datetime import datetime, date

# 🧾 Encabezado
st.set_page_config(page_title="Certificados Unimar", layout="centered")
st.title("Certificados Unimar")
st.subheader("SMART INTELLIGENCE TOOLS")

# 🧩 Formulario
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
        # 🗒️ Simulación de guardado (puedes reemplazar con Google Sheets o base de datos)
        st.success("✅ Registro guardado exitosamente")
        st.write("### Datos capturados:")
        st.write(f"Fecha: {fecha}")
        st.write(f"Orden: {orden}")
        st.write(f"Placa: {placa}")
        st.write(f"Código producto: {codigo}")
        st.write(f"Cantidad: {cantidad}")
        st.write(f"Lote: {lote}")
        st.write(f"Fecha de vencimiento: {vencimiento}")
