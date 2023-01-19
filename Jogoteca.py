from flask import Flask, render_template, request, redirect

class Jogos():
    def __init__(self, nome, genero, console):
        self.nome = nome
        self.genero = genero
        self.console = console

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('lista_jogos.html', titulo="Jogos", jogos = lista)

jogo1 = Jogos('Fortnite', 'Battle Royale', 'PC')
jogo2 = Jogos('Spider-Man PS4', 'Ação', 'PS4')
jogo3 = Jogos('God of War', 'Ação', 'PS4')
lista = [jogo1, jogo2, jogo3]

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo="Novo Jogo")

@app.route('/criar', methods= ['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogos(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

app.run(debug=True)