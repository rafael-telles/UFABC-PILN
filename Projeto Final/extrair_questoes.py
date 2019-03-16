import re

from bs4 import BeautifulSoup

with open("dados/_questoes.html") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')
form = soup.find(id="form_simulado")


def remove_espacos(texto):
    tokens = re.compile("\s").split(texto)
    return " ".join([t for t in tokens if t])


def remove_origem(texto):
    # Remove texto "Questão X - "
    texto = re.sub(r'^Questão \d+\s*\w*\s*-?\s*', '', texto)
    # Remove texto "Fuvest|XXX - 20XX" no inicio da questão
    texto = re.sub(r'^(Fuvest|[A-Z]+) \d+([/-]\d+)?\s*', '', texto)
    # Remove texto "(...)" no inicio da questão
    texto = re.sub(r'^\([^)]+\)\s*', '', texto)

    return texto


disciplina = None
for e in form:
    if e == '\n' or e.name == 'br' or 'class' not in e.attrs:
        continue
    if "disciplina_titulo" in e.attrs['class']:
        disciplina = e.get_text().strip()
        pass
    if "questoes" in e.attrs['class']:
        # Remove o número da questão
        e.find("strong", {"class": "num_questao"}).extract()

        texto = e.get_text()
        texto = remove_espacos(texto)
        texto = remove_origem(texto)

        with open("dados/questoes/{}.txt".format(disciplina), "a") as f:
            f.write(texto)
            f.write("\n")
