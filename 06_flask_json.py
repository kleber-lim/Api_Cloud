from flask import Flask, jsonify

app = Flask(__name__)

# Rota raiz (página inicial da API)
@app.route("/")
def home():
    return "✅ API rodando! Use /alunos ou /saudacao/<nome>"

# Rota que retorna lista de alunos em JSON
@app.route("/alunos")
def get_alunos():
    return jsonify([
        {"nome": "João", "curso": "ADS"},
        {"nome": "Maria", "curso": "CC"}
    ])

# Rota que retorna saudação personalizada
@app.route("/saudacao/<nome>")
def saudacao(nome):
    return jsonify({"mensagem": f"Olá, {nome}! Seja bem-vindo à API."})

if __name__ == "__main__":
    app.run(debug=True)
