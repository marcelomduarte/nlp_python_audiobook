import pyttsx3
import pdfplumber

# inicializando a engine de NLP
engine = pyttsx3.init()

# lendo o arquivo PDF
pdf = pdfplumber.open('Poemas Divertidos 6.pdf')

# gerando lista de páginas do livro (página 4 - 5)
paginas = pdf.pages[3:-17]

texto_livro = ''
for pagina in paginas:
   texto_livro +=  pagina.extract_text()
   
texto_final = texto_livro.replace('.', '. ').replace(',', ', ')

engine.save_to_file(texto_final, 'audiobook.mp3')
engine.runAndWait()
