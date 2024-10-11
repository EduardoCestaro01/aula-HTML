from flask import (Flask, request) # import


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
@app.route("/area")
def area():
    altura= float (request.args.get('a'))
    largura= float (request.args.get('l'))
    return f""" 
    <h1> A área informada> L={largura}* A={altura}  Area={largura*altura}
    </h1>"""

@app.route("/par_ou_impar", methods=('GET',))
def par_ou_impar():
  numero = float(request.args.get('n'))
  if numero % 2 == 0:
    return f"O número {numero} é par."
  else:
    return f"O número {numero} é ímpar."
  
@app.route("/sobrenome", methods=('GET',))
def nomesobrenome():
  nome = request.args.get('nome')
  sobrenome = request.args.get('sobrenome')
  return f"""<h1> sobrenome </h1>
  <p>{sobrenome},{nome}</p>"""