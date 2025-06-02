!pip install pymupdf reportlab

from google.colab import files

uploaded = files.upload()  # Envie os dois arquivos PDF aqui
import fitz  # PyMuPDF

# Pegando os nomes dos arquivos enviados
pdf_names = list(uploaded.keys())

# Abrindo os PDFs
pdfs = [fitz.open(name) for name in pdf_names]

# Verificando o número mínimo de páginas entre eles
min_pages = min(len(pdf) for pdf in pdfs)

# Criar novo PDF de saída
output = fitz.open()

for i in range(min_pages):
    pages = [pdf.load_page(i) for pdf in pdfs]
    widths = [p.rect.width for p in pages]
    heights = [p.rect.height for p in pages]

    # A largura da nova página será a maior entre os três
    new_width = max(widths)
    # A altura será a soma das três
    new_height = sum(heights)

    new_page = output.new_page(width=new_width, height=new_height)

    y_offset = 0
    for page, h in zip(pages, heights):
        rect = fitz.Rect(0, y_offset, page.rect.width, y_offset + page.rect.height)
        new_page.show_pdf_page(rect, page.parent, page.number)
        y_offset += h

# Salvar o resultado
output_file = "Folha_14.pdf"
output.save(output_file)
output.close()

# Baixar o resultado
files.download(output_file)
