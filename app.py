import streamlit as st
from streamlit.components.v1 import html
from datetime import date

# 🎨 Estilos visuales
estilos = """
    <style>
    .main {
        background-color: #1B8FFE;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3 {
        color: white !important;
        text-align: center;
    }
    .stForm {
        background-color: white;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
        color: #333333;
        max-width: 600px;
        margin: auto;
    }
    footer {
        margin-top: 30px;
        padding: 10px;
        background-color: #0A6ACF;
        color: white;
        font-size: 14px;
        text-align: center;
        border-radius: 5px;
    }
    </style>
"""
st.markdown(estilos, unsafe_allow_html=True)

# 🧾 Encabezado
st.set_page_config(page_title="Certificados Unimar", layout="centered")
st.title("Certificados Unimar")
st.subheader("SMART INTELLIGENCE TOOLS")

# 📋 Formulario con etiquetas visibles
with st.form("certificado_formulario"):
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

# 📷 Escáner de código de barras con cámara
st.header("📷 Escáner de Código de Barras")
st.markdown("Activa tu cámara y escanea un código. El resultado aparecerá abajo:")

html("""
<script src="https://cdnjs.cloudflare.com/ajax/libs/quagga/0.12.1/quagga.min.js"></script>
<div id="scanner-container" style="width: 100%; max-width: 500px; margin: auto;"></div>
<h3 id="result" style="text-align: center; color: #333;">Esperando escaneo...</h3>
<script>
  let resultEl = document.getElementById("result");
  Quagga.init({
      inputStream: {
          name: "Live",
          type: "LiveStream",
          target: document.querySelector('#scanner-container'),
          constraints: {
            facingMode: "environment"
          },
      },
      decoder: {
          readers: ["code_128_reader", "ean_reader", "ean_8_reader", "code_39_reader"]
      },
  }, function(err) {
      if (err) {
          console.error(err);
          resultEl.innerText = "❌ Error inicializando escáner";
          return;
      }
      Quagga.start();
  });

  Quagga.onDetected(function(data) {
      let code = data.codeResult.code;
      resultEl.innerText = "✅ Código detectado: " + code;
      Quagga.stop();
  });
</script>
""", height=400)

# 📜 Footer
st.markdown("""
<footer>
NN Holding Solutions Ever Be Better© Todos los derechos reservados, 2025
</footer>
""", unsafe_allow_html=True)
