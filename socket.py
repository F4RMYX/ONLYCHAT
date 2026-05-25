from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta_para_sesiones'
# Inicializamos SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")

# Ruta principal que carga tu interfaz HTML
@app.route('/')
def index():
    return render_template('index.html')

# Evento que escucha cuando alguien envía un mensaje
@socketio.on('enviar_mensaje')
def manejar_mensaje(data):
    # 'broadcast=True' envía el mensaje a TODOS los usuarios conectados
    emit('recibir_mensaje', data, broadcast=True)

if __name__ == '__main__':
    # Ejecutamos el servidor
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)