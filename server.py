from flask import Flask

# Inicializar la aplicación Flask
app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return "¡Hola, Flask está en Render!"

# Si se ejecuta en modo local, usa Flask. Si está en producción, usa Gunicorn.
if __name__ == '__main__':
    import os
    if 'RENDER' in os.environ:  # Detecta si está en Render
        from waitress import serve
        serve(app, host="0.0.0.0", port=10000)
    else:
        app.run(host='0.0.0.0', port=10000, debug=True)