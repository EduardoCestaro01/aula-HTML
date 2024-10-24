from flask import (Flask, render_template, request) # import


app = Flask(__name__) # cria uma instância

@app.route("/", methods=('GET',)) #Assina una rota

def index():
    nome = request.args.get('nome')
    return f"""<h1>Página inicial</h1>
    <p>Olá {nome}, que nome bonito!"""



@app.route("/galeria", methods=('GET',))
def galeria():
    return "<h1>Galeria</h1>"

@app.route("/contato", methods=('GET',))
def contato():
    return "<h1>Contato</h1>"

@app.route("/sobre", methods=('GET',))
def sobre():
    return "<h1>Sobre</h1>"
@app.route("/area/<float:largura>/<float:comprimento>")
def area(largura, comprimento: float):
    return f""" 
    <h1> A área informada> L={largura}* A={comprimento}  Area={largura*comprimento}
    </h1>"""

@app.route("/parimpar/<float:numero>", methods=('GET',))
def parimpar(numero):
  if numero % 2 == 0:
    return f"O número {numero} é par."
  else:
    return f"O número {numero} é ímpar."
    
    
@app.route("/nome/<string:nome>/<string:sobrenome>", methods=('GET',))
def nomesobrenome(nome,sobrenome):
    return f"""<h1> sobrenome </h1>
  <p>{sobrenome},{nome}</p>"""

@app.route("/potencia/<float:numero>/<float:elevado>")
def potencia(numero: float, elevado:float):
    return f""" 
    <h1> A potencia informada> N={numero}** E={elevado}  Potencia={numero**elevado}
    </h1>"""

@app.route("/tabuada")
@app.route("/tabuada/<num>", methods=['GET'])
def tabuada(num = None):

    if'num' in request.args:
       num = request.args.get('num')
       num= int(request.args.get('num'))

    return render_template('tabuada.html', num=num)