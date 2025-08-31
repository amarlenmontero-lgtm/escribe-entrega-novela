
GUÍA DE INSTALACIÓN EN VPS HOSTINGER (Ubuntu 22.04)

1. Conéctate por SSH:
   ssh root@TU_IP_DEL_VPS

2. Instala Python y dependencias:
   sudo apt update
   sudo apt install python3 python3-pip
   pip install -r requirements.txt

3. Sube el archivo ENTRE_SOMBRAS_Y_SEDA_DDI.pdf al mismo directorio.

4. Configura tu certificado SSL:
   - Coloca cert.pem y key.pem en el mismo directorio.

5. Ejecuta el servidor:
   python3 webhook_server.py

6. Configura el Webhook en MercadoPago:
   - URL: https://TU_DOMINIO.com/webhook
   - Eventos: payment.created, payment.approved

7. Verifica que el PDF se genere y se prepare para enviar por email.

NOTA: Configura tu servidor SMTP en enviar_email.py para que el correo se envíe automáticamente.
