with st.form("certificado_formulario"):

    st.markdown("### 📄 Formulario de registro")

    st.markdown('<p style="color:#0056B3;font-weight:bold">📅 Fecha</p>', unsafe_allow_html=True)
    fecha = st.date_input("", value=date.today())

    st.markdown('<p style="color:#0056B3;font-weight:bold">🧾 Orden</p>', unsafe_allow_html=True)
    orden = st.text_input("")

    st.markdown('<p style="color:#0056B3;font-weight:bold">🚛 Placa</p>', unsafe_allow_html=True)
    placa = st.text_input("")

    st.markdown('<p style="color:#0056B3;font-weight:bold">🔢 Código del producto</p>', unsafe_allow_html=True)
    codigo = st.text_input("")

    st.markdown('<p style="color:#0056B3;font-weight:bold">📦 Cantidad</p>', unsafe_allow_html=True)
    cantidad = st.number_input("", min_value=0, step=1)

    st.markdown('<p style="color:#0056B3;font-weight:bold">🔖 Lote</p>', unsafe_allow_html=True)
    lote = st.text_input("")

    st.markdown('<p style="color:#0056B3;font-weight:bold">📅 Fecha de vencimiento</p>', unsafe_allow_html=True)
    vencimiento = st.date_input("")

    enviado = st.form_submit_button("Guardar")

    if enviado:
        st.success("✅ Registro guardado exitosamente")
        st.write("### 📋 Datos capturados:")
        st.write(f"Fecha: {fecha}")
        st.write(f"Orden: {orden}")
        st.write(f"Placa: {placa}")
        st.write(f"Código del producto: {codigo}")
        st.write(f"Cantidad: {cantidad}")
        st.write(f"Lote: {lote}")
        st.write(f"Fecha de vencimiento: {vencimiento}")
