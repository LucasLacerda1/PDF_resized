!pip install pymupdf

import fitz  # PyMuPDF
from google.colab import files

# Upload do PDF
uploaded = files.upload()
entrada = list(uploaded.keys())[0]

# Dimensões desejadas (em cm)
largura_cm = 6.3
altura_cm = 8.8

# Conversão para pontos
largura_pt = largura_cm * 28.3465
altura_pt = altura_cm * 28.3465
retangulo_destino = fitz.Rect(0, 0, largura_pt, altura_pt)

# Abrir o PDF original
pdf_original = fitz.open(entrada)
novo_pdf = fitz.open()

for pagina in pdf_original:
    ret_original = pagina.rect
    escala_x = largura_pt / ret_original.width
    escala_y = altura_pt / ret_original.height
    escala = fitz.Matrix(escala_x, escala_y)  # Estica o conteúdo!

    nova_pagina = novo_pdf.new_page(width=largura_pt, height=altura_pt)

    # Insere a página original redimensionada SEM preservar proporção
    nova_pagina.show_pdf_page(
        retangulo_destino,
        pdf_original,
        pagina.number,
        escala
    )

# Salvar resultado
saida = "PDF_resized.pdf"
novo_pdf.save(saida)
novo_pdf.close()
pdf_original.close()

files.download(saida)
