from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Rafael', idade=29)
    print(pessoa)

def consulta():
    #pessoa = Pessoas.query.filter_by(nome='Rafael')
    pessoa = Pessoas.query.all()
    print(pessoa)

if __name__ == '__main__':
    #insere_pessoas()
    consulta()