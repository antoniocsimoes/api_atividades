from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Rafael', idade=29)
    print(pessoa)
    pessoa.save()
    pessoa = Pessoas(nome='Ronaldo', idade=40)
    print(pessoa)
    pessoa.save()
    
def consulta_pessoas():    
    pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    print(pessoa)
    
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Ronaldo").first()
    pessoa.idade = 46
    pessoa.save()
    
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Rafael").first()
    pessoa.delete()

if __name__ == '__main__':
    # insere_pessoas()
    # consulta_pessoas()
    # altera_pessoa()
    # exclui_pessoa()