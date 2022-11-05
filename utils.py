from models import Pessoas, Usuarios

# insere dados na tabela Pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Rafael', idade=29)
    #print(pessoa)
    pessoa.save()

# Consulta dados na tabela Pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    #pessoa = Pessoas.query.filter_by(nome='Galleani').first()
    #print(pessoa.idade)
    #print(pessoa)

# Altera dados na tabela Pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.nome = 'Felipe'
    pessoa.save()

# Exclui dados na tabela Pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Marcos').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    insere_usuario('rafael', '1234')
    insere_usuario('galleani', '321')
    consulta_todos_usuarios()
    # insere_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    # consulta_pessoas()
