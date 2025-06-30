with st.form("certificado_formulario"):
    # 🔧 Ajuste visual para etiquetas legibles
    st.markdown("""
        <style>
        label, .stTextInput label, .stDateInput label, .stNumberInput label {
            color: #333333 !important;
            font-weight: bold;
            font-size: 16px;
        }
        </style>
    """, unsafe_allow_html=True)

    fecha = st.date_input("📅 Fecha", value=date.today())
    orden = st.text_input("🧾 Orden")
    placa = st.text_input("🚛 Placa")
    codigo = st.text_input("🔢 Código del producto")
    cantidad = st.number_input("📦 Cantidad", min_value=0, step=1)
    lote = st.text_input("🔖 Lote")
    vencimiento = st.date_input("📅 Fecha de vencimiento")

    enviado = st.form_submit_button("Guardar")

    if enviado:
        st.success("✅ Registro guardado exitosamente")
        st.write("### 📄 Datos capturados:")
        st.write(f"Fecha: {fecha}")
        st.write(f"Orden: {orden}")
        st.write(f"Placa: {placa}")
        st.write(f"Código del producto: {codigo}")
        st.write(f"Cantidad: {cantidad}")
        st.write(f"Lote: {lote}")
        st.write(f"Fecha de vencimiento: {vencimiento}")
