
from flask import Flask, request
from generar_pdf import generar_pdf
from enviar_email import enviar_pdf

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def recibir_pago():
    data = request.json
    if data.get('type') == 'payment' and data['data'].get('status') == 'approved':
        nombre = data['data']['payer']['first_name']
        apellido = data['data']['payer']['last_name']
        email = data['data']['payer']['email']
        archivo = generar_pdf(nombre, apellido)
        enviar_pdf(email, archivo)
    return 'OK', 200
@app.route('/', methods=['GET'])
def home():
    return 'Servicio activo y esperando pagos de MercadoPago.', 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
