
import fitz  # PyMuPDF

def generar_pdf(nombre, apellido):
    comprador = f"{nombre} {apellido}"
    marca_agua = f"Comprado por {comprador}"
    contrasena = f"{nombre}_{apellido}1234"
    archivo_original = "ENTRE_SOMBRAS_Y_SEDA_DDI.pdf"
    archivo_marca = "temp_marca_agua.pdf"
    archivo_final = f"novela_{nombre}_{apellido}_protegido.pdf"

    doc = fitz.open(archivo_original)
    for i in range(1, len(doc)):
        pagina = doc[i]
        rect = fitz.Rect(20, pagina.rect.height - 40, pagina.rect.width - 20, pagina.rect.height - 20)
        pagina.insert_textbox(rect, marca_agua, fontsize=10, color=(0.5, 0.5, 0.5), rotate=0, overlay=True)
    doc.save(archivo_marca)
    doc.close()

    doc_final = fitz.open(archivo_marca)
    doc_final.save(archivo_final, encryption=fitz.PDF_ENCRYPT_AES_256, owner_pw=contrasena, user_pw=contrasena)
    doc_final.close()

    return archivo_final
