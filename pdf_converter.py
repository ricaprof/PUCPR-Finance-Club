import fitz  # PyMuPDF

# Abrir o PDF
pdf_document = "sobre nós.pdf"
doc = fitz.open(pdf_document)

# Criar o arquivo HTML
with open("output.html", "w", encoding="utf-8") as html_file:
    for page in doc:
        html_file.write(page.get_text("html"))
print("PDF convertido para HTML com sucesso!")
