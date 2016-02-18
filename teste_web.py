from flask import Flask
import random
rr = random.randrange

app = Flask(__name__)
app.debug = True


@app.route("/")
def hello():
    dias = 30
    tabela = "<table>{}</table>"
    linhas = ""
    for linha in (0, 1, 2):
        linha_html = "<tr>{}</tr>"
        dias = ""
        for dia_linha in range(10):
            dia  = linha * 10 + dia_linha + 1
            cor = "{:02x}{:02x}{:02x}".format (
                0,
                int (255 / 10 * dia_linha),
                255 - int (255 / 10 * dia_linha) )
            dia_html = """    <td style="background: #{};">{}</td>\n""".format(cor, dia)
            dias += dia_html
        linhas += linha_html.format(dias)
    html = tabela.format(linhas)
            
    return """<h1>Alô mundo!<h1>""" + html

if __name__ == "__main__":
    app.run()