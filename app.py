from flask import Flask # import


app = Flask(__name__) # cria uma instância

@app.route("/", methods=('GET',)) #Assina una rota

def index(): # função responsável pela página

 return "<h1>Página inicial</h1> <p>Eu sou fulano</p> <hr> " # HTML retornado

@app.route("/galeria", methods=('GET',))
def galeria():
    return "<h1>Galeria</h1>"

@app.route("/contato", methods=('GET',))
def contato():
    return "<h1>Contato</h1>"

@app.route("/sobre", methods=('GET',))
def sobre():
    return "<h1>Sobre</h1>"