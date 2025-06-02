!pip install pymupdf reportlab


from google.colab import files

uploaded = files.upload()  # Envie os dois arquivos PDF aqui
import fitz  # PyMuPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
import io

# Nomes dos arquivos PDF enviados
pdf1_name = list(uploaded.keys())[0]
pdf2_name = list(uploaded.keys())[1]

# Abrindo os dois PDFs
pdf1 = fitz.open(pdf1_name)
pdf2 = fitz.open(pdf2_name)

# Verificando o número de páginas (usar o menor para evitar erro)
num_pages = min(len(pdf1), len(pdf2))

# Lista para armazenar as páginas lado a lado
output = fitz.open()

for i in range(num_pages):
    page1 = pdf1.load_page(i)
    page2 = pdf2.load_page(i)

    # Dimensões de cada página
    rect1 = page1.rect
    rect2 = page2.rect

    # Criar nova página com largura somada (lado a lado)
    new_width = rect1.width + rect2.width
    new_height = max(rect1.height, rect2.height)
    new_page = output.new_page(width=new_width, height=new_height)

    # Inserir as páginas originais lado a lado
    new_page.show_pdf_page(rect1, pdf1, i)
    new_page.show_pdf_page(fitz.Rect(rect1.width, 0, new_width, new_height), pdf2, i)

# Salvar resultado
output_file = "PDF-name.pdf"
output.save(output_file)
output.close()

# Download
files.download(output_file)
