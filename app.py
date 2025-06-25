from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    
    <h1>FARIAS.BET</h1>
    <h2>Bem-Vindo ao site de apostas</h2>
    <p>Esse é um site de apostas legais dentro das permissões governamentais, é um site pribido para menores de 18 anos de idade </p>

    <p>Alguns topicos para que você possa investir</p>

    <ul><li>Futebol</li></ul>
    <ul><li>Basquete</li></ul>

    <a href="https://www.bet365.bet.br/#/HO/"> Ir para site de apostas</a>
    <br>
    <a href="/sobre"> Ir para sobre</a>
    """
@app.route("/sobre")
def sobre():
    return """
    <h1>SOBRE O NOSSO SITE</h1>

    <h2>Junte-se a 10 milhões de clientes em todo o mundo</h2><br>
<P>1 Pagamento Antecipado Receba seus ganhos antecipadamente ao escolher o time que abrir a vantagem necessária.<br><br>

2 Super Odds Aumentamos as cotações para você ter mais lucro nos seus bilhetes.<br><br>

3 Inteligência Artificial Utilizamos a IA para garantir a sua melhor experiência dentro do nosso site.<br><br>

4 Cashback Semanal Clientes ativos recebem cashback toda semana para apostas esportivas e cassino.<br><br>

5 Freebet Semanal Clientes que fazem bilhetes recebem uma freebet todo sábado!</p><br><br>

    """

if __name__ == "__main__":
    app.run(debug=True)

    #farias 