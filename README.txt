
GUÍA DE INSTALACIÓN EN RENDER

1. Sube este repositorio a GitHub.
2. Ve a https://dashboard.render.com y crea un nuevo Web Service.
3. Conecta tu cuenta de GitHub y selecciona este repositorio.
4. Configura:
   - Build Command: pip install -r requirements.txt
   - Start Command: python webhook_server.py
   - Environment: Python 3
5. Render te dará una URL pública para tu webhook.
6. Configura esa URL en MercadoPago para recibir notificaciones de pago.
