from flask import Flask

def iniciar_servicio_web():
    app = Flask(__name__)

    @app.route("/")
    def inicio():
        return "Bienvenido a la web de PABLO"

    app.run()

# Ejemplo de uso
iniciar_servicio_web()

