import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Escáner de Códigos", layout="centered")
st.title("📷 Escáner de Código de Barras")

st.markdown("Activa tu cámara y escanea un código de barras. El código detectado aparecerá abajo.")

html("""
    <script src="https://cdnjs.cloudflare.com/ajax/libs/quagga/0.12.1/quagga.min.js"></script>
    <div id="scanner-container" style="width: 100%; max-width: 500px; margin: auto;"></div>
    <h3 id="result">Esperando escaneo...</h3>
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
